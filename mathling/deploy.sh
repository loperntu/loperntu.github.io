#!/bin/bash
# ═══════════════════════════════════════════════════════════════════════════
#  deploy.sh — Build the book and deploy to loperntu.github.io/mathling/
# ═══════════════════════════════════════════════════════════════════════════
#
#  Prerequisites:
#    1. Clone your GitHub Pages repo somewhere, e.g.:
#         git clone https://github.com/loperntu/loperntu.github.io.git ../loperntu.github.io
#    2. Set GITHUB_PAGES_REPO to that path, or pass it as the first argument.
#
#  Usage:
#    bash deploy.sh                          # uses $GITHUB_PAGES_REPO
#    bash deploy.sh /path/to/loperntu.github.io
#    bash deploy.sh --no-build /path/to/repo  # skip build, only copy & push
#
#  Result: https://loperntu.github.io/mathling/
#
# ═══════════════════════════════════════════════════════════════════════════

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

DO_BUILD=true
TARGET_REPO=""

for arg in "$@"; do
  if [[ "$arg" == --no-build ]]; then
    DO_BUILD=false
  elif [[ "$arg" != --* ]]; then
    TARGET_REPO="$arg"
    break
  fi
done

if [[ -z "$TARGET_REPO" ]]; then
  TARGET_REPO="${GITHUB_PAGES_REPO:-}"
fi

if [[ -z "$TARGET_REPO" || ! -d "$TARGET_REPO" ]]; then
  echo "Usage: bash deploy.sh [--no-build] /path/to/loperntu.github.io"
  echo ""
  echo "Or set once: export GITHUB_PAGES_REPO=/path/to/loperntu.github.io"
  echo "Then run:     bash deploy.sh"
  echo ""
  echo "To clone the repo first:"
  echo "  git clone https://github.com/loperntu/loperntu.github.io.git ../loperntu.github.io"
  exit 1
fi

TARGET_REPO="$(cd "$TARGET_REPO" && pwd)"
MATHLING="${TARGET_REPO}/mathling"

# ─── Build ─────────────────────────────────────────────────────────────
if [[ "$DO_BUILD" == true ]]; then
  echo "🔨 Building..."
  bash build.sh
  echo ""
fi

if [[ ! -f "geometry_of_grammar.html" ]]; then
  echo "❌ geometry_of_grammar.html not found. Run build.sh first."
  exit 1
fi

# ─── Deploy to mathling/ ───────────────────────────────────────────────
echo "📂 Deploying to $MATHLING ..."
mkdir -p "$MATHLING"
cp geometry_of_grammar.html "$MATHLING/index.html"
if [[ -d "figures" ]]; then
  mkdir -p "$MATHLING/figures"
  for f in figures/*; do [[ -e "$f" ]] && cp -r "$f" "$MATHLING/figures/"; done
fi
echo "   → mathling/index.html"
[[ -d figures ]] && echo "   → mathling/figures/"

# ─── Git commit & push ─────────────────────────────────────────────────
cd "$TARGET_REPO"
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
  echo "❌ Not a git repo: $TARGET_REPO"
  exit 1
fi

git add mathling/
if git diff --staged --quiet; then
  echo "   (no changes to commit)"
else
  git commit -m "Update mathling: The Geometry of Grammar"
  git push
  echo ""
  echo "✅ Deployed. View at: https://loperntu.github.io/mathling/"
fi
