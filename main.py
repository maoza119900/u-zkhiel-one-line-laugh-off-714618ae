#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one fixed joke line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). Fully deterministic: no clock, no randomness,
no network, no file reads, no dependencies.

The output file holds exactly the joke text with no trailing newline,
so its character count is the joke's character count.
"""

import os

JOKE = (
    "I named my dog Stay, so every walk ends with me shouting "
    "my relationship status at strangers in the park."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
