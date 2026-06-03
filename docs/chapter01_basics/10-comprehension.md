---
title: "1.10 串列推導式"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.10 串列推導式</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 學會 list comprehension
- 認識 dict / set / generator comprehension
- 比較推導式 vs 傳統 for 迴圈


## ✨ 為什麼用推導式

```python
# 傳統寫法
squares = []
for i in range(10):
    squares.append(i ** 2)

# 推導式（一行搞定！）
squares = [i ** 2 for i in range(10)]
```


## 🎯 帶條件的推導式

```python
# 1 到 100 的偶數
evens = [i for i in range(1, 101) if i % 2 == 0]

# 大寫
names = ["alice", "bob", "carol"]
upper_names = [n.upper() for n in names]

# 帶 if-else
labels = ["偶數" if i % 2 == 0 else "奇數" for i in range(5)]
```


## 📚 dict / set 推導式

```python
# dict comprehension
square_dict = {i: i**2 for i in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# set comprehension
chars = {c for c in "hello"}
# {'h', 'e', 'l', 'o'}
```


## ⚡ 巢狀推導式（小心！）

```python
# 兩層 list
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

!!! warning "可讀性"

    推導式不要超過兩層，不然就改用 for 迴圈。 **可讀性 > 簡潔**。


## ❗ 常見錯誤

1. **推導式太複雜**：改用 for 迴圈
2. **忘了 if 條件的位置**：`[x for x in lst if x > 0]` 不是 `[x if x > 0 for x in lst]`
3. **generator 跟 list 混淆**：(x for x in lst) 是 generator，要 list(...) 才看得到


## ✏️ 練習題

1. 用推導式把 `[1,2,3,4,5]` 每個元素平方
2. 過濾出長度 > 3 的字串
3. 用推導式建立 `{i: i*2 for i in range(5)}`
4. 把一個 list 扁平化：`[[1,2],[3,4]]` → `[1,2,3,4]`


