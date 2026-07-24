#!/usr/bin/env python3
"""Sweep arbitrary directories for brand/personal markers.

Scans one or more directory trees for every term in the private neutrality
term list and reports hits grouped per file. Use it to inventory brand
material before migrating it to its canonical home, and afterwards to verify
that nothing brand-specific remains scattered outside it.

    scripts/sweep.py ~/projects                      # sweep a tree
    scripts/sweep.py ~/projects ~/.claude            # several roots
    scripts/sweep.py ~/projects --exclude toa-rules  # skip canonical home
    scripts/sweep.py ~/projects --terms my-terms.txt # alternate term list
    scripts/sweep.py ~/projects --per-term           # per-term summary

Exit code 1 if any hit was found (clean sweep = 0), so it doubles as a
"migration complete" check.

Reuses the term parser and matcher from validate.py — one definition of what
counts as a brand marker, two front-ends. No dependencies, Python 3.8+.
"""

import argparse
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
import validate as v  # noqa: E402  (term parsing + matching live there)

REPO_ROOT = os.path.dirname(SCRIPT_DIR)

# Directories never worth scanning (deps, caches, build output, VCS internals).
SKIP_DIRS = {
    ".git", ".hg", ".svn",
    "node_modules", ".pnpm-store", "bower_components", "vendor",
    ".venv", "venv", "__pycache__", ".mypy_cache", ".ruff_cache",
    ".pytest_cache", ".tox",
    "dist", "build", "out", ".output", "_site", "public",
    ".next", ".nuxt", ".astro", ".svelte-kit", ".vercel", ".netlify",
    ".cache", ".parcel-cache", ".turbo",
    "target",  # rust/java
}

# Extensions to scan, beyond validate.py's set: source and template files
# where brand values typically hide.
EXTRA_EXTS = (
    ".vue", ".astro", ".jsx", ".tsx", ".mdx", ".svelte",
    ".go", ".rs", ".php", ".rb",
    ".scss", ".sass", ".less", ".svg",
    ".env.example", ".conf", ".ini", ".cfg", ".xml",
)
SCAN_EXTS = tuple(v.SCANNABLE_EXTS) + EXTRA_EXTS

# Extensionless filenames worth scanning.
SCAN_NAMES = {"Dockerfile", "Makefile", "Caddyfile", "Justfile", "CLAUDE",
              "AGENTS", "README", "LICENSE"}

MAX_BYTES = 2_000_000  # skip anything larger — not hand-written config/docs


def should_scan(filename):
    if filename in SCAN_NAMES:
        return True
    return filename.lower().endswith(SCAN_EXTS)


def is_probably_binary(chunk):
    return b"\x00" in chunk


def iter_files(root, exclude_abs):
    for dirpath, dirnames, filenames in os.walk(root):
        # prune skip-dirs and excluded paths in place
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIRS
            and os.path.join(dirpath, d) not in exclude_abs
        ]
        for fn in sorted(filenames):
            if should_scan(fn):
                yield os.path.join(dirpath, fn)


def scan_file(path):
    """Return list of (lineno, term) or [] — silently skips unreadables."""
    try:
        if os.path.getsize(path) > MAX_BYTES:
            return []
        with open(path, "rb") as fh:
            head = fh.read(4096)
        if is_probably_binary(head):
            return []
        with open(path, "r", encoding="utf-8", errors="ignore") as fh:
            return v.neutrality_hits(fh.read())
    except OSError:
        return []


def main(argv):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("roots", nargs="+", help="directory tree(s) to sweep")
    p.add_argument("--terms", default=None,
                   help="term list file (default: the repo's private list)")
    p.add_argument("--exclude", action="append", default=[],
                   help="path to skip entirely (repeatable)")
    p.add_argument("--include-self", action="store_true",
                   help="also sweep the toa-agents repo itself "
                        "(excluded by default; validate.py owns it)")
    p.add_argument("--per-term", action="store_true",
                   help="print a per-term hit count summary")
    args = p.parse_args(argv)

    # Load terms (possibly from an alternate file) into validate's globals so
    # neutrality_hits uses them.
    words, substrs, hexes = v.load_neutrality_terms(args.terms)
    v.BRAND_WORD_TERMS, v.BRAND_SUBSTR_TERMS, v.BRAND_HEX_TERMS = words, substrs, hexes
    n_terms = len(words) + len(substrs) + len(hexes)
    if n_terms == 0:
        print("No terms loaded — nothing to sweep for.", file=sys.stderr)
        return 2
    using_fallback = args.terms is None and not os.path.isfile(v.TERMS_LOCAL_FILE)
    if using_fallback:
        print("WARNING: no private term list found — sweeping with generic "
              "fallback terms only.\n", file=sys.stderr)

    exclude_abs = {os.path.abspath(os.path.expanduser(e)) for e in args.exclude}
    if not args.include_self:
        exclude_abs.add(os.path.abspath(REPO_ROOT))
    # Never report the term list itself — it is hits by definition.
    terms_file = os.path.abspath(args.terms or v.TERMS_LOCAL_FILE)

    files_scanned = 0
    files_hit = 0
    total_hits = 0
    per_term = {}

    for root in args.roots:
        root = os.path.abspath(os.path.expanduser(root))
        if not os.path.isdir(root):
            print(f"skip (not a directory): {root}", file=sys.stderr)
            continue
        for path in iter_files(root, exclude_abs):
            if os.path.abspath(path) == terms_file:
                continue
            files_scanned += 1
            hits = scan_file(path)
            if not hits:
                continue
            files_hit += 1
            total_hits += len(hits)
            print(f"== {path} ({len(hits)} hit{'s' if len(hits) != 1 else ''})")
            for lineno, term in hits:
                per_term[term] = per_term.get(term, 0) + 1
                print(f"   {lineno}: {term}")
            print()

    if args.per_term and per_term:
        print("Per-term summary:")
        for term, count in sorted(per_term.items(), key=lambda kv: -kv[1]):
            print(f"  {count:5d}  {term}")
        print()

    print(f"Swept {files_scanned} files with {n_terms} terms — "
          f"{files_hit} file(s) with {total_hits} hit(s).")
    if total_hits == 0:
        print("Clean sweep. ✔")
    return 1 if total_hits else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
