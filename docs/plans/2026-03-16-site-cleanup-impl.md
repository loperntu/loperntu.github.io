# Site Cleanup & TOL Fix — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Remove all Quarto artifacts, convert 17 blog posts to new clean style, and fix `docs/tol/` 404 by renaming Unicode filenames.

**Architecture:** Two parallel lines in the same branch. Line 1 (cleanup + posts) uses a Python conversion script. Line 2 (TOL fix) renames three Chinese-named files in `docs/tol/` which are causing `upload-pages-artifact` to silently exclude the entire directory.

**Tech Stack:** Python 3 (BeautifulSoup4), git, GitHub Actions, pure HTML/CSS

---

## Line 1: Quarto Cleanup + Post Conversion

---

### Task 1: Delete orphaned Quarto files

**Files:**
- Delete: `docs/about.html`
- Delete: `docs/research.html`
- Delete: `docs/styles.css`
- Delete: `docs/listings.json`
- Delete: `docs/search.json`
- Delete: `docs/language_culture_handout.html` (already exists in `docs/tol/`)
- Delete: `docs/me_cartoonized.jpeg`
- Delete: `docs/site_libs/` (entire directory — safe to remove after posts are converted in Task 3)

**Step 1: Verify none of these files are referenced by new pages**

Run:
```bash
grep -r "about\.html\|research\.html\|styles\.css\|listings\.json\|search\.json\|me_cartoonized\|language_culture_handout" docs/index.html docs/cv.html docs/posts.html docs/tol/index.html
```
Expected: no output (no references in new pages)

**Step 2: Delete the files**

```bash
rm docs/about.html docs/research.html docs/styles.css docs/listings.json docs/search.json
rm docs/language_culture_handout.html docs/me_cartoonized.jpeg
rm -rf docs/site_libs/
```

**Step 3: Verify deletion**

```bash
ls docs/
```
Expected: `.nojekyll  cv.html  images/  index.html  me.png  plans/  posts/  posts.html  site.css  tol/`

**Step 4: Commit**

```bash
git add -A docs/
git commit -m "chore: remove all Quarto-generated artifacts from docs/"
```

---

### Task 2: Write the post conversion script

**Files:**
- Create: `scripts/convert_posts.py`

**Step 1: Check BeautifulSoup4 is available**

```bash
python3 -c "from bs4 import BeautifulSoup; print('ok')"
```
If not installed: `pip3 install beautifulsoup4`

**Step 2: Create `scripts/` directory and write the script**

```bash
mkdir -p scripts
```

Create `scripts/convert_posts.py` with this content:

