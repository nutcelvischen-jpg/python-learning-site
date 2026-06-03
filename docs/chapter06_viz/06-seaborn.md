---
title: "6.6 seaborn 進階"
---

<div class="lesson-header">
  <span class="chapter-tag">第 6 章 · 視覺化</span>
  <h1>6.6 seaborn 進階</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- seaborn 美化
- heatmap / pairplot / violinplot


## 🌊 seaborn 是什麼

```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 內建資料集練習
df = sns.load_dataset("tips")
print(df.head())
```


## 🔥 heatmap

```python
import numpy as np

data = np.random.rand(8, 6)
sns.heatmap(data, annot=True, cmap="YlOrRd")
plt.title("熱力圖")
```


## 📊 常見圖

```python
# 類別 vs 數值
sns.boxplot(data=df, x="day", y="total_bill")

# 散佈 + 分類
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex")

# 配對圖
sns.pairplot(df, hue="sex")

# 分布
sns.violinplot(data=df, x="day", y="total_bill")
```


## ✏️ 練習題

1. 用 AQI 資料畫 seaborn boxplot（按縣市）
2. 畫 heatmap 看縣市 × 污染物


