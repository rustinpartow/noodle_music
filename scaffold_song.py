#!/usr/bin/env python3
"""Scaffold a new song folder from the `example_song` template.

Usage:
    python3 scaffold_song.py "cool_new_song"

It will:
1. Copy `example_song/` → `cool_new_song/`.
2. Replace every occurrence of the string "example_song" inside **text** files with the new slug.
3. Print the next steps (edit song-prompt.md etc.).

Dependencies: standard library only.
"""

import sys
import shutil
import os
from pathlib import Path

TEMPLATE_DIR = Path(__file__).parent / "example_song"

TEXT_EXT = {".md", ".py", ".ly", "", ".Makefile", "Makefile"}


def copytree(src: Path, dst: Path):
    if dst.exists():
        print(f"Error: target directory {dst} already exists.")
        sys.exit(1)
    shutil.copytree(src, dst)


def replace_tokens(dst: Path, old: str, new: str):
    for path in dst.rglob("*"):
        if path.is_file():
            if path.suffix in TEXT_EXT or path.name == "Makefile":
                try:
                    text = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue  # binary file
                if old in text:
                    path.write_text(text.replace(old, new), encoding="utf-8")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 scaffold_song.py <new_song_slug>")
        sys.exit(1)
    song_slug = sys.argv[1].strip()
    if not song_slug:
        print("Song slug cannot be empty")
        sys.exit(1)
    target_dir = Path(song_slug)

    copytree(TEMPLATE_DIR, target_dir)
    replace_tokens(target_dir, "example_song", song_slug)

    print(f"✅ Created {target_dir}/ from template.")
    print("Next steps:")
    print(f"  cd {song_slug}")
    print("  make demo   # or edit chart_v3.ly first then make")


if __name__ == "__main__":
    main() 