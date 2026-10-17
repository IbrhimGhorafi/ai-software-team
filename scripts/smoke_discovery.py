#!/usr/bin/env python3
"""Mock discovery smoke test for the repository's declarative team inventory.

This checks that inventory paths and agent/skill metadata can be discovered
without starting Claude Code or making network/API calls.
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / ".claude" / "manifest.json"


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"{path.relative_to(ROOT)} has no frontmatter")
    end = re.search(r"\n---\s*(?:\n|$)", text[4:])
    if not end:
        raise ValueError(f"{path.relative_to(ROOT)} has unterminated frontmatter")
    fields: dict[str, str] = {}
    for line in text[4:4 + end.start()].splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Malformed frontmatter in {path.relative_to(ROOT)}: {line}")
        key, value = line.split(":", 1)
        if key.strip() in fields:
            raise ValueError(f"Duplicate frontmatter key {key.strip()} in {path.relative_to(ROOT)}")
        fields[key.strip()] = value.strip().strip('"').strip("'")
    if not fields.get("name") or not fields.get("description"):
        raise ValueError(f"Missing name/description in {path.relative_to(ROOT)}")
    return fields


def main() -> int:
    try:
        inventory = json.loads(MANIFEST.read_text(encoding="utf-8"))["inventory"]
        discovered: dict[str, list[Path]] = {}
        for kind, spec in inventory.items():
            directory = spec["directory"]
            pattern = spec["pattern"]
            folder = ROOT / directory
            paths = sorted(folder.glob(pattern)) if folder.is_dir() else []
            discovered[kind] = paths
            required = spec.get("required", [])
            names = {path.name for path in paths}
            missing = sorted(set(required) - names)
            if missing:
                raise ValueError(f"{kind} missing from discovery: {', '.join(missing)}")
            if kind in ("agents", "skills"):
                minimum = spec["minimum_count"]
                if len(paths) < minimum:
                    raise ValueError(f"{kind}: discovered {len(paths)}, minimum is {minimum}")
            for path in paths:
                if not path.is_file() or not path.read_text(encoding="utf-8").strip():
                    raise ValueError(f"Empty or invalid file: {path.relative_to(ROOT)}")
                if kind in ("agents", "skills"):
                    metadata = frontmatter(path)
                    if kind == "agents" and not metadata.get("tools", "").strip():
                        raise ValueError(f"Agent missing explicit tools allowlist: {path.relative_to(ROOT)}")
        print("MOCK DISCOVERY PASS (does not launch Claude Code)")
        for kind, paths in discovered.items():
            print(f"{kind}: {len(paths)} discovered")
        return 0
    except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"MOCK DISCOVERY FAIL: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