```python
#!/usr/bin/env python3
"""
Convert Quarto-generated blog posts to clean HTML using site.css.
Usage: python3 scripts/convert_posts.py [--dry-run]
"""
import sys
import re
from pathlib import Path
from bs4 import BeautifulSoup

DRY_RUN = "--dry-run" in sys.argv

POST_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="icon" href="../../me.png" type="image/png">
  <link rel="stylesheet" href="../../site.css">
  <style>
    .post-nav {{ padding: 2rem 0 0; }}
    .post-nav a {{ font-size: 0.9rem; color: var(--accent); text-decoration: none; }}
    .post-nav a:hover {{ text-decoration: underline; }}
    article {{ max-width: 680px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }}
    article h1 {{ font-family: 'Noto Sans TC', sans-serif; font-size: 1.9rem; font-weight: 700; margin-bottom: 0.4rem; line-height: 1.3; }}
    .post-date {{ color: #999; font-size: 0.85rem; margin-bottom: 2.5rem; display: block; }}
    .post-body {{ font-family: 'Noto Serif TC', serif; line-height: 1.85; font-size: 1.05rem; }}
    .post-body h2 {{ font-family: 'Noto Sans TC', sans-serif; font-size: 1.3rem; margin-top: 2.5rem; }}
    .post-body h3 {{ font-family: 'Noto Sans TC', sans-serif; font-size: 1.1rem; margin-top: 2rem; }}
    .post-body blockquote {{ border-left: 3px solid #ddd; margin-left: 0; padding-left: 1.2rem; color: #666; }}
    .post-body code {{ background: #f5f5f5; padding: 0.1em 0.4em; border-radius: 3px; font-size: 0.9em; }}
    .post-body pre {{ background: #f5f5f5; padding: 1rem; border-radius: 6px; overflow-x: auto; }}
    .post-body img {{ max-width: 100%; border-radius: 4px; }}
    footer.post-footer {{ text-align: center; padding: 2rem; color: #bbb; font-size: 0.85rem; border-top: 1px solid #eee; }}
  </style>
</head>
<body>
  <div class="post-nav" style="max-width:680px;margin:0 auto;padding:1.5rem 1.5rem 0;">
    <a href="../../posts.html">← 返回文章列表</a>
  </div>
  <article>
    <h1>{title}</h1>
    <time class="post-date" datetime="{date}">{date}</time>
    <div class="post-body">
{body}
    </div>
  </article>
  <footer class="post-footer">謝舒凱 · <a href="../../index.html" style="color:#bbb;">loperntu.github.io</a></footer>
</body>
</html>
"""

def extract_title(soup):
    """Extract post title - try h1.title first, then <title> tag."""
    h1 = soup.find("h1", class_="title")
    if h1:
        return h1.get_text(strip=True)
    title_tag = soup.find("title")
    if title_tag:
        text = title_tag.get_text(strip=True)
        return re.sub(r"\s*[–—]\s*.*$", "", text).strip()
    return "Untitled"

def extract_date(soup):
    """Extract date from meta dcterms.date."""
    meta = soup.find("meta", attrs={"name": "dcterms.date"})
    if meta and meta.get("content"):
        return meta["content"]
    return ""

def extract_body(soup):
    """Extract main content from quarto-document-content, excluding appendix."""
    main = soup.find(id="quarto-document-content")
    if not main:
        main = soup.find("main")
    if not main:
        return "<p>（內容無法提取）</p>"
    # Remove appendix and citation sections
    for el in main.find_all(id=re.compile("quarto-appendix|quarto-margin|quarto-sidebar")):
        el.decompose()
    # Remove the banner title block (title/date already in template)
    for el in main.find_all(class_=re.compile("quarto-title|quarto-banner-title")):
        el.decompose()
    return main.decode_contents().strip()

def convert_post(path: Path, dry_run=False):
    html = path.read_text(encoding="utf-8")
    soup = BeautifulSoup(html, "html.parser")
    title = extract_title(soup)
    date = extract_date(soup)
    body = extract_body(soup)
    new_html = POST_TEMPLATE.format(title=title, date=date, body=body)
    if dry_run:
        print(f"[DRY RUN] Would convert: {path} (title={title!r}, date={date})")
        return
    path.write_text(new_html, encoding="utf-8")
    print(f"Converted: {path}")

def main():
    docs = Path("docs/posts")
    posts = sorted(docs.glob("*/index.html"))
    print(f"Found {len(posts)} posts")
    for p in posts:
        convert_post(p, dry_run=DRY_RUN)
    if not DRY_RUN:
        print(f"\nDone. {len(posts)} posts converted.")

if __name__ == "__main__":
    main()
```

**Step 3: Commit the script**

```bash
git add scripts/convert_posts.py
git commit -m "feat: add Quarto→clean HTML post conversion script"
```

---

### Task 3: Run conversion and verify output

**Step 1: Dry run first**

```bash
python3 scripts/convert_posts.py --dry-run
```
Expected: 17 lines like `[DRY RUN] Would convert: docs/posts/2026-03-05/index.html ...`

**Step 2: Convert one post manually to preview**

```bash
python3 -c "
from pathlib import Path
from bs4 import BeautifulSoup
import sys
sys.argv = ['']
exec(open('scripts/convert_posts.py').read().replace('def main():', 'def main_disabled():'))
convert_post(Path('docs/posts/2026-03-05/index.html'), dry_run=False)
"
```

Then visually inspect:
```bash
head -50 docs/posts/2026-03-05/index.html
```
Expected: Clean HTML with `<link rel="stylesheet" href="../../site.css">`, no Quarto references.

**Step 3: Run on all posts**

```bash
python3 scripts/convert_posts.py
```
Expected: `Found 17 posts` + 17 `Converted:` lines

**Step 4: Spot-check a few posts**

```bash
grep -l "quarto" docs/posts/*/index.html | wc -l
```
Expected: `0` (no Quarto references remain)

```bash
grep -c "site.css" docs/posts/*/index.html | grep -v ":1" | wc -l
```
Expected: `0` (all posts reference site.css exactly once)

**Step 5: Commit**

```bash
git add docs/posts/
git commit -m "feat: convert all 17 blog posts to clean HTML style"
```

---

## Line 2: TOL Deployment Fix

