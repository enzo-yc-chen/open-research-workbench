#!/usr/bin/env python3
"""Small publication-safety scanner for the template workspace.

The script is intentionally conservative. It reports suspicious text matches
and leaves final judgment to the human reviewer.
"""

from __future__ import annotations

import argparse
import fnmatch
import re
from pathlib import Path


DEFAULT_PATTERNS = {
    "absolute-posix-path": re.compile(r"/" + r"home/[^\\s)>'\"]+"),
    "windows-user-path": re.compile(r"[A-Za-z]:\\\\Users\\\\[^\\s)>'\"]+"),
    "private-key": re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----"),
    "token-like": re.compile(r"(?i)(api[_-]?key|token|secret|password)\\s*[:=]"),
    "ssh-url": re.compile(r"git@[^\\s:]+:[^\\s]+"),
    "http-private-host-hint": re.compile(r"https?://(?:localhost|127\\.0\\.0\\.1|10\\.|192\\.168\\.)[^\\s)>'\"]*"),
}

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".pytest_cache", ".mypy_cache"}
SKIP_GLOBS = {"*.png", "*.jpg", "*.jpeg", "*.pdf", "*.h5", "*.bin", "*.dat", "*.npy", "*.npz"}
SKIP_FILES = {Path("scripts/privacy_scan.py")}


def should_skip(path: Path) -> bool:
    if path in SKIP_FILES:
        return True
    if any(part in SKIP_DIRS for part in path.parts):
        return True
    return any(fnmatch.fnmatch(path.name, glob) for glob in SKIP_GLOBS)


def scan(root: Path) -> int:
    count = 0
    for path in sorted(root.rglob("*")):
        if not path.is_file() or should_skip(path.relative_to(root)):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for label, pattern in DEFAULT_PATTERNS.items():
                if pattern.search(line):
                    count += 1
                    rel = path.relative_to(root)
                    print(f"{rel}:{lineno}: {label}: {line.strip()}")
    return count


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", nargs="?", default=".", help="repository root")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    count = scan(root)
    if count:
        print(f"Found {count} suspicious match(es).")
        return 1
    print("No suspicious matches found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
