# loperntu.github.io

Personal website (Quarto), 輸出到 `docs/`，由 GitHub Pages 發布。

---

## 如何更新網站

### 1. 修改內容

編輯要改的檔案（例如 `posts/2026-03-05/index.qmd`、首頁、about 等）。

### 2. 在本機渲染網站

在專案根目錄執行：

```bash
quarto render
```

會把整個網站重新產生到 `docs/`。

若要先預覽再決定是否更新：

```bash
quarto preview
```

### 3. 推上 GitHub 完成更新

將改動（含新的 `docs/`）提交並推送：

```bash
git add .
git commit -m "更新內容說明"
git push
```

推送後 GitHub Pages 會自動用最新的 `docs/` 更新網站。

---

**簡記：改檔 → `quarto render` → `git add` / `git commit` / `git push`**
