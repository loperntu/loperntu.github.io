# loperntu.github.io

謝舒凱的個人網站。  
目前採用 **手動維護 `docs/` 靜態檔案**，由 GitHub Pages 直接發布。

- Site: https://loperntu.github.io
- Deploy source: `main` branch + `docs/` folder

---

## Repository layout

```text
docs/                     # 真正上線內容（網站根目錄）
├── index.html            # Home
├── cv.html               # CV
├── posts.html            # Blog list
├── site.css              # Site-wide styles
├── posts/YYYY-MM-DD/     # Blog posts (HTML)
├── mathling/             # Mathling published pages
├── tol/                  # TOL pages
└── images/               # Static assets

mathling/                 # Mathling source workspace (authoring)
├── book.md               # source text
├── template.html         # template
├── build.py / build.sh   # local build tools
└── README.md             # Mathling-specific guide
```

---

## Golden rule

- **Edit for deployment:** `docs/`
- **Edit for Mathling authoring:** `mathling/`
- **Publish step for Mathling:** copy generated HTML into `docs/mathling/`

In short: `mathling/` is source, `docs/mathling/` is live output.

---

## Basic deploy flow

```bash
git add docs/<changed-files>
git commit -m "update site content"
git push origin main
```

Usually visible in 1–3 minutes after push.

---

## Common edit targets

| Task | File(s) |
|---|---|
| Update homepage | `docs/index.html` |
| Update CV | `docs/cv.html` |
| Update post index cards | `docs/posts.html` |
| Add/edit post page | `docs/posts/YYYY-MM-DD/index.html` |
| Update TOL pages | `docs/tol/*.html` |
| Update Mathling landing page | `docs/mathling/index.html` |
| Update Mathling book (live) | `docs/mathling/book.html` |

---

## Blog post workflow (Markdown -> HTML)

1. Write a Markdown file (example path):

```text
posts/2026-03-20-my-post.md
```

2. Convert with helper script:

```bash
python scripts/md2post.py posts/2026-03-20-my-post.md
# output: docs/posts/2026-03-20/index.html
```

3. Add card entry in `docs/posts.html`.
4. Commit and push `docs/posts/...` + `docs/posts.html`.

---

## Mathling workflow

1. Edit source in `mathling/`:
   - `mathling/book.md`
   - `mathling/template.html` (if needed)
2. Build locally:

```bash
cd mathling
python3 build.py
```

3. Copy generated page to live path:

```bash
cp mathling/temp/book.html docs/mathling/book.html
```

Or use one command:

```bash
cd mathling
bash publish.sh
```

4. Commit/push deployed file:

```bash
git add docs/mathling/book.html
git commit -m "update mathling book"
git push origin main
```

---

## Notes

- This repo no longer uses Quarto build/deploy for the main site.
- Avoid committing local/editor artifacts:
  - `.claude/`
  - `.DS_Store`
  - `.Rhistory`
  - `*.Rproj` / `.Rproj.user/`
- If a page seems not updated, check that you changed the file under `docs/` (not only under source folders).
