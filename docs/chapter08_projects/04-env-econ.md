---
title: "8.4 環境經濟學個案"
---

<div class="lesson-header">
  <span class="chapter-tag">第 8 章 · 實戰專案</span>
  <h1>8.4 環境經濟學個案</h1>
  <div class="meta">
    <span>⏱️ 150 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 整合運用</span>
  </div>
</div>

## 🎯 專案目標

環境經濟學的完整研究案例：

- 資料收集（空汙 + 房價 + 人口）
- 描述統計
- 相關分析
- 簡單迴歸
- 政策建議


## 📋 研究問題

「PM2.5 對房價有影響嗎？ 控制人口密度後呢？」

這是 hedonic pricing 模型的入門。


## 💻 完整程式碼

```python
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 載入
air = pd.read_csv("../assets/data/taiwan_aqi_latest.csv")
house = pd.read_csv("../assets/data/taichung_house_price_2024_2025.csv")

# 縣市平均 AQI
county_aqi = air.groupby("county")["pm2_5"].mean().reset_index()
county_aqi.columns = ["city", "avg_pm25"]

# 模擬人口密度資料
# ... (略)

# 合併
df = house.merge(county_aqi, on="city", how="left")
df.dropna(inplace=True)

# 簡單迴歸
X = sm.add_constant(df[["avg_pm25"]])
y = df["median_price_per_sqm"]
model = sm.OLS(y, X).fit()
print(model.summary())
```


## 🚀 挑戰版

1. 完整 hedonic 模型（多變項）
2. 加入時間序列
3. 跨縣市比較
4. 寫成完整研究報告


