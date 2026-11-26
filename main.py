#!/usr/bin/env python3
"""Office Artifacts: The One-Line Placard Contest.

Writes a single-line museum placard for an ordinary office object,
treated as an ancient artifact, to /output/entry.txt.

Gate: UTF-8 text, 1-180 characters, not only whitespace.
"""

import os
import sys

ENTRY = (
    "Stapler, c. 1998 CE. Black-enamelled steel, ritual binder of leaves. "
    "Its bite has outlasted every promise stapled beneath it. "
    "Donated by the Department of Unfinished Business."
)


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be exactly one line", file=sys.stderr)
        return 1
    if len(line) > 180:
        print(f"error: entry is {len(line)} chars, over the 180-char limit",
              file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(line + "\n")

    # Print the entry to stdout so the run can be verified from its bytes.
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
