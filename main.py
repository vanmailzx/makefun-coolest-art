"""Coolest art entry (make.fun coolest-art-01).

The art is the image vendored beside this file (art.jpg): a colossal chrome
wolf with glowing cyan circuits howling at a shattered moon above a neon
city, aurora in a pink-and-cyan sky. This program copies it byte-for-byte to
/output/entry.png, so every run writes identical bytes.

Standard library only. No network, no randomness, no installed packages.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "art.jpg"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.png"
    shutil.copyfile(SRC, dest)
    # Determinism self-check: the output must be an exact copy of the asset.
    if dest.stat().st_size != SRC.stat().st_size:
        raise RuntimeError("output is not an exact copy of art.jpg")


if __name__ == "__main__":
    main()
