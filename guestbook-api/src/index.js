// Guestbook API (Cloudflare Worker + D1).
// Public wall with moderation: visitors post anonymously, nothing is shown until the owner approves it,
// the owner replies from the admin endpoints, and the original visitor can keep replying in their own thread.

const MAX_NICKNAME = 30;
const MAX_BODY = 1000;
const POSTS_PER_HOUR = 5; // per IP
const PAGE_SIZE = 30;

const sha256 = async (text) => {
  const buf = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(text));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, '0')).join('');
};

const timingSafeEqual = (a, b) => {
  const x = new TextEncoder().encode(a);
  const y = new TextEncoder().encode(b);
  let diff = x.length ^ y.length;
  for (let i = 0; i < Math.max(x.length, y.length); i++) diff |= (x[i] || 0) ^ (y[i] || 0);
  return diff === 0;
};

const corsHeaders = (request, env) => {
  const origin = request.headers.get('Origin') || '';
  const allowed = (env.ALLOWED_ORIGINS || '').split(',').map((s) => s.trim());
  const headers = {
    'Access-Control-Allow-Methods': 'GET, POST, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization, X-Visitor-Token',
    'Access-Control-Max-Age': '86400',
    Vary: 'Origin',
  };
  if (allowed.includes(origin)) headers['Access-Control-Allow-Origin'] = origin;
  return headers;
};

const json = (data, status, request, env) =>
  new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json; charset=utf-8', ...corsHeaders(request, env) },
  });

const clean = (value) => (typeof value === 'string' ? value.replace(/\r\n/g, '\n').trim() : '');

const isOwner = (request, env) => {
  const header = request.headers.get('Authorization') || '';
  if (!env.ADMIN_TOKEN || !header.startsWith('Bearer ')) return false;
  return timingSafeEqual(header.slice(7), env.ADMIN_TOKEN);
};

async function listPublic(request, env, url) {
  const visitor = request.headers.get('X-Visitor-Token');
  const mine = visitor ? await sha256(`${env.HASH_SALT}:token:${visitor}`) : '';
  const offset = Math.max(0, parseInt(url.searchParams.get('offset') || '0', 10) || 0);

  // A visitor also sees their own not-yet-approved messages, marked pending.
  const tops = await env.DB.prepare(
    `SELECT id, nickname, body, created_at, status, (token_hash = ?1) AS mine
       FROM posts
      WHERE parent_id IS NULL AND (status = 'approved' OR (status = 'pending' AND token_hash = ?1))
      ORDER BY id DESC LIMIT ?2 OFFSET ?3`,
  ).bind(mine, PAGE_SIZE + 1, offset).all();

  const rows = tops.results;
  const hasMore = rows.length > PAGE_SIZE;
  const page = rows.slice(0, PAGE_SIZE);
  let replies = [];
  if (page.length) {
    const ids = page.map((r) => r.id);
    const marks = ids.map(() => '?').join(',');
    const res = await env.DB.prepare(
      `SELECT id, parent_id, author, nickname, body, created_at, status
         FROM posts
        WHERE parent_id IN (${marks}) AND (status = 'approved' OR (status = 'pending' AND token_hash = ?))
        ORDER BY id ASC`,
    ).bind(...ids, mine).all();
    replies = res.results;
  }
  const posts = page.map((r) => ({
    id: r.id,
    nickname: r.nickname,
    body: r.body,
    created_at: r.created_at,
    pending: r.status === 'pending',
    mine: !!r.mine,
    replies: replies.filter((x) => x.parent_id === r.id).map((x) => ({
      id: x.id, author: x.author, nickname: x.nickname, body: x.body, created_at: x.created_at, pending: x.status === 'pending',
    })),
  }));
  return { posts, hasMore };
}

const MAX_EMAILS_PER_HOUR = 20; // global cap so a flood of spam cannot flood the owner's inbox

