#!/usr/bin/env python3
"""Check CSS/HTML against the Modern Corporate anti-patterns.

Usage: check_compliance.py <file> [<file> ...]

Mechanical checks only. It cannot judge content strategy, evidence quality
or whether the identity mechanism is coherent — a clean run is not approval.
Exit code 1 if any violation is found.
"""

import re
import sys
from pathlib import Path

# (rule id, description, regex, flags)
RULES = [
    (
        "blue-purple-gradient",
        "Generic blue-purple gradient",
        r"linear-gradient\([^)]*(?:#[0-9a-f]*(?:6|7|8)[0-9a-f]{0,5}"
        r"|blue|purple|violet|indigo|#6366f1|#8b5cf6|#7c3aed|#a855f7)[^)]*\)",
        re.I,
    ),
    (
        "full-viewport-sections",
        "More than two full-viewport-height sections",
        r"(?:min-)?height:\s*100(?:vh|dvh|svh)",
        re.I,
    ),
    (
        "glow-effect",
        "Glow / neon shadow — not part of this style",
        r"(?:box|text)-shadow:[^;]*(?:0\s+0\s+\d+|glow)",
        re.I,
    ),
    (
        "backdrop-blur",
        "Glassmorphism / backdrop blur",
        r"backdrop-filter:\s*blur",
        re.I,
    ),
    (
        "excessive-radius",
        "Radius above 1rem / 16px — outside the token scale",
        r"border-radius:\s*(?:[2-9]\d*rem|(?:[2-9]\d|[1-9]\d{2,})px|9999px|50%)",
        re.I,
    ),
    (
        "animated-gradient",
        "Animated gradient background",
        r"animation:[^;]*gradient",
        re.I,
    ),
]

# Rules where a small number of hits is acceptable
THRESHOLDS = {"full-viewport-sections": 2}


def check(path: Path):
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError as exc:
        print(f"  ! cannot read: {exc}")
        return []

    found = []
    for rule_id, desc, pattern, flags in RULES:
        hits = list(re.finditer(pattern, text, flags))
        if len(hits) > THRESHOLDS.get(rule_id, 0):
            lines = sorted({text[: m.start()].count("\n") + 1 for m in hits})
            found.append((rule_id, desc, len(hits), lines[:8]))
    return found


def main(argv):
    if len(argv) < 2:
        print(__doc__.strip())
        return 2

    total = 0
    for name in argv[1:]:
        path = Path(name)
        if not path.is_file():
            print(f"{name}: not a file")
            continue

        violations = check(path)
        if not violations:
            print(f"{name}: clean")
            continue

        print(f"{name}:")
        for rule_id, desc, count, lines in violations:
            loc = ", ".join(f"L{n}" for n in lines)
            print(f"  [{rule_id}] {desc} — {count}x ({loc})")
        total += len(violations)

    if total:
        print(f"\n{total} rule(s) violated.")
        print("Mechanical check only — review the full anti-pattern list in SKILL.md.")
        return 1

    print("\nNo mechanical violations. Review content and hierarchy manually.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
