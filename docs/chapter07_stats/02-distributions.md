---
title: "7.2 機率分佈"
---

<div class="lesson-header">
  <span class="chapter-tag">第 7 章 · 統計基礎</span>
  <h1>7.2 機率分佈</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 統計</span>
  </div>
</div>

## 🎯 學習目標

- 常態 / t / 卡方 / F 分佈
- 知道何時用哪個


## 📊 常態分佈

```python
from scipy import stats
import numpy as np

# 標準常態 N(0, 1)
x = np.linspace(-4, 4, 100)
y = stats.norm.pdf(x, 0, 1)

# 算 z-score
z = stats.norm.ppf(0.975)   # 1.96（95% CI 邊界）
print(f"95% CI z = {z:.2f}")
```


## 📐 t 分佈（小樣本）

```python
# 樣本數 < 30 用 t 分佈
df = 10  # 自由度
t = stats.t.ppf(0.975, df)
print(f"t(10) at 0.975 = {t:.3f}")   # 2.228
```


## 📊 卡方分佈（類別資料）

```python
# 用於適合度檢定
chi = stats.chi2.ppf(0.95, df=4)
print(f"χ²(4) at 0.95 = {chi:.3f}")   # 9.488
```


## ✏️ 練習題

1. 模擬 10000 個 N(100, 15) 樣本
2. 算 P(X > 120)
3. 視覺化 t 分佈


