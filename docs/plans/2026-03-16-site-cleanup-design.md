# Site Cleanup & TOL Fix — Design Doc
**Date:** 2026-03-16
**Approach:** B — Parallel (cleanup + post conversion // TOL debug)

---

## Goal
Remove all Quarto-generated artifacts from `docs/`, convert blog posts to new clean style, and fix the `docs/tol/` 404 deployment issue.

---

## Section 1: Quarto Cleanup

### Files to delete from `docs/`
| File/Dir | Reason |
|---|---|
| `about.html` | Orphaned page, content absorbed into `index.html` |
| `research.html` | Orphaned page, not linked from nav |
| `styles.css` | Old Quarto CSS, replaced by `site.css` |
| `listings.json` | Quarto listing data, unused |
| `search.json` | Quarto search index, unused |
| `language_culture_handout.html` | Misplaced in root; already exists in `tol/` |
| `site_libs/` | All Quarto JS/CSS — removable after posts are converted |
| `me_cartoonized.jpeg` | Old avatar, new site uses `me.png` only |

### Files to keep
`index.html`, `cv.html`, `posts.html`, `site.css`, `me.png`, `.nojekyll`, `images/`, `posts/`, `tol/`

---

## Section 2: Blog Post Auto-Conversion

### Script: `scripts/convert_posts.py`
- Input: each `docs/posts/*/index.html`
- Extraction via BeautifulSoup:
  - Title from `<title>` or `<h1 class="title">`
  - Date from `<meta name="dcterms.date">`
  - Body from `<div id="quarto-content">` or `<main>`
- Output: same file path, new clean HTML

### New post template structure
```
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <link rel="stylesheet" href="../../site.css">
</head>
<body>
  <nav> ← 返回文章列表 </nav>
  <article>
    <h1>標題 (黑體, 2rem)</h1>
    <time>日期 (淡灰小字)</time>
    <div class="post-body"> 正文 (Noto Serif TC, 1.8 line-height, max-width 680px) </div>
  </article>
  <footer> 簡潔頁尾 </footer>
</body>
</html>
```

### After conversion
`site_libs/` can be fully removed (no posts will reference it).

---

## Section 3: TOL Deployment Fix

### Root cause hypothesis
`actions/upload-pages-artifact@v3` silently excludes or fails on directories containing Unicode filenames, causing the entire `docs/tol/` tree to be omitted from the deployment artifact.

Evidence:
- `docs/tol/` exists in git (raw.githubusercontent.com returns 200)
- `docs/mathling/` also 404 — both are recently-added directories
- `docs/posts/` (pre-existing) works fine
- Three Chinese-named files in `docs/tol/`:
  - `語奧的發展與台灣的跨領域人才.html`
  - `語言學奧賽升學制度化比較.pdf`
  - `頂尖大學語言學科系調查.pdf`

### Fix steps
1. Rename Chinese filenames to ASCII equivalents in `tol/`
2. Update all references in `tol/index.html`
3. Add `ls -la docs/tol/` to workflow for artifact verification
4. Push and verify live

### Fallback
If still 404 after renaming: downgrade to `actions/upload-pages-artifact@v2`.

---

## Parallel Execution Plan
- **Line 1:** Quarto cleanup → post conversion (script-driven, bulk)
- **Line 2:** TOL filename rename + workflow fix
- **Merge:** Single PR combining both lines once verified
