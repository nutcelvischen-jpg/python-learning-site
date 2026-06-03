---
title: "7.5 相關與迴歸"
---

<div class="lesson-header">
  <span class="chapter-tag">第 7 章 · 統計基礎</span>
  <h1>7.5 相關與迴歸</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 統計</span>
  </div>
</div>

## 🎯 學習目標

- Pearson / Spearman 相關
- 簡單線性迴歸


## 🔗 相關分析

```python
from scipy import stats
import numpy as np

x = np.random.randn(100)
y = 0.5 * x + np.random.randn(100) * 0.5

# Pearson
r, p = stats.pearsonr(x, y)
print(f"Pearson r = {r:.3f}, p = {p:.4f}")

# Spearman（單調關係）
rho, p = stats.spearmanr(x, y)
print(f"Spearman ρ = {rho:.3f}, p = {p:.4f}")
```


## 📈 簡單線性迴歸

```python
slope, intercept, r, p, se = stats.linregress(x, y)
print(f"y = {slope:.3f} x + {intercept:.3f}")
print(f"R² = {r**2:.3f}")
```


## 💡 用 statsmodels

```python
import statsmodels.api as sm

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
print(model.summary())
```


## ✏️ 練習題

1. 算兩變數的 Pearson + Spearman
2. 畫散佈圖 + 迴歸線
3. 用 8.5 章的房價 vs AQI 算相關


