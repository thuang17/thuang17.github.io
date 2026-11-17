"""Walk sheet (3 rows x 4 frames) -> hi-res game sheet, NO resampling: the generated pixels are kept 1:1 (only the magenta is removed).
Output walk_hi.png: 4 cols x 4 rows (down, right, left=mirrored right, up) of CELL_W x CELL_H cells, soles on row FEET_ROW, head centred.
usage: python3 make_char_hi.py <walk_sheet.png> <out.png>"""
import sys
import numpy as np
from PIL import Image
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from make_char_frames import load
CELL_W, CELL_H, FEET_ROW = 230, 340, 330

def main(src, out):
    rgba, grid = load(src)
    # one hard alpha, eroded by 1 px so no magenta fringe survives
    if not getattr(load, 'native_alpha', False):      # magenta source: erode 1 px so no magenta fringe survives; a real transparent source is used untouched
        al = rgba[..., 3] > 0; p = np.pad(al, 1); al = al & p[:-2, 1:-1] & p[2:, 1:-1] & p[1:-1, :-2] & p[1:-1, 2:]
        rgba = rgba.copy(); rgba[..., 3] = np.where(al, 255, 0)
    rows = []; stand = []
    for fr in grid:
        hs = [r1 - r0 + 1 for r0, r1, c0, c1 in fr]; sh = min(hs); stand.append(sh)       # the shortest frame = a standing frame; stepping frames reach lower
        cells = []
        for r0, r1, c0, c1 in fr:
            sub = rgba[r0:r1 + 1, c0:c1 + 1]; m = sub[..., 3] > 0
            xs_head = np.where(m[:int(sub.shape[0] * .3)].any(0))[0]; hc = (xs_head.min() + xs_head.max()) // 2
            cell = np.zeros((CELL_H, CELL_W, 4), np.uint8)
            y0 = FEET_ROW - sh; x0 = CELL_W // 2 - hc                  # same head row in every frame of the row: no bobbing
            cell[y0:y0 + sub.shape[0], x0:x0 + sub.shape[1]] = sub
            cells.append(cell)
        rows.append(cells)
    n = len(rows[0])
    mirror = [c[:, ::-1].copy() for c in rows[1]]
    order = [rows[0], rows[1], mirror, rows[2]]
    sheet = np.zeros((4 * CELL_H, n * CELL_W, 4), np.uint8)
    for r, cells in enumerate(order):
        for c in range(n): sheet[r * CELL_H:(r + 1) * CELL_H, c * CELL_W:(c + 1) * CELL_W] = cells[c]
    Image.fromarray(sheet, 'RGBA').save(out); print(sheet.shape, 'frames per row', n, 'standing heights per row', stand, 'mean', round(sum(stand) / 3, 1))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
