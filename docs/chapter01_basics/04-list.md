---
title: "1.4 串列 list"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.4 串列 list</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 學會建立、存取、修改 list
- 熟練 list 方法：append/insert/remove/pop/sort
- 用 for 迴圈走訪 list
- 理解 list 是 mutable（可變的）


## 📦 list 是什麼

list（串列）是 Python 最常用的容器 — **有序、可改變、可放任何東西**。

```python
fruits = ["蘋果", "香蕉", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Elvis", 35, True, 3.14]  # 可以混型別（但不推薦）
empty = []  # 空串列
```


## 🔪 存取元素

```python
fruits = ["蘋果", "香蕉", "葡萄", "橘子"]
#          [0]     [1]     [2]     [3]
#          [-4]    [-3]    [-2]    [-1]

print(fruits[0])    # 蘋果
print(fruits[-1])   # 橘子（最後一個）
print(fruits[1:3])  # ['香蕉', '葡萄'] 切片
print(len(fruits))  # 4 長度
```


## ✏️ 修改 list

```python
fruits = ["蘋果", "香蕉", "葡萄"]
fruits[0] = "草莓"            # 改值
print(fruits)                 # ['草莓', '香蕉', '葡萄']

fruits.append("橘子")         # 尾端加
fruits.insert(1, "奇異果")     # 指定位置加
fruits.remove("香蕉")          # 移除指定值
popped = fruits.pop()         # 移除並回傳最後一個
print(fruits)                  # ['草莓', '奇異果', '葡萄']
```


## 🔧 排序與其他方法

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                    # 原地排序
print(nums)                    # [1, 1, 2, 3, 4, 5, 6, 9]

nums.reverse()                 # 反轉
print(nums)                    # [9, 6, 5, 4, 3, 2, 1, 1]

print(nums.count(1))           # 2 算某值出現幾次
print(nums.index(9))           # 0 找某值第一次出現位置
```


## 🔍 檢查元素

```python
fruits = ["蘋果", "香蕉", "葡萄"]
print("蘋果" in fruits)        # True
print("西瓜" not in fruits)    # True
```


## ❗ 常見錯誤

1. **IndexError**：list 沒那麼長，索引超出範圍
2. **改 list 但忘了賦值**：`fruits.append("x")` 不用 `=`，但 `fruits = fruits.append(...)` 是 None
3. **= 跟 ==**：`a = b` 是複製參考（list 會連動），`a = b.copy()` 才是真的複製


## ✏️ 練習題

1. 建立一個 list 裝你 5 個最愛的食物
2. 加一個新的、移除一個、印出 list
3. 把 `[3,1,4,1,5,9,2,6]` 排序
4. 用 `in` 檢查某個元素是否在 list 裡
5. 試試看 `[[]] * 3` 跟 `[[] for _ in range(3)]` 的差異


