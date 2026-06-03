---
title: "4.1 NumPy 簡介"
---

<div class="lesson-header">
  <span class="chapter-tag">第 4 章 · NumPy</span>
  <h1>4.1 NumPy 簡介</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 知道 NumPy 是什麼
- 為什麼 list 不夠用
- 學會安裝跟 import


## ⚡ NumPy = Numerical Python

```python
import numpy as np

# Python list
list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30, 40, 50]

# 想算 list_a + list_b 怎麼辦？
# 得寫 for 迴圈
result = [a + b for a, b in zip(list_a, list_b)]

# NumPy 一次搞定
arr_a = np.array(list_a)
arr_b = np.array(list_b)
result = arr_a + arr_b    # [11, 22, 33, 44, 55]
```


## 🏃 速度差異

NumPy 用 C 實作，比純 Python **快 10-100x**。

```python
import numpy as np
import time

n = 1_000_000
py_list = list(range(n))
np_arr = np.arange(n)

# 純 Python sum
t0 = time.time()
sum(py_list)
print(f"Python: {time.time() - t0:.3f}s")

# NumPy sum
t0 = time.time()
np.sum(np_arr)
print(f"NumPy:   {time.time() - t0:.3f}s")
```


## ✏️ 練習題

1. 比較 Python list 跟 NumPy 算 100 萬個元素加法的速度
2. 印出 np.__version__


