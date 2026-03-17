# loperntu.github.io

謝舒凱的個人網站，純手工 HTML + CSS，由 GitHub Pages 從 `docs/` 自動發布。

**網址：** https://loperntu.github.io

---

## 網站結構

```
docs/
├── index.html          # 首頁
├── cv.html             # CV
├── posts.html          # Blog 列表
├── site.css            # 全站樣式
├── .nojekyll           # 停用 Jekyll 處理
├── posts/              # Blog 貼文（每篇一個子資料夾）
│   └── YYYY-MM-DD/
│       └── index.html
├── iol/                # 台灣語言奧林匹亞（IOL）相關頁面
└── images/             # 圖片資源
```

---

## 更新網站

**直接編輯 `docs/` 裡的檔案，然後 push 即可。**

```bash
# 1. 編輯任何 docs/ 底下的檔案
# 2. 提交並推送
git add docs/<檔案>
git commit -m "說明"
git push origin main
```

GitHub Pages 偵測到新 push 後，約 **3 分鐘**內自動部署。不需要執行任何 build 工具或 workflow。

---

## 常見操作

| 想做什麼 | 編輯的檔案 |
|---|---|
| 改首頁內容 | `docs/index.html` |
| 更新 CV | `docs/cv.html` |
| 新增 blog 貼文 | 用 `scripts/md2post.py` 轉換（見下方） |
| 更新 Blog 列表 | `docs/posts.html`（手動加一列） |
| 改 IOL 頁面 | `docs/iol/` 裡對應的 html |
| 改全站字型 / 顏色 | `docs/site.css` |

---

## 新增 Blog 貼文（Markdown 工作流程）

用 Markdown 寫作，一行指令轉成符合網站風格的 HTML。

**1. 建立 Markdown 檔**（放在任何地方，例如 `posts/`）

```
posts/2026-03-20-my-post.md
```

**2. 填入 frontmatter + 正文**

```markdown
---
title: 文章標題
date: 2026-03-20
category: Life
description: 一行摘要（用於 posts.html 列表）
math: false        # 有 LaTeX 數學就改成 true
---

## 小節標題

正文，支援 **粗體**、*斜體*、`code`、表格、引言、圍欄程式碼區塊。
```

**3. 轉換**

```bash
python scripts/md2post.py posts/2026-03-20-my-post.md
# → 輸出 docs/posts/2026-03-20/index.html
```

**4. 更新 Blog 列表，然後 push**

在 `docs/posts.html` 的 `<div class="post-list">` 裡手動加一列：

```html
<div class="post-item" data-cats="Life">
  <div class="post-meta">
    <span class="post-date">2026-03-20</span>
    <span class="tag">Life</span>
  </div>
  <div class="post-content">
    <a class="post-title" href="posts/2026-03-20/index.html">文章標題</a>
    <p class="post-desc">一行摘要</p>
  </div>
</div>
```

```bash
git add docs/posts/2026-03-20/ docs/posts.html
git commit -m "post: 文章標題"
git push origin main
```

> `category` 可用值：`Quantum Semantics` / `LLM and Linguistics` / `Geometry of Language` / `Emergence` / `Humanities and AI` / `Life`

---

## 注意事項

- **不使用 Quarto**：網站已於 2026-03 從 Quarto 遷移為純 HTML。請勿執行 `quarto render`。
- **路徑 `/tol/` 已廢棄**：舊路徑因 GitHub Pages 快取鎖死問題無法修復，現改用 `/iol/`。
- **字型**：標題用 Noto Sans TC，內文用 Noto Serif TC，由 Google Fonts CDN 載入。
- **數學渲染**：使用 MathJax 3，支援 `\(...\)` inline 與 `\[...\]` display 語法。**只有含數學的貼文需要加載**，在 `<head>` 加入：

  ```html
  <script>
  MathJax = {
    tex: {
      inlineMath: [["$","$"],["\\(","\\)"]],
      displayMath: [["$$","$$"],["\\[","\\]"]]
    }
  };
  </script>
  <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
  ```

  目前含數學的貼文：`posts/2025-01-13/`、`posts/2026-03-05/`

---

**簡記：改 `docs/` → `git commit` → `git push`**
