#!/usr/bin/env python3
"""
md2post.py — 將 Markdown 貼文轉成網站 HTML

用法：
  python scripts/md2post.py <markdown檔>

範例：
  python scripts/md2post.py posts/2026-03-20-my-post.md

Markdown 檔需有 YAML frontmatter：
  ---
  title: 文章標題
  date: 2026-03-20
  category: Life
  description: 短描述（選填）
  math: false       # true 則載入 MathJax
  ---

輸出：docs/posts/YYYY-MM-DD/index.html
"""

import sys
import re
from pathlib import Path
import markdown as md_lib

# ── 路徑設定 ──────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent
DOCS_POSTS = ROOT / "docs" / "posts"

# ── HTML 模板 ─────────────────────────────────────────────────────────────────
MATHJAX_SNIPPET = """\
  <!-- MathJax 3 -->
  <script>
  MathJax = {
    tex: {
      inlineMath: [["$","$"],["\\\\(","\\\\)"]],
      displayMath: [["$$","$$"],["\\\\[","\\\\]"]]
    }
  };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>"""

POST_TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-TW">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>__TITLE__</title>
  <link rel="icon" href="../../me.png" type="image/png">
  <link rel="stylesheet" href="../../site.css">
  <style>
    .post-nav { padding: 2rem 0 0; }
    .post-nav a { font-size: 0.9rem; color: var(--accent); text-decoration: none; }
    .post-nav a:hover { text-decoration: underline; }
    article { max-width: 680px; margin: 0 auto; padding: 2rem 1.5rem 4rem; }
    article h1 { font-family: 'Noto Sans TC', sans-serif; font-size: 1.9rem; font-weight: 700; margin-bottom: 0.4rem; line-height: 1.3; }
    .post-date { color: #999; font-size: 0.85rem; margin-bottom: 2.5rem; display: block; }
    .post-body { font-family: 'Noto Serif TC', serif; line-height: 1.85; font-size: 1.05rem; }
    .post-body h2 { font-family: 'Noto Sans TC', sans-serif; font-size: 1.3rem; margin-top: 2.5rem; }
    .post-body h3 { font-family: 'Noto Sans TC', sans-serif; font-size: 1.1rem; margin-top: 2rem; }
    .post-body blockquote { border-left: 3px solid #ddd; margin-left: 0; padding-left: 1.2rem; color: #666; }
    .post-body code { background: #f5f5f5; padding: 0.1em 0.4em; border-radius: 3px; font-size: 0.9em; }
    .post-body pre { background: #f5f5f5; padding: 1rem; border-radius: 6px; overflow-x: auto; }
    .post-body img { max-width: 100%; border-radius: 4px; }
    .post-body table { border-collapse: collapse; width: 100%; margin: 1.5rem 0; }
    .post-body th, .post-body td { border: 1px solid #ddd; padding: 0.6rem 0.8rem; font-size: 0.95rem; }
    .post-body th { background: #f8f8f8; font-family: 'Noto Sans TC', sans-serif; }
    footer.post-footer { text-align: center; padding: 2rem; color: #bbb; font-size: 0.85rem; border-top: 1px solid #eee; }
  </style>
__MATHJAX__
</head>
<body>
  <div class="post-nav" style="max-width:680px;margin:0 auto;padding:1.5rem 1.5rem 0;">
    <a href="../../posts.html">← 返回文章列表</a>
  </div>
  <article>
    <h1>__TITLE__</h1>
    <time class="post-date" datetime="__DATE__">__DATE__</time>
    <div class="post-body">
__BODY__
    </div>
  </article>
  <footer class="post-footer">謝舒凱 · loperntu.github.io</footer>
</body>
</html>
"""

# ── Frontmatter 解析 ──────────────────────────────────────────────────────────
def parse_frontmatter(text):
    """分離 YAML frontmatter 與正文，回傳 (meta dict, body str)"""
    if not text.startswith("---"):
        return {}, text

    end = text.find("\n---", 3)
    if end == -1:
        return {}, text

    raw_fm = text[3:end].strip()
    body = text[end + 4:].lstrip("\n")

    meta = {}
    for line in raw_fm.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()

    return meta, body

# ── 主程式 ────────────────────────────────────────────────────────────────────
def convert(md_path_str):
    md_path = Path(md_path_str)
    if not md_path.exists():
        print(f"找不到檔案：{md_path}")
        sys.exit(1)

    text = md_path.read_text(encoding="utf-8")
    meta, body_md = parse_frontmatter(text)

    # 必要欄位
    title = meta.get("title", md_path.stem)
    date  = meta.get("date", "")
    use_math = meta.get("math", "false").lower() == "true"

    # 從檔名或 date 取得資料夾名稱 (YYYY-MM-DD)
    stem = md_path.stem  # e.g. "2026-03-20-my-post" or "my-post"
    date_match = re.match(r"(\d{4}-\d{2}-\d{2})", stem)
    folder_date = date_match.group(1) if date_match else (date or stem)

    # 轉換 Markdown → HTML
    body_html = md_lib.markdown(
        body_md,
        extensions=["fenced_code", "tables", "footnotes", "toc"]
    )

    # 填入模板
    mathjax_block = MATHJAX_SNIPPET if use_math else ""
    html = (POST_TEMPLATE
            .replace("__TITLE__",   title)
            .replace("__DATE__",    date or folder_date)
            .replace("__MATHJAX__", mathjax_block)
            .replace("__BODY__",    body_html))

    # 輸出
    out_dir = DOCS_POSTS / folder_date
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "index.html"
    out_file.write_text(html, encoding="utf-8")

    print(f"✓ 輸出：{out_file.relative_to(ROOT)}")
    print(f"  標題：{title}")
    print(f"  日期：{date or folder_date}")
    print(f"  數學：{'是 (MathJax)' if use_math else '否'}")
    print()
    print("下一步：")
    print(f"  git add {out_file.relative_to(ROOT)}")
    print(f"  git commit -m \"post: {title}\"")
    print(f"  git push origin main")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)
    convert(sys.argv[1])
