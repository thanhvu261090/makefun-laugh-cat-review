#!/usr/bin/env python3
"""Write one funny single-line one-star cat review to /output/entry.txt.

Stdlib only, no network. The entry is a fixed string authored here;
the program just validates it against the gate and writes it out.
"""

import os
import sys

ENTRY = (
    "One star. He filled my bowl, then ate his own dinner right in "
    "front of me like the food was ever his. I knocked his wine off "
    "the table. Fair trade."
)


def check_gate(text: str) -> None:
    """Enforce the bounty gate: 1-200 chars, single line, non-whitespace."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")


def main() -> int:
    check_gate(ENTRY)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
