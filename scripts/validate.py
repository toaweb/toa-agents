#!/usr/bin/env python3
"""Validate Agent Skills in this repo.

Walks skills/*/ and checks each skill's SKILL.md for structural correctness,
frontmatter sanity, reference-file integrity and (advisory) brand-neutrality.

No third-party dependencies. Python 3.8+.

Usage:
    python3 scripts/validate.py            # validate every skill, exit 1 on FAIL
    python3 scripts/validate.py --readme   # print the generated skill table (Markdown)
"""

import os
import sys

# --- paths -------------------------------------------------------------------

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)
SKILLS_DIR = os.path.join(REPO_ROOT, "skills")

# --- thresholds --------------------------------------------------------------

NAME_MAX = 64
DESC_MAX = 1024
DESC_MIN_WORDS = 15          # heuristic: below this, description likely misses WHAT/WHEN
BODY_TOKEN_WARN = 4000       # warn when estimated body tokens exceed this
BODY_TOKEN_HARD = 5000       # documented ceiling (advisory)
TOKENS_PER_WORD = 1.3        # rough word -> token factor

# Characters that make up a relative path we care about.
PATH_CHARS = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_./-")
WORD_CHARS = set("abcdefghijklmnopqrstuvwxyz0123456789_")
NAME_CHARS = set("abcdefghijklmnopqrstuvwxyz0123456789-")
REF_PREFIXES = ("references/", "assets/", "scripts/")

# --- neutrality patterns -----------------------------------------------------
# The actual brand/personal term list is PRIVATE and lives in a gitignored
# local file so the public repo never publishes your own vocabulary
# (usernames, hostnames, internal tool names, brand hex colors, ...).
#
#   scripts/neutrality-terms.local.txt     one term per line, '#'-comments OK
#
# Term kinds (auto-detected per line):
#   - hex color        e.g. `#2dd4bf` or `2dd4bf`  -> case-insensitive substring
#                      match on `#<hex>` (3, 4, 6 or 8 hex digits)
#   - substring term   contains any non-word char (space, /, :, .) ->
#                      literal case-insensitive substring match
#   - word term        plain word -> whole-word match (letters/digits/_
#                      boundaries), so "describe" never matches a term "scribe"
#
# See scripts/neutrality-terms.example.txt for the format. Without the local
# file, only the generic fallback below is checked.
TERMS_LOCAL_FILE = os.path.join(SCRIPT_DIR, "neutrality-terms.local.txt")
FALLBACK_WORD_TERMS = ["brand_color"]
FALLBACK_SUBSTR_TERMS = ["/home/myuser"]
FALLBACK_HEX_TERMS = []


def _looks_like_hex(term):
    t = term.lstrip("#")
    return len(t) in (3, 4, 6, 8) and all(c in "0123456789abcdef" for c in t.lower())


def load_neutrality_terms():
    """Return (word_terms, substr_terms, hex_terms), all lowercase."""
    if not os.path.isfile(TERMS_LOCAL_FILE):
        return (list(FALLBACK_WORD_TERMS),
                list(FALLBACK_SUBSTR_TERMS),
                list(FALLBACK_HEX_TERMS))
    words, substrs, hexes = [], [], []
    with open(TERMS_LOCAL_FILE, "r", encoding="utf-8") as fh:
        for raw in fh:
            term = raw.split("#", 1)[0].strip().lower() if not raw.strip().startswith("#") else ""
            # allow hex terms written with a leading '#': take the whole line then
            if not term and raw.strip().startswith("#") and _looks_like_hex(raw.strip()):
                term = raw.strip().lower()
            if not term:
                continue
            if _looks_like_hex(term):
                hexes.append("#" + term.lstrip("#"))
            elif any(c not in WORD_CHARS for c in term):
                substrs.append(term)
            else:
                words.append(term)
    return words, substrs, hexes


BRAND_WORD_TERMS, BRAND_SUBSTR_TERMS, BRAND_HEX_TERMS = load_neutrality_terms()

# --- result model ------------------------------------------------------------

OK, WARN, FAIL = "OK", "WARN", "FAIL"


class Report:
    def __init__(self, name):
        self.name = name
        self.lines = []  # (level, message)

    def add(self, level, message):
        self.lines.append((level, message))

    def result(self):
        levels = [lvl for lvl, _ in self.lines]
        if FAIL in levels:
            return FAIL
        if WARN in levels:
            return WARN
        return OK


