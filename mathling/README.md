# The Geometry of Grammar — Source Files

## 📁 File Structure

```
├── book.md                    ← ✏️  你編輯這個檔案
├── template.html              ← 🎨 HTML/CSS 設計模板
├── build.py                   ← ⚙️  轉換引擎 (Python 3, 零依賴)
├── build.sh                   ← 🚀 一鍵建置腳本
├── index.html                 ← 📖 產出的網頁 (不要直接編輯)
├── deploy.sh                  ← 🚀 部署到 GitHub Pages 腳本
└── README.md                  ← 📋 本文件
```

## 🔨 使用方式

```bash
# 建置
python3 build.py

# 或用 shell script
bash build.sh

# macOS 建置後自動開啟瀏覽器
bash build.sh --open
```

## 🚀 部署到 GitHub Pages (loperntu.github.io/mathling/)

1. **自動偵測**：在 `mathling/` 目錄下執行時，若未傳入路徑且未設定 `GITHUB_PAGES_REPO`，腳本會自動偵測上一層目錄是否為 GitHub Pages 倉庫（含 `docs/` 或路徑名含 `github.io`），並以此為 deploy 目標。因此多數情況只需：
   ```bash
   bash deploy.sh
   ```

2. **手動指定路徑**（首次或 repo 不在上一層時）：
   ```bash
   bash deploy.sh ..
   # 或
   bash deploy.sh /path/to/loperntu.github.io
   # 或設定一次環境變數後可直接 bash deploy.sh
   export GITHUB_PAGES_REPO="/path/to/loperntu.github.io"
   ```

3. **只複製並推送**（不重新 build）：
   ```bash
   bash deploy.sh --no-build
   # 或 bash deploy.sh --no-build ..
   ```

4. **部署目標**：此站為 Quarto 網站，GitHub Pages 從 `docs/` 發布，故 deploy 會寫入 **`docs/mathling/`**（非 repo 根目錄的 `mathling/`）。推送成功後腳本會提示；網站更新約需 1–2 分鐘。

部署後書本網址：**https://loperntu.github.io/mathling/**

## ✏️ 編輯 book.md 的語法

### 基本結構

```markdown
---
title: "書名"
subtitle: "副標題"
date: "Draft — February 2026"
---

<!-- part: Part I · 離散基礎 -->     ← 側欄分組標籤

# Chapter 1. 章節標題 {#ch1}         ← 章節 (自動編號)
# 前言 {.unnumbered}                 ← 不編號的章節
# 附錄 A. 符號表 {#appendix .unnumbered}

### 1.1 小節標題                      ← 節標題

普通段落文字...
```

### 題詞 (Epigraph)

每章第一個 blockquote 自動變成題詞：

```markdown
> "引文內容"
> — 作者名
```

或明確標記：

```markdown
> "引文內容"
> — 作者名
{.epigraph}
```

### 例句

無標題：

```markdown
> *The bank by the river collapsed after the flood.*
{.example}
```

有標題（可選）：

```markdown
> *The bank by the river collapsed after the flood.*
{.example: Ambiguity Example}
```

例句區塊會以左對齊、圓角、較淡字色與不同字體顯示，且無邊框以與 deep-dive 區塊區分。

### 數學公式

行內：`$E = mc^2$`

獨立區塊：
```markdown
$$H(X) = -\sum_{x} P(x) \log_2 P(x)$$
```

支援所有 KaTeX LaTeX 語法：`\mathbb{R}`, `\langle`, `\rangle`, `\forall`, `\exists`, `\llbracket`, `\rrbracket` 等。

### 清單

```markdown
- **Every:** $\llbracket\text{every}\rrbracket(A)(B) = 1 \iff A \subseteq B$
- **Most:** $\llbracket\text{most}\rrbracket(A)(B) = 1 \iff |A \cap B| > |A \setminus B|$
```

### 行內格式

```markdown
**粗體**  *斜體*  `程式碼`
```

## 🎨 修改設計

編輯 `template.html` 頂部的 CSS variables：

```css
:root {
  --color-bg: #FDFBF7;         /* 背景色 */
  --color-accent: #8B4513;      /* 強調色 */
  --font-display: 'Cormorant Garamond', serif;  /* 標題字體 */
  --font-body: 'Source Sans 3', sans-serif;       /* 正文字體 */
  --content-max: 720px;         /* 內容最大寬度 */
  --nav-width: 300px;           /* 側欄寬度 */
}
```

## 📝 新增章節

1. 在 `book.md` 適當位置新增：

```markdown
# Chapter 14. 新章節標題 {#ch14}

> "題詞"
> — 作者

### 14.1 第一節

內容...
```

2. 執行 `python3 build.py`

側欄導覽會自動更新，不需要手動修改 HTML。

## ⚠️ 注意事項

- `build.py` 只需 Python 3.8+，**不需安裝任何套件**
- 數學公式由 KaTeX CDN 在瀏覽器端渲染，需要網路連線
- **產出檔為 `index.html`**（由 `build.sh` / `build.py` 自動產生），請勿直接編輯
- 所有內容修改都應在 `book.md` 中進行
- 若 deploy 時 `git push` 失敗，腳本會顯示錯誤；可手動於 repo 根目錄執行 `git push`
