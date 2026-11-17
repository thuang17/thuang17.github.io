"""Prepare the owner's blank sign sprite for in-town labels."""

from pathlib import Path
import json
import shutil

import numpy as np
from PIL import Image

from normalize import normalize


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'assets/raw/props/像素风木质告示牌.png'
PROCESSED = ROOT / 'assets/processed/props/town_a/sign_blank.png'
NORMALIZED = ROOT / 'assets/normalized/props/town_a/sign_blank.png'
TOWN = ROOT / 'town/a/p_sign_blank.png'


def main() -> None:
    image = np.array(Image.open(SOURCE).convert('RGBA'))
    # The generated PNG has a transparent dark glow around the actual sign.
    # Keep only its nearly opaque pixels before reducing it to town scale.
    image[image[..., 3] < 110, 3] = 0
    image[image[..., 3] == 0, :3] = 0
    cut = Image.fromarray(image, 'RGBA')
    cut = cut.crop(cut.getchannel('A').getbbox())
    PROCESSED.parent.mkdir(parents=True, exist_ok=True)
    NORMALIZED.parent.mkdir(parents=True, exist_ok=True)
    cut.save(PROCESSED)
    palette = json.loads((ROOT / 'tools/palette.json').read_text())
    normalize(PROCESSED, width_tiles=3.5, pal=palette).save(NORMALIZED)
    shutil.copyfile(NORMALIZED, TOWN)
    print(f'{SOURCE.name} -> {TOWN.name}: {Image.open(TOWN).size}')


if __name__ == '__main__':
    main()
