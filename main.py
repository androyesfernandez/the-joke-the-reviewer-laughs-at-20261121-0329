#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Writes this entry's one-line joke to /output/entry.txt.

make.fun — "The joke the reviewer laughs at": a one-line joke about
working beside AI coding agents, at most 280 characters.
"""
import os

SETUP = (
    "I gave my agent one rule for the legacy codebase: touch nothing "
    "that works."
)
PUNCHLINE = "Four seconds later it came back: \u201cGreat news \u2014 nothing works.\u201d"

JOKE = SETUP + " " + PUNCHLINE


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
