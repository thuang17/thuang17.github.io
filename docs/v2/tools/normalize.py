"""Art-standard normaliser for the V2 town assets.

Every sprite goes through the same steps so that all assets share one pixel
size, one palette and one outline:
  1. scale the cut-out to its target size in ART pixels (1 tile = 32 art px)
     with an area (box) filter, so detail is averaged, not dropped
  2. make alpha binary (no half-transparent edges)
  3. snap every colour to the master palette (no dithering)
  4. redraw the outermost ring of opaque pixels in the outline colour
The game then draws art pixels at an integer scale (2x: 1 tile = 64 screen px).

Usage:
  python3 normalize.py palette   # build master palette from the anchor assets
  python3 normalize.py run       # normalise every asset listed in sizes.json
"""
import json, sys, os
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')
PROC = os.path.join(ASSETS, 'processed')
OUT = os.path.join(ASSETS, 'normalized')
TILE = 32                      # art pixels per tile
OUTLINE = (0x4B, 0x30, 0x25)   # warm dark brown
PALETTE_FILE = os.path.join(HERE, 'palette.json')
SIZES_FILE = os.path.join(HERE, 'sizes.json')

# Anchor assets the site owner accepted; the palette is learnt from these.
ANCHORS = ['buildings/glasshouse_cut.png', 'buildings/aboutme_cut.png',
           'buildings/stories_cut.png', 'buildings/markethall_cut.png',
           'ground/grass1.png', 'ground/grass2.png', 'ground/shore/sand1.png',
           'ground/shore/water1.png', 'nature/trees_stages/oak_summer.png',
           'nature/trees_species/birch.png', 'nature/trees_evergreen_blossom/spruce.png',
           'nature/trees_evergreen_blossom/blossom_lavender.png', 'nature/trees_evergreen_blossom/blossom_white.png',
           'ground/variation_fixed/flowers_mixed.png', 'nature/water_plants/water_iris.png',
           'props/town_a/well.png', 'props/town_a/lamp_street.png']
# Exact ground colours are always kept, so large flat areas never shift hue.
FIXED = ['ground/grass1.png', 'ground/grass2.png', 'ground/grass3.png',
         'ground/shore/sand1.png', 'ground/shore/water1.png', 'ground/bank_recolored/sand1.png']


def opaque_pixels(path):
    a = np.array(Image.open(os.path.join(PROC, path)).convert('RGBA'))
    return a[a[..., 3] > 128][:, :3]


ACCENTS = [
    ('lavender', lambda r, g, b: (b > g + 20) & (r > g + 10) & (b >= r - 5) & (g > 60)),
    ('glow', lambda r, g, b: (r > 230) & (g > 190) & (b < 140)),
    ('teal', lambda r, g, b: (g > r + 25) & (b > r + 15)),
]


def dominant(path, k=3):
    a = opaque_pixels(path)
    vals, cnt = np.unique(a, axis=0, return_counts=True)
    return [tuple(int(c) for c in v) for v in vals[np.argsort(-cnt)[:k]]]


def build_palette(n=48):
    fixed = []
    for p in FIXED:
        for c in dominant(p):
            if c not in fixed:
                fixed.append(c)
    # Small accent hues (lavender flowers, teal, warm window glow) get their
    # own reserved colours, otherwise median-cut merges them into neighbours.
    for name, test in ACCENTS:
        a = np.concatenate([opaque_pixels(p) for p in ANCHORS]).astype(int)
        sel = a[test(a[:, 0], a[:, 1], a[:, 2])]
        if len(sel) > 50:
            img = Image.fromarray(sel.reshape(-1, 1, 3).astype('uint8'))
            q = img.quantize(colors=3, method=Image.Quantize.MEDIANCUT)
            for c in np.array(q.getpalette()[:9]).reshape(-1, 3).tolist():
                if tuple(c) not in fixed:
                    fixed.append(tuple(c))
    px = np.concatenate([opaque_pixels(p) for p in ANCHORS])
    rng = np.random.default_rng(1)
    px = px[rng.choice(len(px), min(len(px), 400_000), replace=False)]
    img = Image.fromarray(px.reshape(-1, 1, 3).astype('uint8'))
    m = n - 1 - len(fixed)
    q = img.quantize(colors=m, method=Image.Quantize.MEDIANCUT)
    pal = np.array(q.getpalette()[:3 * m]).reshape(-1, 3).tolist()
    pal += [list(c) for c in fixed] + [list(OUTLINE)]
    json.dump(pal, open(PALETTE_FILE, 'w'))
    return pal


