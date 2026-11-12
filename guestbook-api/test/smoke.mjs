// End-to-end smoke test against a running `wrangler dev` instance.
// Usage: ADMIN_TOKEN=... node test/smoke.mjs [baseUrl]
const BASE = process.argv[2] || 'http://127.0.0.1:8787';
const ADMIN = process.env.ADMIN_TOKEN;
if (!ADMIN) { console.error('Set ADMIN_TOKEN'); process.exit(2); }

let failed = 0;
const check = (name, ok, extra = '') => {
  console.log(`${ok ? 'PASS' : 'FAIL'}  ${name}${ok ? '' : '  ' + extra}`);
  if (!ok) failed++;
};
const call = async (method, path, { body, token, admin } = {}) => {
  const headers = { 'Content-Type': 'application/json' };
  if (token) headers['X-Visitor-Token'] = token;
  if (admin) headers.Authorization = `Bearer ${admin}`;
  const res = await fetch(BASE + path, { method, headers, body: body ? JSON.stringify(body) : undefined });
  return { status: res.status, data: await res.json().catch(() => ({})) };
};
const randomToken = () => [...crypto.getRandomValues(new Uint8Array(32))].map((b) => b.toString(16).padStart(2, '0')).join('');

const tokenA = randomToken();
const tokenB = randomToken();
const marker = `smoke-${Date.now()}`;

// 1. Validation
check('empty body rejected', (await call('POST', '/api/posts', { body: { nickname: 'A', body: '', token: tokenA } })).status === 400);
check('long nickname rejected', (await call('POST', '/api/posts', { body: { nickname: 'x'.repeat(31), body: 'hi', token: tokenA } })).status === 400);
check('missing token rejected', (await call('POST', '/api/posts', { body: { nickname: 'A', body: 'hi' } })).status === 400);

// 2. Visitor posts, message stays hidden from the public until approved
const created = await call('POST', '/api/posts', { body: { nickname: 'Visitor A', body: marker, token: tokenA } });
check('post created as pending', created.status === 201 && created.data.status === 'pending', JSON.stringify(created));
const id = created.data.id;
const publicBefore = await call('GET', '/api/posts');
check('hidden from public before approval', !publicBefore.data.posts.some((p) => p.id === id));
const own = await call('GET', '/api/posts', { token: tokenA });
check('visible to its author as pending', own.data.posts.some((p) => p.id === id && p.pending && p.mine));
const other = await call('GET', '/api/posts', { token: tokenB });
check('hidden from another visitor', !other.data.posts.some((p) => p.id === id));

// 3. Admin endpoints need the token
check('admin without token -> 401', (await call('GET', '/api/admin/posts')).status === 401);
check('admin with wrong token -> 401', (await call('GET', '/api/admin/posts', { admin: 'nope' })).status === 401);
const pending = await call('GET', '/api/admin/posts?status=pending', { admin: ADMIN });
check('admin sees pending message', pending.status === 200 && pending.data.posts.some((p) => p.id === id));

// 4. Approve -> public
check('approve ok', (await call('POST', `/api/admin/posts/${id}/status`, { admin: ADMIN, body: { status: 'approved' } })).status === 200);
const publicAfter = await call('GET', '/api/posts');
check('public after approval', publicAfter.data.posts.some((p) => p.id === id && p.body === marker));

// 5. Owner replies, thread shows the reply
const reply = await call('POST', `/api/admin/posts/${id}/reply`, { admin: ADMIN, body: { body: 'Thanks for stopping by' } });
check('owner reply created', reply.status === 201, JSON.stringify(reply));
const thread = (await call('GET', '/api/posts')).data.posts.find((p) => p.id === id);
check('reply visible in thread', thread && thread.replies.some((r) => r.author === 'owner' && r.nickname === 'Trevor'));

