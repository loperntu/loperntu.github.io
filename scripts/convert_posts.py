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
