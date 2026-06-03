---
title: "1.2 運算子"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.2 運算子</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 💻 入門</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 學會 5 種運算子（算術、比較、邏輯、賦值、成員）
- 理解運算子優先順序
- 知道 `==` 跟 `=` 的差別


## ➕ 算術運算子

```python
print(10 + 3)    # 13 加
print(10 - 3)    # 7  減
print(10 * 3)    # 30 乘
print(10 / 3)    # 3.333... 除（一定回傳 float）
print(10 // 3)   # 3  整數除法（取商）
print(10 % 3)    # 1  餘數
print(10 ** 3)   # 1000 次方
```


## ⚖️ 比較運算子

```python
print(5 == 5)    # True  等於（注意是兩個等號）
print(5 != 3)    # True  不等於
print(5 > 3)     # True  大於
print(5 < 3)     # False 小於
print(5 >= 5)    # True  大於等於
print(5 <= 3)    # False 小於等於
```


## 🔗 邏輯運算子

```python
# and: 兩邊都 True 才 True
print(True and False)   # False
print(True and True)    # True

# or: 有一邊 True 就 True
print(False or True)    # True
print(False or False)   # False

# not: 反向
print(not True)         # False
print(not False)        # True
```


## 💡 實務範例

```python
age = 25
has_license = True

# 判斷能不能開車
can_drive = age >= 18 and has_license
print(f"可以開車嗎？ {can_drive}")
```


## ❗ 常見錯誤

1. **`=` 跟 `==` 搞混**：`=` 是賦值，`==` 是比較
2. **除法 vs 整除**：`/` 回傳 float，`//` 回傳 int
3. **鏈式比較**：Python 支援 `1 < x < 10` 但新手不熟


## ✏️ 練習題

1. 算 17 除以 5 的商跟餘數
2. 寫一個判斷「年齡在 18-65 之間」的運算式
3. 試試看 `True + True` 的結果（提示：布林是 int 的子型別）
4. 寫一個 BMI 公式 `體重 / 身高²`