// Emails the owner when a visitor posts. Never throws: a failed email must not fail the post.
async function notifyOwner(env, post) {
  try {
    if (!env.RESEND_API_KEY || !env.NOTIFY_EMAIL) return;
    const recent = await env.DB.prepare(
      `SELECT COUNT(*) AS n FROM posts WHERE author = 'visitor' AND created_at > strftime('%Y-%m-%dT%H:%M:%fZ', 'now', '-1 hour')`,
    ).first();
    if (recent.n > MAX_EMAILS_PER_HOUR) return;
    const oneLine = (t) => t.replace(/[\r\n]+/g, ' ').slice(0, 60);
    const kind = post.parentId ? 'reply in a thread' : 'new message';
    const res = await fetch(env.RESEND_API_URL || 'https://api.resend.com/emails', {
      method: 'POST',
      headers: { Authorization: `Bearer ${env.RESEND_API_KEY}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({
        from: 'Guestbook <onboarding@resend.dev>',
        to: [env.NOTIFY_EMAIL],
        subject: `Guestbook: ${kind} from ${oneLine(post.nickname)}`,
        text: `${post.nickname} wrote:\n\n${post.body}\n\nReview and reply: ${env.ADMIN_URL || ''}\n`,
      }),
    });
    if (!res.ok) console.error('notify failed', res.status, await res.text());
  } catch (err) {
    console.error('notify error', err);
  }
}

async function createPost(request, env) {
  let input;
  try { input = await request.json(); } catch { return [{ error: 'Invalid JSON' }, 400]; }
  const nickname = clean(input.nickname);
  const body = clean(input.body);
  const token = typeof input.token === 'string' ? input.token : '';
  const parentId = input.parent_id == null ? null : Number(input.parent_id);

  if (!nickname || nickname.length > MAX_NICKNAME) return [{ error: `Nickname must be 1-${MAX_NICKNAME} characters` }, 400];
  if (!body || body.length > MAX_BODY) return [{ error: `Message must be 1-${MAX_BODY} characters` }, 400];
  if (!/^[0-9a-f]{32,128}$/.test(token)) return [{ error: 'Missing visitor token' }, 400];
  if (parentId !== null && !Number.isInteger(parentId)) return [{ error: 'Invalid parent' }, 400];

  const tokenHash = await sha256(`${env.HASH_SALT}:token:${token}`);
  const ip = request.headers.get('CF-Connecting-IP') || 'local';
  const ipHash = await sha256(`${env.HASH_SALT}:ip:${ip}`);

  const recent = await env.DB.prepare(
    `SELECT COUNT(*) AS n FROM posts WHERE ip_hash = ? AND created_at > strftime('%Y-%m-%dT%H:%M:%fZ', 'now', '-1 hour')`,
  ).bind(ipHash).first();
  if (recent.n >= POSTS_PER_HOUR) return [{ error: 'Too many messages, please try again later' }, 429];

  if (parentId !== null) {
    // Only the visitor who started a thread can continue it.
    const parent = await env.DB.prepare(`SELECT id, token_hash, status, parent_id FROM posts WHERE id = ?`).bind(parentId).first();
    if (!parent || parent.parent_id !== null || parent.status !== 'approved') return [{ error: 'Message not found' }, 404];
    if (parent.token_hash !== tokenHash) return [{ error: 'Only the original author can reply here' }, 403];
  }

  const res = await env.DB.prepare(
    `INSERT INTO posts (parent_id, author, nickname, body, status, token_hash, ip_hash) VALUES (?, 'visitor', ?, ?, 'pending', ?, ?)`,
  ).bind(parentId, nickname, body, tokenHash, ipHash).run();
  return [{ id: res.meta.last_row_id, status: 'pending' }, 201, { nickname, body, parentId }];
}

async function admin(request, env, url, method) {
  const path = url.pathname.replace(/^\/api\/admin/, '');

  if (method === 'GET' && path === '/posts') {
    const status = url.searchParams.get('status') || 'pending';
    const where = status === 'all' ? '1=1' : 'status = ?';
    const stmt = env.DB.prepare(
      `SELECT id, parent_id, author, nickname, body, status, created_at FROM posts WHERE ${where} ORDER BY id DESC LIMIT 200`,
    );
    const res = status === 'all' ? await stmt.all() : await stmt.bind(status).all();
    return [{ posts: res.results }, 200];
  }

  let m = path.match(/^\/posts\/(\d+)\/status$/);
  if (method === 'POST' && m) {
    const { status } = await request.json().catch(() => ({}));
    if (!['approved', 'rejected', 'pending'].includes(status)) return [{ error: 'Invalid status' }, 400];
    const res = await env.DB.prepare(`UPDATE posts SET status = ? WHERE id = ?`).bind(status, Number(m[1])).run();
    return res.meta.changes ? [{ ok: true }, 200] : [{ error: 'Not found' }, 404];
  }

  m = path.match(/^\/posts\/(\d+)\/reply$/);
  if (method === 'POST' && m) {
    const input = await request.json().catch(() => ({}));
    const body = clean(input.body);
    if (!body || body.length > MAX_BODY) return [{ error: `Reply must be 1-${MAX_BODY} characters` }, 400];
    const target = await env.DB.prepare(`SELECT id, parent_id FROM posts WHERE id = ?`).bind(Number(m[1])).first();
    if (!target) return [{ error: 'Not found' }, 404];
    const threadId = target.parent_id ?? target.id; // replying to a reply continues the same thread
    // Replying also approves the thread's top message so the conversation is visible.
    await env.DB.prepare(`UPDATE posts SET status = 'approved' WHERE id = ? AND status = 'pending'`).bind(threadId).run();
    const res = await env.DB.prepare(
      `INSERT INTO posts (parent_id, author, nickname, body, status) VALUES (?, 'owner', 'Trevor', ?, 'approved')`,
    ).bind(threadId, body).run();
    return [{ id: res.meta.last_row_id }, 201];
  }

  m = path.match(/^\/posts\/(\d+)$/);
  if (method === 'DELETE' && m) {
    const res = await env.DB.prepare(`DELETE FROM posts WHERE id = ?`).bind(Number(m[1])).run();
    return res.meta.changes ? [{ ok: true }, 200] : [{ error: 'Not found' }, 404];
  }

  return [{ error: 'Not found' }, 404];
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const method = request.method;
    if (method === 'OPTIONS') return new Response(null, { status: 204, headers: corsHeaders(request, env) });
    if (!env.HASH_SALT) return json({ error: 'Server not configured' }, 500, request, env);

    try {
      if (url.pathname.startsWith('/api/admin/')) {
        if (!isOwner(request, env)) return json({ error: 'Unauthorized' }, 401, request, env);
        const [data, status] = await admin(request, env, url, method);
        return json(data, status, request, env);
      }
      if (url.pathname === '/api/posts' && method === 'GET') return json(await listPublic(request, env, url), 200, request, env);
      if (url.pathname === '/api/posts' && method === 'POST') {
        const [data, status, post] = await createPost(request, env);
        if (status === 201) ctx.waitUntil(notifyOwner(env, post));
        return json(data, status, request, env);
      }
      return json({ error: 'Not found' }, 404, request, env);
    } catch (err) {
      console.error(err);
      return json({ error: 'Server error' }, 500, request, env);
    }
  },
};
