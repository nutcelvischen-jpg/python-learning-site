---
title: "4.3 形狀操作"
---

<div class="lesson-header">
  <span class="chapter-tag">第 4 章 · NumPy</span>
  <h1>4.3 形狀操作</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- reshape / ravel / transpose
- 改陣列形狀


## 🔄 reshape

```python
import numpy as np

a = np.arange(12)        # [0, 1, ..., 11]
b = a.reshape(3, 4)      # 3x4 矩陣
c = a.reshape(2, 2, 3)   # 2x2x3 張量

# -1 自動算
d = a.reshape(2, -1)     # 2x6
e = a.reshape(-1, 4)     # 3x4
```


## ↔️ ravel / flatten

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ravel())     # [1, 2, 3, 4, 5, 6]  # view
print(a.flatten())   # [1, 2, 3, 4, 5, 6]  # copy
```


## ↕️ transpose

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T)   # 轉置
# [[1, 4],
#  [2, 5],
#  [3, 6]]
```


## 🔗 stack / split

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 合併
np.concatenate([a, b])          # [1, 2, 3, 4, 5, 6]
np.vstack([a, b])              # 垂直疊
np.hstack([a, b])              # 水平排

# 切割
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np.split(c, 2, axis=1)          # 兩半
```


## ✏️ 練習題

1. 把 [1,12] reshape 成 3x4
2. 計算 3x4 矩陣的轉置
3. 合併兩個 1D array


