"""Walk sheet (3 rows x 4 frames: front, right, back) -> game sprite sheets.
idle.png : 2 cols x 4 rows of 60 px cells (rows: down, right, left, up). Both columns = the standing frame.
trav.png : 4 cols x 4 rows of 60 px cells, frames = stand, step, stand, step. Left row = mirrored right row.
Each frame is scaled with ONE factor (height of the tallest frame -> TARGET_H px), aligned on the head (same hair-top row, same head centre),
snapped to one shared palette and given the shared 1 px outline.
usage: python3 make_char_frames.py <walk_sheet.png> <out_dir> [target_h=48]"""
import sys, os
import numpy as np
from PIL import Image
OUTLINE = (0x4B, 0x30, 0x25); CELL = 60; FEET = 56; NCOL = 56   # FEET: row of the soles inside a cell

def runs(v, thr, minw=40):
    r, s = [], None
    for i, x in enumerate(list(v > thr) + [False]):
        if x and s is None: s = i
        if not x and s is not None:
            if i - s > minw: r.append((s, i - 1))
            s = None
    return r

def load(path):
    raw = Image.open(path)
    if raw.mode == 'RGBA' and (np.array(raw)[..., 3] < 255).any():                      # real transparency from the generator: use it as is (hard threshold, no erosion)
        arr = np.array(raw); rgba = arr.copy(); rgba[..., 3] = np.where(arr[..., 3] >= 128, 255, 0)
        rgba[rgba[..., 3] == 0, :3] = 0
        bgm = rgba[..., 3] == 0; rows = runs((~bgm).mean(1), 0.01); frames = []
        for r0, r1 in rows:
            cols = runs((~bgm[r0:r1 + 1]).mean(0), 0.01); assert len(cols) in (4, 6), (r0, cols)
            frames.append([(r0, r1, c0, c1) for c0, c1 in cols])
        load.native_alpha = True
        return rgba, frames
    load.native_alpha = False
    im = raw.convert('RGB'); a = np.array(im).astype(int)
    bg = ((a[..., 0] > 200) & (a[..., 2] > 180) & (a[..., 1] < 120)) | ((a[..., 0] - a[..., 1] > 70) & (a[..., 2] - a[..., 1] > 70))   # magenta and its blends
    rgba = np.dstack([a.astype('uint8'), np.where(bg, 0, 255).astype('uint8')])
    rows = runs((~bg).mean(1), 0.01); frames = []
    for r0, r1 in rows:
        cols = runs((~bg[r0:r1 + 1]).mean(0), 0.01); assert len(cols) in (4, 6), (r0, cols)
        frames.append([(r0, r1, c0, c1) for c0, c1 in cols])
    return rgba, frames

def frame_img(rgba, r0, r1, c0, c1, H):
    sub = np.zeros((H, c1 - c0 + 1, 4), np.uint8); part = rgba[r0:r1 + 1, c0:c1 + 1]; sub[:part.shape[0]] = part; al = sub[..., 3] > 0
    top = al[:int(H * .3)]; xs = np.where(top.any(0))[0]; hc = (xs.min() + xs.max()) / 2     # head centre
    return sub, hc

def main(src, out, TH=48):
    rgba, grid = load(src)
    H = max(r1 - r0 + 1 for fr in grid for r0, r1, c0, c1 in fr); s = TH / H; Wc = 200
    px = np.concatenate([rgba[..., :3][rgba[..., 3] > 0]])
    q = Image.fromarray(px.reshape(1, -1, 3).astype('uint8')).quantize(NCOL, method=Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE)
    pal = np.array(q.getpalette()[:NCOL * 3]).reshape(-1, 3)
    snap_idx = lambda rgb: ((rgb[:, :, None, :].astype(int) - pal[None, None, :, :]) ** 2).sum(-1).argmin(-1)
    sheets = {}
    for ri, fr in enumerate(grid):
        cells = []
        for r0, r1, c0, c1 in fr:
            sub, hc = frame_img(rgba, r0, r1, c0, c1, H)
            canvas = np.zeros((H, Wc, 4), np.uint8); off = int(round(Wc / 2 - hc))
            xs0 = max(0, off); xs1 = min(Wc, off + sub.shape[1])
            canvas[:, xs0:xs1] = sub[:, xs0 - off:xs1 - off]
            w = round(Wc * s); h = round(H * s)
            idx = snap_idx(canvas[..., :3]); opq = canvas[..., 3] > 0
            ys_ = np.linspace(0, H, h + 1).astype(int); xs_ = np.linspace(0, Wc, w + 1).astype(int)
            rgb = np.zeros((h, w, 3), np.uint8); m = np.zeros((h, w), bool)
            for j in range(h):
                for i in range(w):
                    o = opq[ys_[j]:ys_[j + 1], xs_[i]:xs_[i + 1]]
                    if o.mean() < .5: continue
                    ix = idx[ys_[j]:ys_[j + 1], xs_[i]:xs_[i + 1]][o]
                    rgb[j, i] = pal[np.bincount(ix, minlength=len(pal)).argmax()]; m[j, i] = True      # dominant colour, not an average: no blur
            p = np.pad(m, 1); edge = m & ~(p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:]); rgb[edge] = OUTLINE
            spr = np.dstack([rgb, np.where(m, 255, 0).astype('uint8')])
            cell = np.zeros((CELL, CELL, 4), np.uint8)
            ys, xs = np.where(spr[..., 3] > 0)
            y0 = FEET - h; x0 = CELL // 2 - w // 2
            cell[y0:y0 + h, x0:x0 + w] = spr[:min(h, CELL - y0)]
            cells.append(cell)
        sheets[ri] = cells
    mirror = [c[:, ::-1].copy() for c in sheets[1]]
    order = [sheets[0], sheets[1], mirror, sheets[2]]        # down, right, left, up
    os.makedirs(out, exist_ok=True)
    trav = np.zeros((4 * CELL, 4 * CELL, 4), np.uint8); idle = np.zeros((4 * CELL, 2 * CELL, 4), np.uint8)
    for r, cells in enumerate(order):
        for c in range(4): trav[r * CELL:(r + 1) * CELL, c * CELL:(c + 1) * CELL] = cells[c]
        for c in range(2): idle[r * CELL:(r + 1) * CELL, c * CELL:(c + 1) * CELL] = cells[0]
    Image.fromarray(trav, 'RGBA').save(os.path.join(out, 'trav.png')); Image.fromarray(idle, 'RGBA').save(os.path.join(out, 'idle.png'))
    print('scale', round(s, 4), 'sprite', w, 'x', h, 'cells', CELL)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 48)
