#!/usr/bin/env bash
#
# Symlink every skill in this repo's skills/ into your Claude skills directory
# (~/.claude/skills/ by default; override with CLAUDE_SKILLS_DIR), and every
# agent in agents/ into your Claude agents directory (~/.claude/agents/ by
# default; override with CLAUDE_AGENTS_DIR).
#
# The agent files are canonical and client-neutral markdown. Claude Code reads
# them directly; for other clients (Codex, OpenCode, ...) point the client at
# the same files or add a translation step here — the repo stays the single
# source of truth either way.
#
#   scripts/install.sh            link every skill + agent
#   scripts/install.sh --dry-run  show what would happen, change nothing
#
# Properties:
#   - absolute paths (the repo can live anywhere)
#   - idempotent (safe to re-run)
#   - never overwrites anything that is not already a symlink into this repo;
#     it warns and skips instead
#
set -euo pipefail

# --- resolve paths (absolute, location-independent) --------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
SKILLS_DIR="$REPO_ROOT/skills"
TARGET_DIR="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"

REPO_ROOT_CANON="$(readlink -f "$REPO_ROOT")"

# --- args --------------------------------------------------------------------
DRY_RUN=0
for arg in "$@"; do
  case "$arg" in
    --dry-run) DRY_RUN=1 ;;
    -h|--help)
      grep '^#' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//; 1d'
      exit 0 ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo "Usage: $(basename "$0") [--dry-run]" >&2
      exit 2 ;;
  esac
done

run() {
  # Execute a command, or just describe it under --dry-run.
  if [ "$DRY_RUN" -eq 1 ]; then
    return 0
  fi
  "$@"
}

# --- sanity ------------------------------------------------------------------
if [ ! -d "$SKILLS_DIR" ]; then
  echo "ERROR: no skills/ directory at $SKILLS_DIR" >&2
  exit 1
fi

shopt -s nullglob
skill_dirs=("$SKILLS_DIR"/*/)
shopt -u nullglob
if [ "${#skill_dirs[@]}" -eq 0 ]; then
  echo "ERROR: no skills found under $SKILLS_DIR" >&2
  exit 1
fi

echo "Repo:   $REPO_ROOT"
echo "Target: $TARGET_DIR"
if [ "$DRY_RUN" -eq 1 ]; then
  echo "Mode:   DRY RUN (no changes)"
fi
echo

# --- ensure target dir -------------------------------------------------------
if [ ! -d "$TARGET_DIR" ]; then
  echo "[MKDIR] $TARGET_DIR"
  run mkdir -p "$TARGET_DIR"
fi

# --- link each skill ---------------------------------------------------------
linked=0 relinked=0 already=0 warned=0

for skill_path in "${skill_dirs[@]}"; do
  src="${skill_path%/}"                 # strip trailing slash
  name="$(basename "$src")"
  target="$TARGET_DIR/$name"
  src_canon="$(readlink -f "$src")"

  if [ -L "$target" ]; then
    # It is a symlink (possibly broken). Where does it resolve?
    resolved="$(readlink -f "$target" 2>/dev/null || true)"
    if [ "$resolved" = "$src_canon" ]; then
      echo "[OK]    $name -> already linked"
      already=$((already + 1))
    elif [ -n "$resolved" ] && [ "${resolved#$REPO_ROOT_CANON/}" != "$resolved" ]; then
      # symlink points somewhere else inside THIS repo -> managed by us, fix it
      echo "[RELINK] $name -> was $resolved"
      run rm "$target"
      run ln -s "$src" "$target"
      relinked=$((relinked + 1))
    else
      echo "[WARN]  $name -> symlink points outside this repo ($resolved); left untouched"
      warned=$((warned + 1))
    fi
  elif [ -e "$target" ]; then
    # A real file or directory — never overwrite.
    echo "[WARN]  $name -> exists and is not a symlink; left untouched"
    warned=$((warned + 1))
  else
    echo "[LINK]  $name -> $target"
    run ln -s "$src" "$target"
    linked=$((linked + 1))
  fi
done

# --- link each agent ---------------------------------------------------------
AGENTS_SRC="$REPO_ROOT/agents"
AGENTS_TARGET_DIR="${CLAUDE_AGENTS_DIR:-$HOME/.claude/agents}"

if [ -d "$AGENTS_SRC" ]; then
  echo
  echo "Agents: $AGENTS_TARGET_DIR"
  if [ ! -d "$AGENTS_TARGET_DIR" ]; then
    echo "[MKDIR] $AGENTS_TARGET_DIR"
    run mkdir -p "$AGENTS_TARGET_DIR"
  fi

  shopt -s nullglob
  agent_files=("$AGENTS_SRC"/*.md)
  shopt -u nullglob

  for src in "${agent_files[@]}"; do
    name="$(basename "$src")"
    target="$AGENTS_TARGET_DIR/$name"
    src_canon="$(readlink -f "$src")"

    if [ -L "$target" ]; then
      resolved="$(readlink -f "$target" 2>/dev/null || true)"
      if [ "$resolved" = "$src_canon" ]; then
        echo "[OK]    $name -> already linked"
        already=$((already + 1))
      elif [ -n "$resolved" ] && [ "${resolved#"$REPO_ROOT_CANON"/}" != "$resolved" ]; then
        echo "[RELINK] $name -> was $resolved"
        run rm "$target"
        run ln -s "$src" "$target"
        relinked=$((relinked + 1))
      else
        echo "[WARN]  $name -> symlink points outside this repo ($resolved); left untouched"
        warned=$((warned + 1))
      fi
    elif [ -e "$target" ]; then
      echo "[WARN]  $name -> exists and is not a symlink; left untouched"
      warned=$((warned + 1))
    else
      echo "[LINK]  $name -> $target"
      run ln -s "$src" "$target"
      linked=$((linked + 1))
    fi
  done
fi

# --- summary -----------------------------------------------------------------
echo
echo "Done: $linked linked, $relinked relinked, $already already ok, $warned warned."
if [ "$DRY_RUN" -eq 1 ]; then
  echo "(dry run — nothing was changed)"
fi
if [ "$warned" -gt 0 ]; then
  echo "Review the [WARN] entries above; nothing was overwritten."
fi
