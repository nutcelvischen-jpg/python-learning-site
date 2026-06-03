---
title: "8.1 空氣品質分析"
---

<div class="lesson-header">
  <span class="chapter-tag">第 8 章 · 實戰專案</span>
  <h1>8.1 空氣品質分析</h1>
  <div class="meta">
    <span>⏱️ 120 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 整合運用</span>
  </div>
</div>

## 🎯 專案目標

用環境部 AQI 資料做完整視覺化分析：

- 全台 AQI 分佈
- 縣市比較
- 污染物相關性
- 趨勢分析


## 📥 資料準備

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

air = pd.read_csv("../assets/data/taiwan_aqi_latest.csv")
print(air.head())
print(air.describe())
```


## 📊 全台 AQI 地圖

```python
# 見 [8.5 章](../../chapter08_projects_extra/05-air-vs-house/) 的圖表程式碼
fig, ax = plt.subplots(figsize=(11, 7))
colors = air['aqi'].apply(lambda x:
    '#16A34A' if x <= 50 else
    '#EAB308' if x <= 100 else
    '#FF6B35' if x <= 150 else '#DC2626'
)
ax.scatter(air['longitude'], air['latitude'], c=colors, s=100, alpha=0.75)
ax.set_title("全台 AQI 分佈")
plt.show()
```


## 📈 縣市比較

```python
county = air.groupby("county")["aqi"].median().sort_values()
county.plot(kind="barh", figsize=(10, 6))
plt.title("縣市 AQI 中位數")
```


## 💡 結論

- 西部走廊 AQI 普遍較高
- 中南部空品較北部差
- 山區空品最好


