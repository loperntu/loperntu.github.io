# Mathling Authoring Guide

This folder is the **source workspace** for Mathling.

- Write and edit here: `mathling/book.md`, `mathling/template.html`
- Live website reads from: `docs/mathling/book.html`

If you only edit `mathling/` but do not publish to `docs/`, the website will not change.

## Folder Map

```text
mathling/
├── book.md               # source content (edit this)
├── template.html         # HTML/CSS template
├── build.py              # markdown -> html converter
├── build.sh              # convenience wrapper for build.py
├── publish.sh            # build + sync to docs/mathling/book.html
├── temp/book.html        # default build output (generated)
└── README.md
```

## Quick Start (Recommended)

From `mathling/`:

```bash
bash publish.sh
```

This does:
1. `book.md` -> `temp/book.html`
2. `temp/book.html` -> `docs/mathling/book.html`

Then commit/push from repo root:

```bash
git add docs/mathling/book.html
git commit -m "update mathling book"
git push origin main
```

## Build Only

```bash
cd mathling
python3 build.py
# default output: temp/book.html
```

Optional:

```bash
bash build.sh --open
```

## Markdown Conventions

```markdown
---
title: "The Geometry of Grammar"
subtitle: "A Mathematical Journey Through Language"
author: "SHUKAI HSIEH"
date: "Draft — February 2026"
---

<!-- part: Part I · Discrete Foundations -->
# Chapter 1. Title {#ch1}
# Preface {.unnumbered}
### 1.1 Section

> "Quote"
> — Author
{.epigraph}

> *Example sentence*
{.example}

> Deep explanation block
{.deep-dive}

$inline$ and $$display$$ math
```

## Troubleshooting

- **“Website didn’t update”**  
  Most likely `docs/mathling/book.html` was not updated/committed.

- **“I can build, but style is broken”**  
  Ensure `docs/site_libs/` is present and committed (used by `docs/mathling/book.html`).

- **“Wrong output file”**  
  Current default output is `temp/book.html` (not `geometry_of_grammar.html`).

## Design Notes

The template is integrated with the main site style:
- top navigation
- book sidebar TOC
- responsive layout
- math rendering and long-form reading design
