"""Local server for the town page. Serves docs/v2/town and lets the build mode
save the layout:  POST /layout.json  ->  docs/v2/town/layout.json

Usage: python3 town_server.py [port]      (default 8180)
Then open http://127.0.0.1:8180/?build   (the ?build part turns the editor on)
"""
import http.server, json, os, sys
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'town')
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store'); super().end_headers()
    def do_POST(self):
        name = self.path.split('?')[0]
        if name not in ('/layout.json', '/ui_layout.json'):
            self.send_error(404); return
        n = int(self.headers.get('Content-Length', 0)); body = self.rfile.read(n)
        try: json.loads(body)
        except Exception: self.send_error(400); return
        fn = name[1:]
        tmp = os.path.join(ROOT, fn + '.tmp'); open(tmp, 'wb').write(body)
        os.replace(tmp, os.path.join(ROOT, fn))
        self.send_response(200); self.end_headers(); self.wfile.write(b'ok')
    def log_message(self, *a): pass
if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8180
    http.server.ThreadingHTTPServer(('127.0.0.1', port), H).serve_forever()
