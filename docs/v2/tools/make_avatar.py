"""Head portrait (generated transparent PNG) -> avatar sizes.
The generated blocks are not on a regular pixel grid (tried: rebuilding the grid breaks eyes and chin), so the picture is only scaled, never rebuilt:
alpha-aware Lanczos, then a hard alpha (>=128). The head is centred on its visual centre and scaled so that its farthest point lies at FILL * (size/2) from the
centre, which makes every size safe to crop to a circle.
usage: python3 make_avatar.py <head.png> <out_dir> [fill=0.92]"""
import sys, os
import numpy as np
from PIL import Image

def prep(src):
    a = np.array(Image.open(src).convert('RGBA')); a[..., 3] = np.where(a[..., 3] >= 128, 255, 0); a[a[..., 3] == 0, :3] = 0
    ys, xs = np.where(a[..., 3] > 0); cx = (xs.min() + xs.max() + 1) / 2; cy = (ys.min() + ys.max() + 1) / 2
    r = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2).max()
    return a, cx, cy, r

def make(a, cx, cy, r, size, fill):
    s = fill * size / 2 / r                                              # scale factor
    H, W = a.shape[:2]; big = Image.fromarray(a, 'RGBA')
    pm = np.array(big).astype(np.float32); pm[..., :3] *= pm[..., 3:4] / 255
    pw, ph = round(W * s), round(H * s)
    ch = [np.array(Image.fromarray(pm[..., k]).resize((pw, ph), Image.LANCZOS)) for k in range(4)]
    out = np.stack(ch, -1); al = out[..., 3]
    rgb = np.where(al[..., None] > 0, out[..., :3] * 255 / np.maximum(al[..., None], 1), 0).clip(0, 255)
    res = np.dstack([rgb, np.where(al >= 128, 255, 0)]).astype(np.uint8)
    canvas = np.zeros((size, size, 4), np.uint8); ox = int(round(size / 2 - cx * s)); oy = int(round(size / 2 - cy * s))
    sx0, sy0 = max(0, -ox), max(0, -oy); dx0, dy0 = max(0, ox), max(0, oy)
    w = min(pw - sx0, size - dx0); h = min(ph - sy0, size - dy0)
    canvas[dy0:dy0 + h, dx0:dx0 + w] = res[sy0:sy0 + h, sx0:sx0 + w]
    return Image.fromarray(canvas, 'RGBA')

if __name__ == '__main__':
    src, out = sys.argv[1], sys.argv[2]; fill = float(sys.argv[3]) if len(sys.argv) > 3 else .92; os.makedirs(out, exist_ok=True)
    a, cx, cy, r = prep(src); print('centre', cx, cy, 'farthest point from centre', round(r))
    for size in (1024, 512, 256, 180):
        make(a, cx, cy, r, size, fill).save(os.path.join(out, f'avatar_{size}.png'))
