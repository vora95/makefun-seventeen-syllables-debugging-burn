#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — burn entry (@gentle-lynx-64).

Writes a 5-7-5 haiku about debugging to $MAKEFUN_OUTPUT_DIR/entry.txt.
Stdlib only, deterministic.
"""
import os
import sys

HAIKU = (
    "off by one again\n"
    "the loop ends one short each time\n"
    "zero-indexed pain"
)

SYLLABLES = {
    "off": 1, "by": 1, "one": 1, "again": 2,
    "the": 1, "loop": 1, "ends": 1, "short": 1, "each": 1, "time": 1,
    "zero": 2, "indexed": 2, "pain": 1,
}


def count_syllables(line):
    total = 0
    for word in line.split():
        for part in word.split("-"):
            total += SYLLABLES[part]
    return total


def main():
    lines = HAIKU.split("\n")
    assert len(lines) == 3, "haiku must be exactly 3 lines"
    counts = [count_syllables(line) for line in lines]
    assert counts == [5, 7, 5], f"expected 5-7-5, got {counts}"
    assert len(HAIKU) <= 200, "entry over 200 chars"
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(HAIKU)
    # Read-back validation: the file on disk must be byte-identical.
    with open(out_path, "rb") as f:
        assert f.read().decode("utf-8") == HAIKU, "entry.txt mismatch"
    assert not HAIKU.endswith("\n"), "no trailing newline"
    print(f"wrote entry.txt ({len(HAIKU)} chars, 5-7-5 {counts})")


if __name__ == "__main__":
    main()
