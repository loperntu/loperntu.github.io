#!/bin/bash
# Publish Mathling book (EN + 中文) to docs/mathling/book.html and book-zh.html
#
# Usage:
#   bash publish.sh
#   bash publish.sh --open

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

SRC_MD="$SCRIPT_DIR/book.md"
OUT_HTML="$SCRIPT_DIR/temp/book.html"
OUT_HTML_ZH="$SCRIPT_DIR/temp/book-zh.html"
TARGET_DIR="$REPO_ROOT/docs/mathling"
TARGET_HTML="$TARGET_DIR/book.html"

if [[ ! -f "$SRC_MD" ]]; then
  echo "❌ Source not found: $SRC_MD"
  exit 1
fi

echo "🔨 Building Mathling book..."
cd "$SCRIPT_DIR"
python3 build.py

if [[ ! -f "$OUT_HTML" ]]; then
  echo "❌ Build output missing: $OUT_HTML"
  exit 1
fi

mkdir -p "$(dirname "$TARGET_HTML")"
cp "$OUT_HTML" "$TARGET_HTML"
echo "✅ Synced to: $TARGET_HTML"
if [[ -f "$OUT_HTML_ZH" ]]; then
  cp "$OUT_HTML_ZH" "$TARGET_DIR/book-zh.html"
  echo "✅ Synced to: $TARGET_DIR/book-zh.html"
fi

if [[ "${1:-}" == "--open" ]]; then
  if command -v open >/dev/null 2>&1; then
    open "$TARGET_HTML"
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$TARGET_HTML"
  fi
fi

echo
echo "Next steps:"
echo "  git add docs/mathling/book.html docs/mathling/book-zh.html"
echo "  git commit -m \"update mathling book\""
echo "  git push origin main"
