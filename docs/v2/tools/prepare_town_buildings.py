"""Cut out and normalize the four chosen town buildings without changing their designs."""

from pathlib import Path
import json
import shutil

import numpy as np
from PIL import Image

from normalize import normalize


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'assets/raw/buildings'
PROCESSED = ROOT / 'assets/processed/buildings'
NORMALIZED = ROOT / 'assets/normalized/buildings'
TOWN = ROOT / 'town/a'

# Widths are in town tiles. Keep each building's role and silhouette distinct.
BUILDINGS = [
    ('温馨像素艺术工坊小屋.png', 'stories_cut.png', 'b_tower.png', 7.5),
    ('温暖核桃木双层图书馆.png', 'markethall_cut.png', 'b_market.png', 7.0),
    ('栗棕屋顶的温馨像素小屋.png', 'aboutme_cut.png', 'b_cabin.png', 5.5),
    ('像素风木结构施工建筑.png', 'mill_construction_cut.png', 'b_mill.png', 6.5),
]


def cutout(src: Path) -> Image.Image:
    pixels = np.array(Image.open(src).convert('RGBA'))
    rgb = pixels[..., :3].astype(np.int16)
    if np.all(pixels[..., 3] == 255):
        # The workshop has a white backdrop; the construction image has a
        # printed white/grey checkerboard, including between its roof beams.
        # Those pixels are neutral and bright, unlike the warm stone or fabric.
        neutral_backdrop = (rgb.min(axis=2) > 220) & (np.ptp(rgb, axis=2) < 16)
        pixels[neutral_backdrop, 3] = 0
    pixels[pixels[..., 3] < 110, 3] = 0
    pixels[pixels[..., 3] == 0, :3] = 0
    image = Image.fromarray(pixels, 'RGBA')
    return image.crop(image.getchannel('A').getbbox())


def main() -> None:
    palette = json.loads((ROOT / 'tools/palette.json').read_text())
    for source, intermediate, target, width in BUILDINGS:
        cut = cutout(RAW / source)
        cut.save(PROCESSED / intermediate)
        normalized = normalize(PROCESSED / intermediate, width_tiles=width, pal=palette)
        normalized.save(NORMALIZED / intermediate)
        shutil.copyfile(NORMALIZED / intermediate, TOWN / target)
        print(f'{source} -> {target}: {normalized.width}x{normalized.height}')


if __name__ == '__main__':
    main()
