#!/bin/bash
# ═══════════════════════════════════════════════════
#  build.sh — One-command build: book.md → temp/book.html
# ═══════════════════════════════════════════════════
#
#  Usage:
#    bash build.sh              # build with defaults
#    bash build.sh --open       # build and open in browser (macOS)
#    bash build.sh src.md o.html # custom paths
#
# ═══════════════════════════════════════════════════

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

SRC="${1:-book.md}"
OUT="${2:-temp/book.html}"

# Skip flags
[[ "$SRC" == --* ]] && SRC="book.md"
[[ "$OUT" == --* ]] && OUT="temp/book.html"

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
