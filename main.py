#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line — one deadpan line about the
pointless meeting, written to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line is a single sentence, under 200 characters, and the program is
fully deterministic: repeated runs produce byte-identical output.
"""

import os

ENTRY = (
    "This one-hour meeting cost more than the decision it was supposed "
    "to make \u2014 and the decision still hasn't been made."
)


def build_entry() -> str:
    """Assemble the line from its two beats: the cost, then the punch."""
    return ENTRY.strip()


def main() -> None:
    line = build_entry()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry is {len(line)} chars, must be 1-200"
    assert line.strip() == line and line, "entry must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = "output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")


if __name__ == "__main__":
    main()
