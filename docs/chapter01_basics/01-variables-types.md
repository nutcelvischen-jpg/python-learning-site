---
title: "1.1 變數與資料型別"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.1 變數與資料型別</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 💻 入門</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 理解什麼是變數和賦值
- 認識 4 個基本資料型別（int / float / str / bool）
- 學會用 `type()` 檢查型別
- 知道型別錯誤的常見原因


## 📦 變數是什麼

變數就像一個**貼了標籤的箱子**，用來裝資料。

```python
name = "Elvis"      # 把 "Elvis" 放進叫 name 的箱子
age = 35            # 把 35 放進叫 age 的箱子
pi = 3.14159        # 浮點數
is_student = False  # 布林值
```


## 🔢 4 個基本型別

| 型別 | 範例 | 說明 |
|---|---|---|
| `int` 整數 | `42`, `-7`, `0` | 沒有小數點的數字 |
| `float` 浮點數 | `3.14`, `-0.5` | 有小數點的數字 |
| `str` 字串 | `"Hello"`, `'台灣'` | 用引號包起來的文字 |
| `bool` 布林 | `True`, `False` | 只有兩個值（注意大寫） |

```python
print(type(42))       # <class 'int'>
print(type(3.14))     # <class 'float'>
print(type("Hello"))  # <class 'str'>
print(type(True))     # <class 'bool'>
```


## 💻 程式碼範例

```python
# 變數命名規則：英文字母開頭、可含數字底線
user_name = "小明"
user_age = 25
user_height = 175.5
is_member = True

# 印出來
print(f"姓名: {user_name}")
print(f"年齡: {user_age}")
print(f"身高: {user_height} cm")
print(f"會員: {is_member}")
```

**輸出：**
```
姓名: 小明
年齡: 25
身高: 175.5 cm
會員: True
```


## ❗ 常見錯誤

1. **拼字錯誤**：`Aage = 25` 跟 `age = 25` 是兩個變數
2. **忘了引號**：`name = Elvis` 會把 Elvis 當變數（NameError）
3. **True/False 大小寫**：必須大寫
4. **型別混用**：`"年齡: " + 25` 會 TypeError，要用 f-string 或 str(25)


## ✏️ 練習題

1. 宣告一個變數裝你的名字，印出
2. 宣告 int、float、str、bool 各一個，印出它們的 type
3. 把攝氏 25 度存成變數，印成「25°C」
4. 練習錯誤：試試 `x = 5` 然後 `print(X)` 會發生什麼？
5. 試試看 `a = 5; b = a; print(b)` 的結果，理解變數賦值


## 📚 延伸閱讀

- [Python 官方：數值型別](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python 官方：文字序列](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)


