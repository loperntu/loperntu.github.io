#!/bin/bash
# Publish Mathling book to docs/mathling/book.html
#
# Usage:
#   bash publish.sh
#   bash publish.sh --open

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

SRC_MD="$SCRIPT_DIR/book.md"
OUT_HTML="$SCRIPT_DIR/temp/book.html"
TARGET_HTML="$REPO_ROOT/docs/mathling/book.html"

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

if [[ "${1:-}" == "--open" ]]; then
  if command -v open >/dev/null 2>&1; then
    open "$TARGET_HTML"
  elif command -v xdg-open >/dev/null 2>&1; then
    xdg-open "$TARGET_HTML"
  fi
fi

echo
echo "Next steps:"
echo "  git add docs/mathling/book.html"
echo "  git commit -m \"update mathling book\""
echo "  git push origin main"
