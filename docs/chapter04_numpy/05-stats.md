---
title: "4.5 統計函式"
---

<div class="lesson-header">
  <span class="chapter-tag">第 4 章 · NumPy</span>
  <h1>4.5 統計函式</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 學會 sum / mean / std / median
- 沿軸計算（axis）


## 📊 基本統計

```python
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(a.sum())         # 55
print(a.mean())        # 5.5
print(a.std())         # 2.872
print(a.var())         # 8.25
print(a.min())         # 1
print(a.max())         # 10
print(np.median(a))    # 5.5
print(np.percentile(a, 75))  # 7.75
```


## ↕️ 沿軸計算

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.sum(axis=0))   # [5, 7, 9]   每欄加總
print(a.sum(axis=1))   # [6, 15]     每列加總
print(a.mean(axis=0))  # [2.5, 3.5, 4.5]
```


## 🔍 argmax / where

```python
a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(a.argmax())     # 5（最大值的 index）
print(a.argmin())     # 1

print(np.where(a > 3))            # 回傳符合條件的 index
print(np.where(a > 3, a, 0))     # 條件為真留 a，否則 0
```


## ✏️ 練習題

1. 算 [1..100] 的 mean / std / median
2. 隨機 1000 個常態分佈樣本，算分位數
3. 沿 axis=0 算 2D 陣列的 mean


