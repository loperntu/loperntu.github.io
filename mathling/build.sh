#!/bin/bash
# ═══════════════════════════════════════════════════
#  build.sh — One-command build: book.md → index.html
# ═══════════════════════════════════════════════════
#
#  Usage:
#    bash build.sh              # build book.md → index.html
#    bash build.sh --open       # build and open in browser (macOS)
#    bash build.sh src.md o.html # custom paths
#
# ═══════════════════════════════════════════════════

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

SRC="${1:-book.md}"
OUT="${2:-index.html}"

# Skip flags
[[ "$SRC" == --* ]] && SRC="book.md"
[[ "$OUT" == --* ]] && OUT="index.html"

echo "🔨 Building..."
python3 build.py "$SRC" "$OUT"

# Open in browser if --open flag
if [[ "$*" == *--open* ]]; then
  if command -v open &>/dev/null; then
    open "$OUT"
  elif command -v xdg-open &>/dev/null; then
    xdg-open "$OUT"
  fi
fi

echo "🎉 Done!"
