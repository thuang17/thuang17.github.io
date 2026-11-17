"""Export the V2 town page and the assets it really uses to the live site (public/town/).
The source of truth stays docs/v2/town/index.html (it still contains the local-only build mode, which is inert on any other host).
usage: python3 export_town.py <site_root> [base_dir_name=town] [--api URL] [--sitekey KEY] [--home]"""
import os, re, shutil, sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'town')
TITLE = 'Trevor Huang'
DESC = 'Trevor Huang: a pixel-art town you can walk around. Projects, favorites and a guestbook, plus the story of ChamberUp, a member app now live on the Australian App Store.'

def env_value(root, key):
    try:
        for line in open(os.path.join(root, '.env.production'), encoding='utf-8'):
            if line.startswith(key + '='): return line.split('=', 1)[1].strip()
    except OSError: pass
    return ''

def main(root, name='town', api=None, sitekey=None, as_home=False):
    out = os.path.join(root, 'public', name)
    if os.path.isdir(out): shutil.rmtree(out)
    os.makedirs(out)
    html = open(os.path.join(SRC, 'index.html'), encoding='utf-8').read()
    # 1. fonts: Jersey 15 self-hosted instead of Google Fonts
    html = html.replace('<link href="https://fonts.googleapis.com/css2?family=Jersey+15&display=swap" rel="stylesheet">', '')
    face = ("<style>"
            "@font-face{font-family:'Jersey 15';font-style:normal;font-weight:400;font-display:swap;src:url(fonts/jersey-15-latin-ext.woff2) format('woff2');unicode-range:U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C4,U+2113,U+2C60-2C7F,U+A720-A7FF}"
            "@font-face{font-family:'Jersey 15';font-style:normal;font-weight:400;font-display:swap;src:url(fonts/jersey-15-latin.woff2) format('woff2');unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}"
            "</style>")
    # 2. head: title, description, share preview, canonical
    html = html.replace('<title>Town</title>', f'<title>{TITLE}</title><meta name="description" content="{DESC}"><meta property="og:title" content="{TITLE}"><meta property="og:description" content="{DESC}"><meta property="og:type" content="website"><meta property="og:image" content="https://thuang17.github.io/{name}/media/avatar-512.png"><meta name="twitter:card" content="summary">{face}')
    # guestbook backend: public values from .env.production (the same ones the current /guestbook page uses); --api/--sitekey override for local tests
    api = api if api is not None else env_value(root, 'PUBLIC_GUESTBOOK_API'); sitekey = sitekey if sitekey is not None else env_value(root, 'PUBLIC_TURNSTILE_SITEKEY')
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8"><script>window.GB=' + __import__('json').dumps({'api': api, 'sitekey': sitekey}) + '</script>', 1)
    # 3. assets: copy what the page references
    refs = set(re.findall(r"(?:src|href|url)\(?=?['\"]?((?:media|a|ui)/[A-Za-z0-9_./\-]+\.[a-z0-9]+)", html))
    refs |= {'layout.json', 'ui_layout.json', 'mock-notes.json'}
    for f in os.listdir(os.path.join(SRC, 'a')):
        if f.endswith('.png'): refs.add('a/' + f)
    for f in os.listdir(os.path.join(SRC, 'poster-candidates')):
        if f.endswith('.jpg'): refs.add('poster-candidates/' + f)
    refs |= {'stories-vine.svg', 'media/chamberup/poster.jpg'}
    # images chosen by JS (website pages, screenshots) are not in the HTML text: ship the whole folder
    for f in os.listdir(os.path.join(SRC, 'media/chamberup')):
        if f.endswith(('.jpg', '.png', '.mp4')): refs.add('media/chamberup/' + f)
    refs |= {'media/avatar-512.png', 'fonts/jersey-15-latin.woff2', 'fonts/jersey-15-latin-ext.woff2'}
    for r in sorted(refs):
        s = os.path.join(SRC, r)
        if r == 'media/avatar-512.png': s = os.path.join(SRC, '..', 'assets', 'avatar', 'avatar_512.png')
        if r.startswith('fonts/'): s = os.path.join(SRC, '..', 'assets', r)
        if not os.path.isfile(s): print('MISSING', r); continue
        d = os.path.join(out, r); os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copy(s, d)
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8"><link rel="canonical" href="https://thuang17.github.io/">', 1)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(html)
    if as_home:   # the same page as the site homepage; <base> makes every relative asset path resolve to /town/
        open(os.path.join(root, 'public', 'index.html'), 'w', encoding='utf-8').write(html.replace('<meta charset="utf-8">', '<meta charset="utf-8"><base href="/' + name + '/">', 1))
    total = sum(os.path.getsize(os.path.join(dp, f)) for dp, _, fs in os.walk(out) for f in fs)
    print('exported', len(refs) + 1, 'files,', round(total / 1e6, 2), 'MB to', out)

if __name__ == '__main__':
    a = sys.argv[1:]; opt = {}
    for k in ('--api', '--sitekey'):
        if k in a: i = a.index(k); opt[k[2:]] = a[i + 1]; del a[i:i + 2]
    if '--home' in a: a.remove('--home'); opt['as_home'] = True
    main(a[0], a[1] if len(a) > 1 else 'town', **opt)
