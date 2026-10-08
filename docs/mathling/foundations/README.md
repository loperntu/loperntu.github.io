# Mathematical Foundations of Linguistics / 語言學的數學基礎

Interactive primers that accompany the Mathling book appendix.

## Modules

| Topic | English | 中文 |
|---|---|---|
| Logic for formal semantics | `Logic for Formal Semantics.dc.html` | `形式語義學的邏輯基礎.dc.html` |
| Graph theory for semantics | `Graph Theory for Semantics.dc.html` | `語意學的圖論基礎.dc.html` |
| Vector foundations for semantics | *(in preparation)* | `語意學的向量基礎.dc.html` |

Also available: `Logic for Formal Semantics (standalone).html` (self-contained bundle).

## Runtime files

- `support.js` — DC runtime (loads React from CDN)
- `_ds/` — shared styles / design-system stubs
- `work/` — source fragments used to assemble modules (not required at runtime)

## Publishing

`bash ../publish.sh` syncs this folder to `docs/mathling/foundations/`
(excluding `work/` and any local uploads).