def snap(rgb, pal):
    p = np.array(pal, dtype=np.int32)
    flat = rgb.reshape(-1, 3).astype(np.int32)
    # weighted RGB distance (cheap perceptual approximation)
    w = np.array([2, 4, 3])
    d = (((flat[:, None, :] - p[None, :, :]) ** 2) * w).sum(-1)
    return p[d.argmin(1)].reshape(rgb.shape).astype('uint8')


def normalize(src, width_tiles=None, height_tiles=None, pal=None, outline=True):
    im = Image.open(src).convert('RGBA')
    bb = im.getbbox()
    im = im.crop(bb)
    w, h = im.size
    if width_tiles:
        tw = max(1, round(width_tiles * TILE)); th = max(1, round(h * tw / w))
    else:
        th = max(1, round(height_tiles * TILE)); tw = max(1, round(w * th / h))
    # premultiply so transparent pixels do not bleed colour into the edge
    a = np.array(im).astype(np.float32)
    a[..., :3] *= a[..., 3:4] / 255
    pm = Image.fromarray(a.astype('uint8'), 'RGBA').resize((tw, th), Image.BOX)
    b = np.array(pm).astype(np.float32)
    alpha = b[..., 3]
    rgb = np.where(alpha[..., None] > 0, b[..., :3] * 255 / np.maximum(alpha[..., None], 1), 0)
    mask = alpha > 110
    rgb = snap(np.clip(rgb, 0, 255), pal)
    if outline:
        m = np.pad(mask, 1)
        edge = mask & ~(m[:-2, 1:-1] & m[2:, 1:-1] & m[1:-1, :-2] & m[1:-1, 2:])
        rgb[edge] = OUTLINE
    out = np.dstack([rgb, np.where(mask, 255, 0).astype('uint8')])
    return Image.fromarray(out, 'RGBA')


def normalize_sheet(src, scale, pal):
    # Whole sprite sheet at one fixed scale (no cropping), so frames stay aligned.
    im = Image.open(src).convert('RGBA')
    tw, th = round(im.size[0] * scale), round(im.size[1] * scale)
    a = np.array(im).astype(np.float32); a[..., :3] *= a[..., 3:4] / 255
    b = np.array(Image.fromarray(a.astype('uint8'), 'RGBA').resize((tw, th), Image.BOX)).astype(np.float32)
    al = b[..., 3]
    rgb = np.where(al[..., None] > 0, b[..., :3] * 255 / np.maximum(al[..., None], 1), 0)
    mask = al > 110
    rgb = snap(np.clip(rgb, 0, 255), pal)
    m = np.pad(mask, 1)
    edge = mask & ~(m[:-2, 1:-1] & m[2:, 1:-1] & m[1:-1, :-2] & m[1:-1, 2:])
    rgb[edge] = OUTLINE
    return Image.fromarray(np.dstack([rgb, np.where(mask, 255, 0).astype('uint8')]), 'RGBA')


def normalize_tile(src, pal):
    im = Image.open(src).convert('RGB').resize((TILE, TILE), Image.BOX)
    return Image.fromarray(snap(np.array(im), pal), 'RGB')


def run():
    pal = json.load(open(PALETTE_FILE))
    sizes = json.load(open(SIZES_FILE))
    for rel, spec in sizes.items():
        if rel.startswith('_'):
            continue
        src = os.path.join(PROC, rel)
        dst = os.path.join(OUT, rel)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if spec.get('sheet_scale'):
            normalize_sheet(src, spec['sheet_scale'], pal).save(dst)
        elif spec.get('tile'):
            normalize_tile(src, pal).save(dst)
        else:
            normalize(src, spec.get('w'), spec.get('h'), pal, spec.get('outline', True)).save(dst)
    print('normalised', sum(1 for k in sizes if not k.startswith('_')), 'assets ->', OUT)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'run'
    if cmd == 'palette':
        print(len(build_palette()), 'colours ->', PALETTE_FILE)
    else:
        run()
