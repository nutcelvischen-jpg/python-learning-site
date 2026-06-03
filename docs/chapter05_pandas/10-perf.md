---
title: "5.10 效能優化"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.10 效能優化</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- vectorization
- query / eval
- 避免 Python 迴圈


## ⚡ 向量化

```python
# 慢：用 apply
df["price_x2"] = df["price"].apply(lambda x: x * 2)

# 快：向量化
df["price_x2"] = df["price"] * 2
```


## 🔍 query / eval

```python
# query（可讀性高）
adults = df.query("age >= 18 and city == '台中'")

# eval（算術表達式）
df.eval("total = price * quantity", inplace=True)
```


## ✏️ 練習題

1. 用向量化算 AQI 跟 PM2.5 的比值
2. 用 query 過濾 AQI > 100 的測站


