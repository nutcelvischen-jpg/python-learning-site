---
title: "4.6 隨機數與線代"
---

<div class="lesson-header">
  <span class="chapter-tag">第 4 章 · NumPy</span>
  <h1>4.6 隨機數與線代</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 隨機數生成
- 線性代數基本運算


## 🎲 隨機數

```python
import numpy as np

np.random.seed(42)      # 設種子（讓結果可重現）

np.random.rand(5)       # 5 個 0-1 均勻
np.random.randn(5)      # 5 個標準常態
np.random.randint(1, 100, 10)  # 1-100 整數 10 個
np.random.choice([1,2,3,4,5], 3)  # 隨機抽 3 個

# 重要：攪亂順序
arr = np.arange(10)
np.random.shuffle(arr)
print(arr)

# 抽樣
np.random.choice(arr, 3, replace=False)
```


## 📐 線性代數

```python
from numpy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

# 解聯立方程組 Ax = b
x = linalg.solve(A, b)
print(x)    # [-4.  4.5]

# 反矩陣
A_inv = linalg.inv(A)

# 特徵值
eigvals, eigvecs = linalg.eig(A)

# 行列式
print(linalg.det(A))    # -2.0
```


## ✏️ 練習題

1. 模擬 1000 次丟 2 個骰子，畫分佈
2. 解 2x2 聯立方程組
3. 算 3x3 矩陣的特徵值


