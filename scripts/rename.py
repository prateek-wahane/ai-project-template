"""Rename the template package: python scripts/rename.py my_new_package"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OLD = "project_name"
TEXT_SUFFIXES = {".py", ".toml", ".md", ".yml", ".yaml", ".txt", ".cfg", ".example"}


def main() -> None:
    if len(sys.argv) != 2 or not re.fullmatch(r"[a-z][a-z0-9_]*", sys.argv[1]):
        sys.exit("usage: python scripts/rename.py <snake_case_package_name>")
    new = sys.argv[1]
    src = ROOT / "src" / OLD
    if not src.exists():
        sys.exit(f"{src} not found - already renamed?")

    changed = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or ".venv" in path.parts or path.suffix not in TEXT_SUFFIXES:
            continue
        if path.name == "rename.py":
            continue
        text = path.read_text(encoding="utf-8")
        if OLD in text:
            path.write_text(text.replace(OLD, new), encoding="utf-8")
            changed += 1
    src.rename(src.with_name(new))
    print(f"renamed package to {new!r}; updated {changed} files")


if __name__ == "__main__":
    main()
