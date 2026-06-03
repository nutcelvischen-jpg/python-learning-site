---
title: "1.6 tuple 與不可變"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.6 tuple 與不可變</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 認識 tuple（序對 / 元組）
- 理解 tuple 跟 list 的差別
- 知道什麼時候用 tuple
- 學會 tuple unpacking


## 📦 tuple 是什麼

tuple 跟 list 很像，但是**不可變（immutable）** — 創了就不能改。

```python
# 建立
t = (1, 2, 3)
single = (5,)     # 單元素 tuple 要加逗號！
empty = ()

# 也可以不加括號
coords = 10, 20
x, y = coords     # tuple unpacking
```


## 🔒 為什麼用 tuple

| 特性 | list | tuple |
|---|---|---|
| 可改 | ✅ | ❌ |
| 速度 | 慢一點 | 快一點 |
| 用途 | 動態資料 | 固定資料 |
| 當 dict key | ❌ | ✅ |

```python
# tuple 可以當 dict key（list 不行）
locations = {
    (0, 0): "原點",
    (1, 0): "東邊",
    (0, 1): "北邊"
}
print(locations[(1, 0)])   # 東邊
```


## 📥 Tuple Unpacking

```python
# 同時賦值給多個變數
x, y, z = (10, 20, 30)

# 交換兩個變數（超優雅）
a, b = 5, 10
a, b = b, a
print(a, b)    # 10 5

# 函式回傳多個值
def get_user():
    return "Elvis", 35, "台中"

name, age, city = get_user()
```


## ❗ 常見錯誤

1. **單元素 tuple 忘記逗號**：`t = (5)` 是 int 不是 tuple
2. **想改 tuple 內容**：`t[0] = 1` 會錯


## ✏️ 練習題

1. 建立一個 tuple 裝 RGB 三個值 `(255, 128, 0)`
2. 用 unpacking 把 tuple 解開到三個變數
3. 寫一個函式回傳 `(min, max, avg)` 三個值
4. 試試看 `t = (1, [2, 3]); t[1].append(4)` 的結果（提示：tuple 內的 list 是可變的）


