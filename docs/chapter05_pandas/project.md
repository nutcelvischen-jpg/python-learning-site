---
title: "小專案: 銷售資料分析"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>小專案: 銷售資料分析</h1>
  <div class="meta">
    <span>⏱️ 90 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 專案目標

用模擬的 1 萬筆電商銷售資料做完整分析：

- 讀 CSV → 清理 → groupby → 視覺化


## 📥 模擬資料

```python
import pandas as pd
import numpy as np

np.random.seed(42)
n = 10000
df = pd.DataFrame({
    "order_id": range(n),
    "date": pd.date_range("2025-01-01", periods=n, freq="30min"),
    "product": np.random.choice(["筆電", "手機", "耳機", "平板"], n),
    "price": np.random.randint(500, 50000, n),
    "quantity": np.random.randint(1, 5, n),
})
df["revenue"] = df["price"] * df["quantity"]
df.to_csv("sales.csv", index=False, encoding="utf-8")
```


## 📊 分析問題

1. 各產品總營收？
2. 月營收趨勢？
3. 哪天賣最好？
4. 平均客單價？
5. 高單價產品分布？


## 💻 完整分析

```python
df = pd.read_csv("sales.csv", parse_dates=["date"])

# 1. 各產品營收
print(df.groupby("product")["revenue"].sum().sort_values(ascending=False))

# 2. 月營收
df["month"] = df["date"].dt.to_period("M")
print(df.groupby("month")["revenue"].sum())

# 3. 哪一天賣最好
best_day = df.groupby(df["date"].dt.date)["revenue"].sum().idxmax()
print(f"Best day: {best_day}")

# 4. 平均客單價
print(f"客單價平均: NT${df.groupby('order_id')['revenue'].sum().mean():.0f}")

# 5. 高單價產品（> 30000）
print(df[df["price"] > 30000]["product"].value_counts())
```


## 📈 視覺化

```python
import matplotlib.pyplot as plt

# 月營收趨勢
monthly = df.groupby("month")["revenue"].sum()
monthly.plot(kind="line", marker="o", figsize=(10, 5))
plt.title("月營收趨勢")
plt.ylabel("NT$")
plt.grid(True, alpha=0.3)
plt.show()

# 產品圓餅圖
df.groupby("product")["revenue"].sum().plot.pie(autopct="%1.1f%%")
plt.title("產品營收占比")
plt.show()
```


## 🚀 挑戰版

1. RFM 分析
2. 產品交叉銷售分析
3. 預測下月營收


