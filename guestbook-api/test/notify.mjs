// Checks the owner-notification email against a local stub of the Resend API.
// Usage (with `wrangler dev` running and .dev.vars pointing RESEND_API_URL at port 8799): node test/notify.mjs
import http from 'node:http';
const BASE = process.argv[2] || 'http://127.0.0.1:8787';
const received = [];
let mode = 'ok';
const stub = http.createServer((req, res) => {
  let body = '';
  req.on('data', (c) => (body += c));
  req.on('end', () => {
    received.push({ auth: req.headers.authorization, body: JSON.parse(body || '{}') });
    res.writeHead(mode === 'ok' ? 200 : 500, { 'Content-Type': 'application/json' });
    res.end('{}');
  });
}).listen(8799);
const token = () => [...crypto.getRandomValues(new Uint8Array(32))].map((b) => b.toString(16).padStart(2, '0')).join('');
const post = (nickname, body) => fetch(BASE + '/api/posts', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ nickname, body, token: token() }) });
const wait = (ms) => new Promise((r) => setTimeout(r, ms));
let failed = 0;
const check = (n, ok) => { console.log((ok ? 'PASS  ' : 'FAIL  ') + n); if (!ok) failed++; };

let r = await post('Sam', 'Hello\nsecond line');
await wait(800);
check('post accepted', r.status === 201);
check('one email sent', received.length === 1);
const mail = received[0]?.body || {};
check('uses the API key as bearer', received[0]?.auth === 'Bearer fake-local-key');
check('sent to the owner', Array.isArray(mail.to) && mail.to[0] === 'owner@example.test');
check('subject names the sender', /Sam/.test(mail.subject || ''));
check('body has the message and admin link', /Hello\nsecond line/.test(mail.text || '') && /guestbook-admin/.test(mail.text || ''));

mode = 'fail';
r = await post('Kim', 'Email provider is down');
await wait(800);
check('post still accepted when the email provider fails', r.status === 201);

stub.close();
console.log(failed ? `\n${failed} check(s) FAILED` : '\nAll checks passed');
process.exit(failed ? 1 : 0);
