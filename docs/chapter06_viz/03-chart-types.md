---
title: "6.3 圖表類型"
---

<div class="lesson-header">
  <span class="chapter-tag">第 6 章 · 視覺化</span>
  <h1>6.3 圖表類型</h1>
  <div class="meta">
    <span>⏱️ 35 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 8 種基本圖表
- 怎麼選


## 📊 圖表速查

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
vals = [3, 7, 2, 5, 8]

fig, axes = plt.subplots(2, 4, figsize=(16, 8))

# 1. Line
axes[0, 0].plot(x, vals)
axes[0, 0].set_title("Line")

# 2. Bar
axes[0, 1].bar(x, vals)
axes[0, 1].set_title("Bar")

# 3. Scatter
axes[0, 2].scatter(np.random.rand(20), np.random.rand(20))
axes[0, 2].set_title("Scatter")

# 4. Hist
axes[0, 3].hist(np.random.randn(1000), bins=30)
axes[0, 3].set_title("Histogram")

# 5. Box
axes[1, 0].boxplot([np.random.randn(100) for _ in range(5)])
axes[1, 0].set_title("Box")

# 6. Pie
axes[1, 1].pie(vals, labels=list("ABCDE"), autopct='%1.1f%%')
axes[1, 1].set_title("Pie")

# 7. Area
axes[1, 2].fill_between(x, vals, alpha=0.5)
axes[1, 2].set_title("Area")

# 8. Step
axes[1, 3].step(x, vals)
axes[1, 3].set_title("Step")

plt.tight_layout()
plt.show()
```


## 🤔 怎麼選圖表

| 想看什麼 | 用什麼圖 |
|---|---|
| 趨勢（隨時間） | Line |
| 比較類別 | Bar |
| 兩變數關係 | Scatter |
| 分布 | Histogram / Box |
| 占比 | Pie（謹慎） |
| 部分佔整體 | Stacked Bar |
| 地理 | Map / Choropleth |


## ✏️ 練習題

1. 用 AQI 資料畫 5 個縣市 AQI 比較 bar
2. 畫 AQI 分布 histogram
3. 試試 pie 圖的限制


