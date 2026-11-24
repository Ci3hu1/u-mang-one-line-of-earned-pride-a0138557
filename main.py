#!/usr/bin/env python3
"""u-mang-one-line-of-earned-pride-a0138557 entry.

Writes one fixed line -- a quiet, earned moment of pride -- to
/output/entry.txt. Python 3.13, standard library only. Deterministic:
the output bytes are exactly the line below plus a trailing newline,
on every run. No network, no randomness.
"""

import os
from pathlib import Path

LINE = "His hands still shook from the chemo, but he steadied the chisel and carved his granddaughter's name straight into the oak."


def main() -> None:
    # Gate: UTF-8 text of 1-240 characters, not only whitespace.
    if not 1 <= len(LINE) <= 240:
        raise SystemExit(f"line is {len(LINE)} characters, outside the 1-240 gate")
    if not LINE.strip():
        raise SystemExit("line is only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / "entry.txt"
    dest.write_text(LINE + "\n", encoding="utf-8")
    # The grader collects outputs as another user: force world-readable.
    os.chmod(dest, 0o644)
    # Read back and verify the exact bytes the judge will see.
    if dest.read_bytes() != (LINE + "\n").encode("utf-8"):
        raise SystemExit(f"verify failed: {dest} does not match the line bytes")
    print(f"wrote {dest} ({dest.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
