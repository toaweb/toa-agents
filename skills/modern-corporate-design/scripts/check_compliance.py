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
        # Match only *named* blue/purple words and the well-known indigo/violet
        # framework hexes. Never guess hue from arbitrary hex digits — that
        # flags warm and green palettes as "blue-purple" (false positives).
        "blue-purple-gradient",
        "Generic blue-purple gradient",
        r"linear-gradient\([^)]*(?:\b(?:blue|purple|violet|indigo)\b"
        r"|#(?:6366f1|818cf8|4f46e5|4338ca|8b5cf6|7c3aed|6d28d9|a855f7|9333ea|c084fc)\b)[^)]*\)",
        re.I,
    ),
    (
        "full-viewport-sections",
        "More than two full-viewport-height sections",
        r"(?:min-)?height:\s*100(?:vh|dvh|svh)",
        re.I,
    ),
    (
        # Glow requires actual blur: third length value > 0.
        # `0 0 0 1px` (hairline ring / border substitute) is NOT a glow.
        "glow-effect",
        "Glow / neon shadow — not part of this style",
        r"(?:(?:box|text)-shadow:|(?:box|text)-shadow:[^;]*,)\s*(?:inset\s+)?"
        r"0(?:px)?\s+0(?:px)?\s+0*[1-9]\d*(?:\.\d+)?(?:px|rem|em)"
        r"|(?:box|text)-shadow:[^;]*\bglow\b",
        re.I,
    ),
    (
        "backdrop-blur",
        "Glassmorphism / backdrop blur",
        r"backdrop-filter:\s*blur",
        re.I,
    ),
    (
        # Flags radii between 17px/1.05rem and 999px — outside the token scale.
        # Deliberately ALLOWS `9999px` (pill) and `50%` (avatar): both are
        # legitimate `--radius-full` uses; the token scale should include it.
        "excessive-radius",
        "Radius above 1rem / 16px — outside the token scale (pill 9999px / avatar 50% allowed)",
        r"border-radius:\s*(?:\b(?:1[7-9]|[2-9]\d|[1-9]\d{2})px\b"
        r"|\b(?:[2-9]\d*(?:\.\d+)?|1\.\d*[1-9])rem\b)",
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
