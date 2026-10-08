# Mathling Authoring Guide

This folder is the **source workspace** for Mathling (bilingual: English + 繁體中文).

- Edit here: `mathling/book.md` (EN), `mathling/book.zh.md` (中文), `mathling/template.html`
- Live website reads from: `docs/mathling/book.html` and `docs/mathling/book-zh.html`

If you only edit `mathling/` but do not publish to `docs/`, the website will not change.

## Folder Map

```text
mathling/
├── book.md                          # English source (edit this)
├── book.zh.md                       # Traditional Chinese source
├── template.html                    # HTML/CSS template (EN/中文 UI)
├── build.py                         # markdown -> html (both languages)
├── build.sh                         # convenience wrapper for build.py
├── publish.sh                       # build + sync to docs/mathling/
├── language_complexity_simulator.html
├── foundations/                     # Appendix primers (語言學的數學基礎)
├── figures/                         # images referenced by the book
├── temp/book.html                   # generated EN HTML
├── temp/book-zh.html                # generated 中文 HTML
├── REVISIONS.md                     # recent content/build notes
├── extras/                          # side materials (tutorials, backups)
├── archive/                         # older snapshots (do not publish)
└── README.md
```

## Quick Start (Recommended)

From `mathling/`:

```bash
bash publish.sh
```

This does:
1. `book.md` → `temp/book.html`
2. `book.zh.md` → `temp/book-zh.html`
3. Sync both (plus figures / simulator) → `docs/mathling/`

Then commit/push from repo root:

```bash
git add docs/mathling/book.html docs/mathling/book-zh.html
git commit -m "update mathling bilingual book"
git push origin main
```

## Build Only

```bash
cd mathling
python3 build.py
# outputs: temp/book.html + temp/book-zh.html
```

Optional:

```bash
bash build.sh --open
```

## Language Switch

The built pages include an EN / 中文 switch in the top bar.
Chapter and section ids (`#ch7`, `#sec-7-3`) match across languages, so switching keeps the reader in the same section.

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
#### Sub-heading

> "Quote"
> — Author
{.epigraph}

> *Example sentence*
{.example}

> Deep explanation block
{.deep-dive}

> Intuition / analogy
{.intuition}

$inline$ and $$display$$ math
```

## Troubleshooting

- **“Website didn’t update”**  
  Most likely `docs/mathling/book.html` / `book-zh.html` were not updated/committed.

- **“I can build, but style is broken”**  
  Ensure `docs/site_libs/` / `docs/site.css` are present (used by the landing page).

- **“Wrong output file”**  
  Default outputs are `temp/book.html` and `temp/book-zh.html`.

## Design Notes

The template is integrated with the main site style:
- top navigation + language switch
- book sidebar TOC
- responsive layout
- math rendering and long-form reading design
- Chinese typography via Noto Serif TC / Noto Sans TC
