---
title: "6.8 發表品質"
---

<div class="lesson-header">
  <span class="chapter-tag">第 6 章 · 視覺化</span>
  <h1>6.8 發表品質</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 解析度
- 格式選擇
- 期刊投稿要求


## 🖼️ 解析度

```python
# 螢幕 72-100 dpi
# 海報 300 dpi
# 期刊通常要求 300 dpi

fig.savefig("output.png", dpi=300, bbox_inches="tight")
```


## 📁 格式選擇

| 格式 | 用途 | 優點 |
|---|---|---|
| PNG | 網頁 / 簡報 | 無損、透明背景 |
| JPG | 照片 | 檔案小 |
| SVG | 期刊 / 海報 | 矢量、無限放大 |
| PDF | 論文 | 矢量、LaTeX 友好 |


## ✏️ 練習題

1. 把一張圖存成 PNG 跟 SVG
2. 比較檔案大小


