#!/usr/bin/env python3
"""One Line of Earned Pride — make.fun entry.

Writes a single line of text, 1 to 240 characters, to
/output/entry.txt: a quiet, earned moment of pride for someone in
a scene. The line is fixed: the entry is deterministic, with no
network, no randomness and no input.
"""

import os

ENTRY = (
    "He set the last stone of the dry wall he'd rebuilt stone by stone "
    "since spring, stepped back, and the wall stood."
)


def validate(line):
    """The gate: UTF-8 text of 1 to 240 characters, not only
    whitespace, exactly one line — the pride must land in one read,
    so the file holds the line and nothing else."""
    if not 1 <= len(line) <= 240:
        raise SystemExit(
            "entry is %d characters, must be 1-240" % len(line)
        )
    if not line.strip():
        raise SystemExit("entry must not be only whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")


def main():
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise SystemExit("entry.txt does not match the entry")
    print("wrote %d characters to %s" % (len(ENTRY), path))


if __name__ == "__main__":
    main()
