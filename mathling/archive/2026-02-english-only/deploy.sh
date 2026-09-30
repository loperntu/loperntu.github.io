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

# Auto-detect: if we're inside mathling/ and parent is a git repo, use it
if [[ -z "$TARGET_REPO" || ! -d "$TARGET_REPO" ]]; then
  PARENT="$(cd "$SCRIPT_DIR/.." && pwd)"
  if [[ -d "$PARENT/.git" ]] && { [[ -d "$PARENT/docs" ]] || [[ "$(basename "$PARENT")" == *github.io* ]]; }; then
    TARGET_REPO="$PARENT"
  fi
fi

if [[ -z "$TARGET_REPO" || ! -d "$TARGET_REPO" ]]; then
  echo "Usage: bash deploy.sh [--no-build] /path/to/loperntu.github.io"
  echo ""
  echo "Or set once: export GITHUB_PAGES_REPO=/path/to/loperntu.github.io"
  echo "Or run from mathling/ with repo one level up:  bash deploy.sh .."
  echo ""
  echo "To clone the repo first:"
  echo "  git clone https://github.com/loperntu/loperntu.github.io.git ../loperntu.github.io"
  exit 1
fi

TARGET_REPO="$(cd "$TARGET_REPO" && pwd)"
# GitHub Pages for this repo serves from docs/ (Quarto output-dir), so deploy there
if [[ -d "${TARGET_REPO}/docs" ]]; then
  MATHLING="${TARGET_REPO}/docs/mathling"
else
  MATHLING="${TARGET_REPO}/mathling"
fi

# ─── Build ─────────────────────────────────────────────────────────────
if [[ "$DO_BUILD" == true ]]; then
  echo "🔨 Building..."
  bash build.sh
  echo ""
fi

if [[ ! -f "index.html" ]]; then
  echo "❌ index.html not found. Run build.sh first."
  exit 1
fi

# ─── Deploy to mathling/ (under repo root or docs/) ─────────────────────
echo "📂 Deploying to $MATHLING ..."
mkdir -p "$MATHLING"
cp index.html "$MATHLING/index.html"
if [[ -d "figures" ]]; then
  mkdir -p "$MATHLING/figures"
  for f in figures/*; do [[ -e "$f" ]] && cp -r "$f" "$MATHLING/figures/"; done
fi
echo "   → $MATHLING/index.html"
[[ -d figures ]] && echo "   → $MATHLING/figures/"

# ─── Git commit & push ─────────────────────────────────────────────────
cd "$TARGET_REPO"
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
  echo "❌ Not a git repo: $TARGET_REPO"
  exit 1
fi

# Stage the folder we wrote to (docs/mathling or mathling)
REL_MATHLING="${MATHLING#${TARGET_REPO}/}"
git add "$REL_MATHLING"
if git diff --staged --quiet; then
  echo "   (no changes to commit)"
else
  git commit -m "Update mathling: The Geometry of Grammar"
  echo "📤 Pushing to GitHub..."
  if git push; then
    echo ""
    echo "✅ Deployed successfully!"
    echo "   View at: https://loperntu.github.io/mathling/"
    echo "   (GitHub Pages may take 1-2 minutes to update)"
  else
    echo ""
    echo "❌ Push failed! Please check your git credentials and try:"
    echo "   cd $TARGET_REPO && git push"
    exit 1
  fi
fi