---

### Task 4: Rename Chinese-named files in docs/tol/

**Root cause confirmed:** Three files in `docs/tol/` have Unicode (Chinese) filenames. `actions/upload-pages-artifact@v3` silently excludes directories containing such files from the deployment artifact, causing all of `docs/tol/` to return 404.

**Files affected:**
- `docs/tol/語奧的發展與台灣的跨領域人才.html` → `docs/tol/tol-talent-development.html`
- `docs/tol/語言學奧賽升學制度化比較.pdf` → `docs/tol/tol-edu-comparison.pdf`
- `docs/tol/頂尖大學語言學科系調查.pdf` → `docs/tol/tol-university-survey.pdf`

**Step 1: Rename in git (preserves history)**

```bash
cd docs/tol
git mv "語奧的發展與台灣的跨領域人才.html" tol-talent-development.html
git mv "語言學奧賽升學制度化比較.pdf" tol-edu-comparison.pdf
git mv "頂尖大學語言學科系調查.pdf" tol-university-survey.pdf
cd ../..
```

**Step 2: Update any references in tol/index.html**

```bash
grep -n "語奧\|語言學奧賽\|頂尖大學" docs/tol/index.html
```
If matches found, update them:
```bash
sed -i '' 's|語奧的發展與台灣的跨領域人才\.html|tol-talent-development.html|g' docs/tol/index.html
sed -i '' 's|語言學奧賽升學制度化比較\.pdf|tol-edu-comparison.pdf|g' docs/tol/index.html
sed -i '' 's|頂尖大學語言學科系調查\.pdf|tol-university-survey.pdf|g' docs/tol/index.html
```

**Step 3: Verify no remaining Chinese filenames in docs/**

```bash
git ls-files docs/ | python3 -c "
import sys
for line in sys.stdin:
    line = line.strip()
    if any(ord(c) > 127 for c in line):
        print('UNICODE FILENAME:', line)
"
```
Expected: no output (or only non-tol files if any)

**Step 4: Commit**

```bash
git add docs/tol/
git commit -m "fix: rename Unicode filenames in docs/tol/ to fix GitHub Pages deployment"
```

---

### Task 5: Add workflow debug + push to verify

**Files:**
- Modify: `.github/workflows/deploy-pages.yml`

**Step 1: Add debug step to workflow**

Open `.github/workflows/deploy-pages.yml` and add after the checkout step:

```yaml
      - name: Debug - list tol directory
        run: |
          echo "=== docs/tol/ contents ==="
          ls -la docs/tol/ || echo "docs/tol/ not found"
          echo "=== total files in docs/ ==="
          find docs/ -type f | wc -l
```

**Step 2: Commit and push**

```bash
git add .github/workflows/deploy-pages.yml
git commit -m "ci: add tol debug output to verify artifact contents"
git push origin main
```

**Step 3: Wait ~2 minutes then verify**

```bash
curl -s -o /dev/null -w "%{http_code}" https://loperntu.github.io/tol/index.html
echo " tol/index.html"
curl -s -o /dev/null -w "%{http_code}" https://loperntu.github.io/tol/morphology_handout.html
echo " morphology_handout.html"
```
Expected: `200` for both

**Step 4: If still 404 — fallback to artifact v2**

Edit `.github/workflows/deploy-pages.yml`:
Change `actions/upload-pages-artifact@v3` to `actions/upload-pages-artifact@v2`

```bash
git add .github/workflows/deploy-pages.yml
git commit -m "fix: downgrade upload-pages-artifact to v2 for unicode compatibility"
git push origin main
```

---

## Final: Cleanup and Verify

### Task 6: End-to-end smoke test

```bash
# Check all key pages return 200
for url in "" "posts.html" "cv.html" "tol/index.html" "tol/morphology_handout.html" "posts/2026-03-05/index.html" "posts/2026-01-29/index.html"; do
  code=$(curl -s -o /dev/null -w "%{http_code}" "https://loperntu.github.io/$url")
  echo "$code  $url"
done
```
Expected: all `200`

```bash
# Confirm no Quarto JS loaded on any page
curl -s https://loperntu.github.io/posts/2026-03-05/index.html | grep -c "quarto"
```
Expected: `0`

```bash
# Confirm site_libs is gone
curl -s -o /dev/null -w "%{http_code}" https://loperntu.github.io/site_libs/quarto-nav/quarto-nav.js
```
Expected: `404`
