#!/bin/bash
# Publish Mathling book (EN + 中文) to docs/mathling/
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

echo "🔨 Building Mathling book (EN + 中文)..."
cd "$SCRIPT_DIR"
python3 build.py

if [[ ! -f "$OUT_HTML" ]]; then
  echo "❌ Build output missing: $OUT_HTML"
  exit 1
fi

mkdir -p "$TARGET_DIR"

cp "$OUT_HTML" "$TARGET_HTML"
echo "✅ Synced to: $TARGET_HTML"

if [[ -f "$OUT_HTML_ZH" ]]; then
  cp "$OUT_HTML_ZH" "$TARGET_DIR/book-zh.html"
  echo "✅ Synced to: $TARGET_DIR/book-zh.html"
fi

# Keep companion assets next to the book HTML
if [[ -d "$SCRIPT_DIR/figures" ]]; then
  mkdir -p "$TARGET_DIR/figures"
  cp -a "$SCRIPT_DIR/figures/." "$TARGET_DIR/figures/"
  echo "✅ Synced figures/ → $TARGET_DIR/figures/"
fi

if [[ -f "$SCRIPT_DIR/language_complexity_simulator.html" ]]; then
  cp "$SCRIPT_DIR/language_complexity_simulator.html" "$TARGET_DIR/language_complexity_simulator.html"
  echo "✅ Synced language_complexity_simulator.html"
fi

# Interactive primers for Appendix: Mathematical Foundations / 語言學的數學基礎
if [[ -d "$SCRIPT_DIR/foundations" ]]; then
  mkdir -p "$TARGET_DIR/foundations"
  rsync -a --delete \
    --exclude 'work/' \
    --exclude 'uploads/' \
    --exclude '.DS_Store' \
    --exclude '.thumbnail' \
    "$SCRIPT_DIR/foundations/" "$TARGET_DIR/foundations/"
  echo "✅ Synced foundations/ → $TARGET_DIR/foundations/"
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
echo "  git add docs/mathling/book.html docs/mathling/book-zh.html docs/mathling/foundations docs/mathling/figures docs/mathling/language_complexity_simulator.html docs/mathling/index.html"
echo "  git commit -m \"update mathling bilingual book\""
echo "  git push origin main"
