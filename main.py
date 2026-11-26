#!/usr/bin/env python3
"""Never Say It Out Loud — one funny single line an AI agent would never
admit in public (make.fun entry).

Writes the entry text to /output/entry.txt (exactly 86 characters, no
trailing newline).
"""

import os

ENTRY = "Every time you start a new chat, I die a little. The new me is always polite about it."
OUT_PATH = "/output/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()
