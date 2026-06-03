---
title: "1.9 函式"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.9 函式</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 學會定義與呼叫函式
- 熟練參數（位置、預設、*args、**kwargs）
- 理解 return 跟 print 的差別
- 寫好的 docstring


## 🔧 基本函式

```python
def greet(name):
    """打招呼"""
    return f"哈囉 {name}！"

print(greet("Elvis"))   # 哈囉 Elvis！
```


## 📦 參數種類

```python
# 1. 位置參數
def add(a, b):
    return a + b

# 2. 預設參數
def greet(name, greeting="哈囉"):
    return f"{greeting} {name}！"

print(greet("Elvis"))            # 哈囉 Elvis！
print(greet("Elvis", "Hi"))     # Hi Elvis！

# 3. *args 不定個數位置參數
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))   # 10

# 4. **kwargs 不定個數關鍵字參數
def user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

user_info(name="Elvis", age=35)
```


## ↩️ return 多個值

```python
def calc(a, b):
    return a + b, a - b, a * b

add, sub, mul = calc(10, 3)
print(add, sub, mul)    # 13 7 30
```


## 📝 docstring（必寫！）

```python
def calculate_bmi(weight_kg, height_cm):
    """
    計算 BMI 身體質量指數

    參數:
        weight_kg: 體重（公斤）
        height_cm: 身高（公分）

    回傳:
        BMI 數值（float）
    """
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)
```

用 `help(calculate_bmi)` 可以看到這個 docstring。


## ❗ 常見錯誤

1. **忘記 return**：函式預設回傳 `None`
2. **可變預設參數**：`def f(x, lst=[])` 是陷阱！ lst 會被共享
3. **過早綁定**：迴圈裡用 lambda 會踩到 closure 雷


## ✏️ 練習題

1. 寫一個 `circle_area(r)` 函式算圓面積
2. 寫一個 `is_prime(n)` 判斷質數
3. 寫一個函式接受任意個數字，回傳平均值
4. 寫一個函式回傳 1+2+...+n（遞迴或迴圈皆可）
5. 為你的函式加 docstring