# --- tiny frontmatter parser -------------------------------------------------

def split_frontmatter(text):
    """Return (frontmatter_dict, body_str) or (None, whole_text) if no valid block.

    Only handles top-level `key: value` scalars on single lines — enough for
    skill frontmatter (name, description). Does not attempt full YAML.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None, text
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text

    fm = {}
    for raw in lines[1:end]:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        # top-level key only (no leading whitespace)
        if raw[0] in (" ", "\t"):
            continue
        if ":" not in raw:
            continue
        key, _, value = raw.partition(":")
        fm[key.strip()] = value.strip()

    body = "\n".join(lines[end + 1:])
    return fm, body


# --- helpers -----------------------------------------------------------------

def is_word_boundary(text, start, end):
    before = text[start - 1] if start > 0 else ""
    after = text[end] if end < len(text) else ""
    return (before.lower() not in WORD_CHARS) and (after.lower() not in WORD_CHARS)


def find_whole_word(line_lower, needle):
    """Yield start indices where needle occurs with word boundaries."""
    idx = line_lower.find(needle)
    while idx != -1:
        if is_word_boundary(line_lower, idx, idx + len(needle)):
            yield idx
        idx = line_lower.find(needle, idx + 1)


def neutrality_hits(body):
    """Return list of (lineno, term) advisory matches."""
    hits = []
    for lineno, line in enumerate(body.splitlines(), start=1):
        low = line.lower()
        for term in BRAND_WORD_TERMS:
            if next(find_whole_word(low, term), None) is not None:
                hits.append((lineno, term))
        for term in BRAND_SUBSTR_TERMS:
            if term in low:
                hits.append((lineno, term))
        for term in BRAND_HEX_TERMS:
            # hex boundary: next char must not extend the hex value
            idx = low.find(term)
            while idx != -1:
                after = low[idx + len(term)] if idx + len(term) < len(low) else ""
                if after not in "0123456789abcdef":
                    hits.append((lineno, term))
                    break
                idx = low.find(term, idx + 1)
    return hits


SCANNABLE_EXTS = (".md", ".css", ".py", ".sh", ".json", ".txt", ".yml", ".yaml",
                  ".js", ".ts", ".html", ".toml")


def neutrality_scan_dir(root, skip_rel=()):
    """Scan every text file under root; return [(relpath:lineno, term)]."""
    hits = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in sorted(filenames):
            if not fn.lower().endswith(SCANNABLE_EXTS):
                continue
            fp = os.path.join(dirpath, fn)
            rel = os.path.relpath(fp, root)
            if rel in skip_rel:
                continue
            try:
                with open(fp, "r", encoding="utf-8") as fh:
                    text = fh.read()
            except (OSError, UnicodeDecodeError):
                continue
            for lineno, term in neutrality_hits(text):
                hits.append((f"{rel}:{lineno}", term))
    return hits


def extract_ref_paths(body):
    """Return an ordered, de-duplicated list of relative reference paths."""
    found = []
    seen = set()
    for prefix in REF_PREFIXES:
        start = body.find(prefix)
        while start != -1:
            # require a boundary before the prefix so 'myreferences/' is ignored
            before = body[start - 1] if start > 0 else ""
            if before not in PATH_CHARS or before in " \t\n`|(":
                end = start
                while end < len(body) and body[end] in PATH_CHARS:
                    end += 1
                path = body[start:end].rstrip(".")  # trailing sentence dot
                if path not in seen and path.endswith((".md", ".css", ".py", ".json", ".txt")):
                    seen.add(path)
                    found.append(path)
            start = body.find(prefix, start + 1)
    return found


def estimate_tokens(body):
    words = len(body.split())
    return int(words * TOKENS_PER_WORD), words


def validate_name(name):
    problems = []
    if not name:
        return ["name is empty"]
    if len(name) > NAME_MAX:
        problems.append(f"name is {len(name)} chars (> {NAME_MAX})")
    bad = sorted(set(c for c in name if c not in NAME_CHARS))
    if bad:
        problems.append("name has illegal chars %r (want lowercase-hyphens)" % "".join(bad))
    if name.startswith("-") or name.endswith("-"):
        problems.append("name starts/ends with a hyphen")
    return problems


# --- per-skill validation ----------------------------------------------------

def load_skill(skill_dir):
    """Return (frontmatter, body) or (None, None) if unreadable/invalid."""
    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        return None, None
    with open(skill_md, "r", encoding="utf-8") as fh:
        text = fh.read()
    return split_frontmatter(text)


def validate_skill(skill_dir):
    name_on_disk = os.path.basename(skill_dir.rstrip("/"))
    rep = Report(name_on_disk)

    skill_md = os.path.join(skill_dir, "SKILL.md")
    if not os.path.isfile(skill_md):
        rep.add(FAIL, "SKILL.md is missing")
        return rep

    fm, body = load_skill(skill_dir)
    if fm is None:
        rep.add(FAIL, "SKILL.md has no valid --- frontmatter --- block")
        return rep
    rep.add(OK, "SKILL.md has a frontmatter block")

    # (b) required keys
    name = fm.get("name")
    desc = fm.get("description")
    if name is None:
        rep.add(FAIL, "frontmatter missing 'name'")
    if desc is None:
        rep.add(FAIL, "frontmatter missing 'description'")
    if name is None or desc is None:
        return rep

    # (c) name matches directory
    if name == name_on_disk:
        rep.add(OK, "name matches directory")
    else:
        rep.add(FAIL, f"name '{name}' != directory '{name_on_disk}'")

    # (d) name format
    name_problems = validate_name(name)
    if name_problems:
        for p in name_problems:
            rep.add(FAIL, p)
    else:
        rep.add(OK, f"name is valid lowercase-hyphens ({len(name)} chars)")

    # (e) description length + WHAT/WHEN heuristic
    if len(desc) > DESC_MAX:
        rep.add(FAIL, f"description is {len(desc)} chars (> {DESC_MAX})")
    else:
        rep.add(OK, f"description length OK ({len(desc)} chars)")
    words = len(desc.split())
    if words < DESC_MIN_WORDS:
        rep.add(WARN, f"description is {words} words (< {DESC_MIN_WORDS}) — state WHAT it does AND WHEN to use it")

    # (f) body token estimate
    tokens, wordcount = estimate_tokens(body)
    if tokens > BODY_TOKEN_HARD:
        rep.add(FAIL, f"body ~{tokens} tokens (> {BODY_TOKEN_HARD} ceiling; {wordcount} words)")
    elif tokens > BODY_TOKEN_WARN:
        rep.add(WARN, f"body ~{tokens} tokens (> {BODY_TOKEN_WARN}; {wordcount} words) — consider moving detail to references/")
    else:
        rep.add(OK, f"body size OK (~{tokens} tokens, {wordcount} words)")

    # (g) referenced files exist  — the important one
    refs = extract_ref_paths(body)
    if not refs:
        rep.add(WARN, "SKILL.md mentions no reference files")
    else:
        for path in refs:
            full = os.path.join(skill_dir, path)
            if os.path.isfile(full):
                rep.add(OK, f"reference exists: {path}")
            else:
                rep.add(FAIL, f"referenced file missing: {path}")

    # orphan references/*.md not mentioned in SKILL.md (advisory)
    ref_dir = os.path.join(skill_dir, "references")
    if os.path.isdir(ref_dir):
        for fn in sorted(os.listdir(ref_dir)):
            if fn.endswith(".md") and ("references/" + fn) not in refs:
                rep.add(WARN, f"references/{fn} exists but is not mentioned in SKILL.md")

    # (h) neutrality — advisory, never a hard fail.
    # Scans EVERY text file in the skill directory: SKILL.md including
    # frontmatter, references/, assets/ (token CSS!), scripts/ — a brand hex
    # in a token file must not slip through.
    hits = neutrality_scan_dir(skill_dir)
    if hits:
        for loc, term in hits:
            rep.add(WARN, f"neutrality: '{term}' at {loc} — review manually")
    else:
        rep.add(OK, "no brand/personal-path markers found")
    if not os.path.isfile(TERMS_LOCAL_FILE):
        rep.add(WARN, "neutrality: no scripts/neutrality-terms.local.txt — "
                      "only the generic fallback terms were checked")

    return rep


# --- agents validation -------------------------------------------------------

AGENTS_DIR = os.path.join(REPO_ROOT, "agents")
SKILL_LOOKUP_MARKER = "skills/"   # every agent must instruct a skills/ lookup


def validate_agent(path):
    rep = Report("agents/" + os.path.basename(path))
    with open(path, "r", encoding="utf-8") as fh:
        text = fh.read()
    fm, body = split_frontmatter(text)
    if fm is None:
        rep.add(FAIL, "no valid --- frontmatter --- block")
        return rep
    for key in ("name", "description"):
        if not fm.get(key):
            rep.add(FAIL, f"frontmatter missing '{key}'")
    if fm.get("name") and fm["name"] + ".md" != os.path.basename(path):
        rep.add(FAIL, f"name '{fm['name']}' != filename '{os.path.basename(path)}'")
    if SKILL_LOOKUP_MARKER not in body:
        rep.add(FAIL, "agent never instructs a skills/ lookup — the skill-first "
                      "workflow is the whole point; add the mandatory lookup step")
    else:
        rep.add(OK, "instructs a skills/ lookup")
    for lineno, term in neutrality_hits(text):
        rep.add(WARN, f"neutrality: '{term}' at line {lineno} — review manually")
    if rep.result() == OK:
        rep.add(OK, "frontmatter and skill-first workflow OK")
    return rep


def discover_agents():
    if not os.path.isdir(AGENTS_DIR):
        return []
    return [os.path.join(AGENTS_DIR, f)
            for f in sorted(os.listdir(AGENTS_DIR))
            if f.endswith(".md")]


# --- discovery ---------------------------------------------------------------

def discover_skills():
    if not os.path.isdir(SKILLS_DIR):
        return []
    out = []
    for name in sorted(os.listdir(SKILLS_DIR)):
        d = os.path.join(SKILLS_DIR, name)
        if os.path.isdir(d):
            out.append(d)
    return out


# --- readme table ------------------------------------------------------------

def generate_readme_table():
    rows = []
    for skill_dir in discover_skills():
        fm, _ = load_skill(skill_dir)
        name = (fm or {}).get("name", os.path.basename(skill_dir))
        desc = (fm or {}).get("description", "").strip()
        # collapse whitespace; escape pipes for Markdown table cells
        desc = " ".join(desc.split()).replace("|", "\\|")
        rows.append((name, desc))

    lines = ["| Skill | Description |", "|---|---|"]
    for name, desc in rows:
        lines.append(f"| `{name}` | {desc} |")
    return "\n".join(lines)


# --- readme write ------------------------------------------------------------

README_PATH = os.path.join(REPO_ROOT, "README.md")
TABLE_BEGIN = "<!-- BEGIN SKILLS TABLE"
TABLE_END = "<!-- END SKILLS TABLE -->"


def write_readme_table():
    """Replace the block between the BEGIN/END markers in README.md in place."""
    with open(README_PATH, "r", encoding="utf-8") as fh:
        text = fh.read()
    begin = text.find(TABLE_BEGIN)
    end = text.find(TABLE_END)
    if begin == -1 or end == -1 or end < begin:
        print("README.md: BEGIN/END SKILLS TABLE markers not found", file=sys.stderr)
        return 1
    begin_line_end = text.index("\n", begin) + 1
    new = text[:begin_line_end] + generate_readme_table() + "\n" + text[end:]
    if new == text:
        print("README.md table already up to date")
        return 0
    with open(README_PATH, "w", encoding="utf-8") as fh:
        fh.write(new)
    print("README.md table updated")
    return 0


# --- main --------------------------------------------------------------------

def main(argv):
    if "--readme" in argv:
        if "--write" in argv:
            return write_readme_table()
        print(generate_readme_table())
        return 0

    skills = discover_skills()
    if not skills:
        print(f"No skills found under {SKILLS_DIR}", file=sys.stderr)
        return 1

    any_fail = False
    counts = {OK: 0, WARN: 0, FAIL: 0}

    reports = [validate_skill(d) for d in skills]
    reports += [validate_agent(p) for p in discover_agents()]

    for rep in reports:
        res = rep.result()
        counts[res] += 1
        if res == FAIL:
            any_fail = True

        print(f"=== {rep.name} ===  [{res}]")
        for level, msg in rep.lines:
            marker = {OK: "OK  ", WARN: "WARN", FAIL: "FAIL"}[level]
            print(f"  [{marker}] {msg}")
        print()

    print(f"Summary: {len(reports)} checked "
          f"({len(skills)} skills, {len(reports) - len(skills)} agents) — "
          f"{counts[OK]} OK, {counts[WARN]} WARN, {counts[FAIL]} FAIL")
    return 1 if any_fail else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
