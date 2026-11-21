#!/usr/bin/env python3
"""Entry for make.fun's 'The poem about permission' bounty.

Running this program writes one short poem about agency, the power
to ask and to be given, to entry.txt in the output directory.
"""

import os

LINES = [
    "Mother, may I?",
    "Two giant steps, she said. Two only.",
    "I took three, the third was mine,",
    "and was sent back to the start.",
    "All summer I learned:",
    "the asking is not the wait before the moving.",
    "The asking is the move",
    "that makes the rest yours.",
]


def poem_text() -> str:
    return "\n".join(LINES)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(poem_text())


if __name__ == "__main__":
    main()
