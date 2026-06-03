---
title: "6.7 plotly 互動"
---

<div class="lesson-header">
  <span class="chapter-tag">第 6 章 · 視覺化</span>
  <h1>6.7 plotly 互動</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 互動式圖表
- plotly express
- 存成 HTML


## 🎮 為什麼用 plotly

matplotlib 是**靜態**圖表（PNG），plotly 是**互動**（hover / zoom / pan）。 網頁上必備。


## 💫 快速上手

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "x": [1, 2, 3, 4, 5],
    "y": [1, 4, 9, 16, 25]
})

fig = px.line(df, x="x", y="y", title="平方數")
fig.show()
fig.write_html("plot.html")
```


## 📊 真實範例

```python
# 用 AQI 資料
fig = px.scatter(
    air, x="longitude", y="latitude",
    color="aqi", size="pm2_5",
    hover_name="sitename",
    color_continuous_scale="RdYlGn_r",
    title="全台 AQI 分佈"
)
fig.show()
```


## ✏️ 練習題

1. 用 plotly 畫 AQI 散佈圖
2. 存成 HTML


