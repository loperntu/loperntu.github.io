# The Geometry of Grammar — Source Files

## 📁 File Structure

```
├── book.md                    ← ✏️  你編輯這個檔案
├── template.html              ← 🎨 HTML/CSS 模板（含網站導覽列）
├── build.py                   ← ⚙️  轉換引擎 (Python 3, 零依賴)
├── build.sh                   ← 🚀 一鍵建置
├── temp/book.html             ← 📖 預設產出網頁 (勿直接編輯)
└── README.md
```

## 🔨 建置

```bash
python3 build.py          # 預設: book.md → temp/book.html
bash build.sh --open      # 建置並開啟瀏覽器 (macOS)
```

## 🎨 設計

與 [loperntu.github.io](https://loperntu.github.io/) 整合：

- **頂部導覽列** — 深灰 `#343a40`，含 Home / Blog / CV / TOL / Book
- **書本側欄** — 暖棕 `#2B2B2B`，Cormorant Garamond 書名，自動追蹤閱讀位置
- **內文** — 學術書籍排版，暖米色背景，KaTeX 數學公式
- **封面動畫** / **進度條** / **Back-to-top** / **響應式** / **列印友善**

## ✏️ Markdown 語法

```markdown
---
title: "The Geometry of Grammar"
subtitle: "A Mathematical Journey Through Language"
author: "SHUKAI HSIEH"
date: "Draft — February 2026"
---

<!-- part: Part I · Discrete Foundations -->
# Chapter 1. Title {#ch1}         ← 章節
# Preface {.unnumbered}           ← 不編號章節
### 1.1 Section                    ← 小節

> "Quote" \n> — Author            ← 題詞（每章首個 blockquote 自動）
{.epigraph}

> *Example sentence*              ← 例句
{.example}

> 深入說明...                      ← 深入區塊
{.deep-dive}

$inline$  $$display$$             ← KaTeX 數學
```python                         ← 程式碼
code here
```
![alt](url)                       ← 圖片
```

## 🚀 部署

將 `temp/book.html` 複製到 `docs/mathling/book.html` 後 commit/push 即可上線。
