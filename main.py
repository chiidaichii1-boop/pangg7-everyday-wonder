"""Everyday Wonder — make.fun entry.

Writes one sentence about a small moment of wonder in everyday life
to /output/entry.txt.
"""

import os

ENTRY = (
    "This morning the elevator stopped on a floor nobody pressed, and "
    "a dog I have never met stepped in, sat down, and rode down with "
    "me like it had been waiting for this exact ride all along."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
