---
title: "1.8 迴圈"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.8 迴圈</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 熟練 `for` 迴圈走 list / dict / range
- 熟練 `while` 迴圈
- 理解 `break` / `continue` / `else` clause
- 避開無窮迴圈


## 🔁 for 迴圈

```python
# 走 list
fruits = ["蘋果", "香蕉", "葡萄"]
for fruit in fruits:
    print(fruit)

# 用 range
for i in range(5):         # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 11):     # 1 到 10
    print(i)

for i in range(0, 100, 10): # 0, 10, 20, ..., 90（步長 10）
    print(i)
```


## 🔄 while 迴圈

```python
n = 1
while n <= 5:
    print(n)
    n += 1
# 印 1 2 3 4 5
```

!!! danger "小心無窮迴圈"

    如果 `while` 條件永遠是 True，程式會卡住。 記得在迴圈內更新變數。


## ⛔ break / continue

```python
# break: 完全跳出迴圈
for i in range(10):
    if i == 5:
        break
    print(i)     # 0 1 2 3 4

# continue: 跳過這次，繼續下一次
for i in range(5):
    if i == 2:
        continue
    print(i)     # 0 1 3 4
```


## 🎁 for-else 模式

```python
# 找質數，沒找到時 else 處理
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(f"{n} 是質數")
```


## 🧰 enumerate / zip

```python
# enumerate: 拿到 index + value
fruits = ["蘋果", "香蕉", "葡萄"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# zip: 兩個 list 同時走
names = ["Elvis", "Bob", "Carol"]
ages = [35, 28, 42]
for name, age in zip(names, ages):
    print(f"{name} 歲數: {age}")
```


## ❗ 常見錯誤

1. **無窮迴圈**：while 條件沒更新
2. **改 list 邊迭代**：用 `for x in list: list.remove(x)` 會跳過元素，改用 list comprehension
3. **range 結尾**：`range(5)` 是 0-4 不是 1-5


## ✏️ 練習題

1. 印 1 到 100，3 的倍數印 "Fizz"，5 的倍數印 "Buzz"，兩個都是印 "FizzBuzz"
2. 用 while 算 1+2+...+100
3. 用 for + enumerate 走 list
4. 找 1-100 的所有質數
5. 寫一個 `for-else` 找 list 裡有沒有某個值


