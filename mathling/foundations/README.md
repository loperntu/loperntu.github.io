# 語言學的數學基礎

《語言的幾何》的附錄，也可以單獨當成一本圖解小書來讀。目錄在 [`index.html`](index.html)。

## 目錄

**第一部　語意的數學**

| 篇 | 中文 | English | 對照主書 |
|---|---|---|---|
| 1 | `語意學的邏輯基礎.dc.html` | `Logic for Formal Semantics.dc.html` | 第 3 章 |
| 2 | `語意學的圖論基礎.dc.html` | `Graph Theory for Semantics.dc.html` | 第 5、10 章 |
| 3 | `語意學的向量基礎.dc.html` | （尚未有英文版） | 第 7、9 章 |

邏輯篇另有可離線開啟的 `logic-standalone.html`。

**第二部　模型裡的數學**（建議順序：統計 → 微積分 → 線性代數 → 微分幾何）

| 篇 | 檔案 | 對照主書 |
|---|---|---|
| 4 | `LLM 統計學圖解.dc.html` | 第 6 章 |
| 5 | `LLM 微積分圖解.dc.html` | 第 8 章 |
| 6 | `LLM 線性代數圖解.dc.html` | 第 7、8 章 |
| 7 | `LLM 微分幾何圖解.dc.html` | 第 9、11 章 |

`LLM 的統計學.dc.html` 只是轉到第 4 篇的短連結。

**第三部　模型本身**

| 篇 | 檔案 | 對照主書 |
|---|---|---|
| 8 | `圖解學習指南：Transformer 與大型語言模型（全六章）.html` | 第 8 章 |

## 執行時需要的檔案

- `support.js`：各 `.dc.html` 的執行環境（從 CDN 載入 React）
- `fonts/lm.css`：第二部使用的 Latin Modern 字型
- `_ds/`：第一部共用的版面樣式

`work/` 是組裝模組時用的片段，閱讀時不需要。

## 發布

在上一層目錄執行 `bash publish.sh`，會把這個資料夾同步到 `docs/mathling/foundations/`（不含 `work/`）。
