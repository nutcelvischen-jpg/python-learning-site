---
title: "8.2 銷售儀表板"
---

<div class="lesson-header">
  <span class="chapter-tag">第 8 章 · 實戰專案</span>
  <h1>8.2 銷售儀表板</h1>
  <div class="meta">
    <span>⏱️ 120 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 整合運用</span>
  </div>
</div>

## 🎯 專案目標

做一個**互動式銷售儀表板**：

- 月營收趨勢
- 產品暢銷排行
- 地區分布
- KPI 卡片


## 💻 完整程式碼

```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

np.random.seed(42)
n = 1000
df = pd.DataFrame({
    "date": pd.date_range("2025-01-01", periods=n, freq="D"),
    "product": np.random.choice(["A", "B", "C"], n),
    "region": np.random.choice(["北", "中", "南", "東"], n),
    "quantity": np.random.randint(1, 20, n),
    "price": np.random.randint(100, 5000, n),
})
df["revenue"] = df["quantity"] * df["price"]

# 4 個子圖
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=("月營收趨勢", "產品營收占比", "地區分布", "單日分布")
)

# 1. 月趨勢
monthly = df.groupby(df["date"].dt.to_period("M"))["revenue"].sum()
fig.add_trace(
    go.Scatter(x=monthly.index.astype(str), y=monthly.values, mode="lines+markers"),
    row=1, col=1
)

# 2. 產品
prod = df.groupby("product")["revenue"].sum()
fig.add_trace(
    go.Pie(labels=prod.index, values=prod.values),
    row=1, col=2
)

# 3. 地區
reg = df.groupby("region")["revenue"].sum()
fig.add_trace(
    go.Bar(x=reg.index, y=reg.values),
    row=2, col=1
)

# 4. 單日直方圖
fig.add_trace(
    go.Histogram(x=df["revenue"], nbinsx=30),
    row=2, col=2
)

fig.update_layout(height=800, title_text="銷售儀表板", showlegend=False)
fig.show()
```


## 🚀 挑戰版

1. 加 KPI 卡（總營收、平均客單價、毛利率）
2. 加日期區間選擇
3. 串 Streamlit 做網頁版


