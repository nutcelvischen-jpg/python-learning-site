---
title: "4.4 向量化與 broadcasting"
---

<div class="lesson-header">
  <span class="chapter-tag">第 4 章 · NumPy</span>
  <h1>4.4 向量化與 broadcasting</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 理解 broadcasting 規則
- 寫出高效的向量化運算


## 🌊 什麼是 broadcasting

不同形狀的陣列**自動擴展**做運算。

```python
import numpy as np

a = np.array([1, 2, 3])
b = 10                # 純量
print(a + b)          # [11, 12, 13]  ← 自動擴展

c = np.array([10, 20, 30])
print(a + c)          # [11, 22, 33]  ← 元素對元素
```


## 📏 規則

1. 如果兩個陣列維度數不同，小的補 1 在左邊
2. 如果形狀不相等，會在 size 1 的維度擴展
3. 如果還是不合，broadcasting 失敗

```python
# 範例 1: (3,) + (1,) → (3,)
a = np.array([1, 2, 3])
b = np.array([10])
print(a + b)    # [11, 12, 13]

# 範例 2: (3, 1) + (1, 4) → (3, 4)
a = np.array([[1], [2], [3]])      # 3x1
b = np.array([[10, 20, 30, 40]])   # 1x4
print(a + b)
# [[11, 21, 31, 41],
#  [12, 22, 32, 42],
#  [13, 23, 33, 43]]
```


## 💡 為什麼好用

```python
# 不用 for 迴圈
prices = np.array([100, 200, 300])
discounts = np.array([[0.9], [0.8], [0.7]])   # 3x1
final = prices * discounts                     # 3x3
```


## ✏️ 練習題

1. 算陣列 `[[1,2,3], [4,5,6]]` 加 10 的結果
2. (3,1) + (1,4) broadcasting 後形狀
3. 用 broadcasting 算 5 個產品 3 種稅率的價格


