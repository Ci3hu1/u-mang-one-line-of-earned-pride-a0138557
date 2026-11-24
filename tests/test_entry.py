"""Tests for the One Line of Earned Pride entry.

Run from the repo root: python3 -m unittest discover -s tests -v
"""

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


class TestEntry(unittest.TestCase):
    def test_main_writes_one_valid_line(self):
        with tempfile.TemporaryDirectory() as tmp:
            env = dict(os.environ, MAKEFUN_OUTPUT_DIR=tmp)
            result = subprocess.run(
                [sys.executable, str(ROOT / "main.py")],
                env=env, capture_output=True, text=True, timeout=30,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            dest = Path(tmp) / "entry.txt"
            self.assertTrue(dest.is_file())
            raw = dest.read_bytes()
            text = raw.decode("utf-8")  # must be valid UTF-8
            self.assertTrue(text.endswith("\n"), "entry must end with a newline")
            self.assertEqual(text.count("\n"), 1, "entry must be exactly one line")
            line = text.rstrip("\n")
            self.assertTrue(1 <= len(line) <= 240, f"line is {len(line)} chars")
            self.assertTrue(line.strip(), "line must not be only whitespace")
            # Output must be readable by the collector (another user).
            self.assertEqual(oct(dest.stat().st_mode & 0o777), "0o644")


if __name__ == "__main__":
    unittest.main()