// 6. Only the original visitor can continue the thread, and it needs approval again
check('other visitor cannot reply', (await call('POST', '/api/posts', { body: { nickname: 'B', body: 'hijack', token: tokenB, parent_id: id } })).status === 403);
const follow = await call('POST', '/api/posts', { body: { nickname: 'Visitor A', body: 'Nice site', token: tokenA, parent_id: id } });
check('original visitor can reply (pending)', follow.status === 201);
const threadPublic = (await call('GET', '/api/posts')).data.posts.find((p) => p.id === id);
check('visitor reply hidden until approved', !threadPublic.replies.some((r) => r.id === follow.data.id));
const threadOwn = (await call('GET', '/api/posts', { token: tokenA })).data.posts.find((p) => p.id === id);
check('visitor sees own pending reply', threadOwn.replies.some((r) => r.id === follow.data.id && r.pending));

// 7. HTML is stored as plain text (the page must render it as text)
const xss = await call('POST', '/api/posts', { body: { nickname: '<b>x</b>', body: '<script>alert(1)</script>', token: tokenB } });
check('html accepted as plain text', xss.status === 201);

// 7b. Visitors manage their own messages: edit while pending, delete any time, never anyone else's
const tokenC = randomToken();
const mine = await call('POST', '/api/posts', { body: { nickname: 'Visitor C', body: 'first draft', token: tokenC } });
const mid = mine.data.id;
check('author can edit pending message', (await call('PATCH', `/api/posts/${mid}`, { token: tokenC, body: { body: 'second draft' } })).status === 200);
check('edit applied and still pending', (await call('GET', '/api/posts', { token: tokenC })).data.posts.some((p) => p.id === mid && p.body === 'second draft' && p.pending));
check('other visitor cannot edit', (await call('PATCH', `/api/posts/${mid}`, { token: tokenB, body: { body: 'hijack' } })).status === 404);
check('edit without token rejected', (await call('PATCH', `/api/posts/${mid}`, { body: { body: 'x' } })).status === 400);
check('empty edit rejected', (await call('PATCH', `/api/posts/${mid}`, { token: tokenC, body: { body: '  ' } })).status === 400);
check('approved message cannot be edited', (await call('PATCH', `/api/posts/${id}`, { token: tokenA, body: { body: 'rewrite' } })).status === 403);
check('other visitor cannot delete', (await call('DELETE', `/api/posts/${mid}`, { token: tokenB })).status === 404);
check('author can delete pending message', (await call('DELETE', `/api/posts/${mid}`, { token: tokenC })).status === 200);
check('deleted message is gone', !(await call('GET', '/api/posts', { token: tokenC })).data.posts.some((p) => p.id === mid));
check('owner reply cannot be deleted by a visitor', (await call('DELETE', `/api/posts/${reply.data.id}`, { token: tokenA })).status === 404);
const tokenD = randomToken();
const appr = await call('POST', '/api/posts', { body: { nickname: 'Visitor D', body: 'to be approved', token: tokenD } });
await call('POST', `/api/admin/posts/${appr.data.id}/status`, { admin: ADMIN, body: { status: 'approved' } });
check('author can delete approved message', (await call('DELETE', `/api/posts/${appr.data.id}`, { token: tokenD })).status === 200);

// 8. Reject + delete
check('reject ok', (await call('POST', `/api/admin/posts/${xss.data.id}/status`, { admin: ADMIN, body: { status: 'rejected' } })).status === 200);
check('delete ok', (await call('DELETE', `/api/admin/posts/${id}`, { admin: ADMIN })).status === 200);
check('delete cascades to replies', !(await call('GET', '/api/admin/posts?status=all', { admin: ADMIN })).data.posts.some((p) => p.parent_id === id));

// 9. Rate limit (5 per hour per IP): the posts above already count; keep posting until blocked
let blocked = false;
for (let i = 0; i < 8 && !blocked; i++) {
  const r = await call('POST', '/api/posts', { body: { nickname: 'Spam', body: `spam ${i}`, token: tokenB } });
  if (r.status === 429) blocked = true;
}
check('rate limit kicks in', blocked);

console.log(failed ? `\n${failed} check(s) FAILED` : '\nAll checks passed');
process.exit(failed ? 1 : 0);
