---
title: "4.2 ndarray 建立/索引/切片"
---

<div class="lesson-header">
  <span class="chapter-tag">第 4 章 · NumPy</span>
  <h1>4.2 ndarray 建立/索引/切片</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 學會建立 ndarray
- 索引跟切片
- 常用屬性：shape / dtype / ndim


## 🏗️ 建立 ndarray

```python
import numpy as np

# 從 list
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])   # 2D

# 特殊陣列
np.zeros(5)          # [0, 0, 0, 0, 0]
np.ones((2, 3))      # 2x3 全 1
np.full((2, 2), 7)   # 2x2 全 7
np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5) # [0, 0.25, 0.5, 0.75, 1]
np.eye(3)            # 3x3 單位矩陣
np.random.rand(3, 4) # 0-1 隨機
```


## 🔪 索引切片

```python
a = np.array([10, 20, 30, 40, 50])
print(a[0])     # 10
print(a[-1])    # 50
print(a[1:4])   # [20, 30, 40]
print(a[::2])   # [10, 30, 50]

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 1])     # 2
print(b[:, 0])     # 第一欄 [1, 4, 7]
print(b[1, :])     # 第二列 [4, 5, 6]
```


## 🔍 屬性

```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)    # (2, 3)
print(a.dtype)    # int64
print(a.ndim)     # 2
print(a.size)     # 6
```


## ✏️ 練習題

1. 建立 1D ndarray 含 1-10
2. 建立 3x3 全 0 陣列
3. 建立 2x5 identity matrix
4. 切片取出第 2 列第 3 欄


