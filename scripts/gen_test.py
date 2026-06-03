#!/usr/bin/env python3
"""
generate_all_chapters.py — 一次生成所有 Python 學堂章節
每章節保持一致結構：lesson-header + 學習目標 + 概念 + code + 練習 + 小結 + 延伸
"""
import os
from pathlib import Path

ROOT = Path("/Users/elvis/projects/python-learning-site/docs")

def header(chap, h1, time, audience="", level="入門"):
    aud = audience or f"💻 {level}"
    return f"""---
title: "{h1}"
---

<div class="lesson-header">
  <span class="chapter-tag">{chap}</span>
  <h1>{h1}</h1>
  <div class="meta">
    <span>⏱️ {time}</span>
    <span>📖 {aud}</span>
    <span>🎯 {level}</span>
  </div>
</div>

"""

# 章節元資料
SECTIONS = {
    # ===== 第 1 章 基礎語法 =====
    "chapter01_basics/01-variables-types.md": ("第 1 章 · 基礎語法", "1.1 變數與資料型別", "20 分鐘", "入門", [
        ("🎯 學習目標", """- 理解什麼是變數和賦值
- 認識 4 個基本資料型別（int / float / str / bool）
- 學會用 `type()` 檢查型別
- 知道型別錯誤的常見原因
"""),
        ("📦 變數是什麼", """變數就像一個**貼了標籤的箱子**，用來裝資料。

```python
name = "Elvis"      # 把 "Elvis" 放進叫 name 的箱子
age = 35            # 把 35 放進叫 age 的箱子
pi = 3.14159        # 浮點數
is_student = False  # 布林值
```
"""),
        ("🔢 4 個基本型別", """| 型別 | 範例 | 說明 |
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
"""),
        ("💻 程式碼範例", """```python
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
"""),
        ("❗ 常見錯誤", """1. **拼字錯誤**：`Aage = 25` 跟 `age = 25` 是兩個變數
2. **忘了引號**：`name = Elvis` 會把 Elvis 當變數（NameError）
3. **True/False 大小寫**：必須大寫
4. **型別混用**：`"年齡: " + 25` 會 TypeError，要用 f-string 或 str(25)
"""),
        ("✏️ 練習題", """1. 宣告一個變數裝你的名字，印出
2. 宣告 int、float、str、bool 各一個，印出它們的 type
3. 把攝氏 25 度存成變數，印成「25°C」
4. 練習錯誤：試試 `x = 5` 然後 `print(X)` 會發生什麼？
5. 試試看 `a = 5; b = a; print(b)` 的結果，理解變數賦值
"""),
        ("📚 延伸閱讀", """- [Python 官方：數值型別](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)
- [Python 官方：文字序列](https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str)
"""),
    ]),
    "chapter01_basics/02-operators.md": ("第 1 章 · 基礎語法", "1.2 運算子", "15 分鐘", "入門", [
        ("🎯 學習目標", """- 學會 5 種運算子（算術、比較、邏輯、賦值、成員）
- 理解運算子優先順序
- 知道 `==` 跟 `=` 的差別
"""),
        ("➕ 算術運算子", """```python
print(10 + 3)    # 13 加
print(10 - 3)    # 7  減
print(10 * 3)    # 30 乘
print(10 / 3)    # 3.333... 除（一定回傳 float）
print(10 // 3)   # 3  整數除法（取商）
print(10 % 3)    # 1  餘數
print(10 ** 3)   # 1000 次方
```
"""),
        ("⚖️ 比較運算子", """```python
print(5 == 5)    # True  等於（注意是兩個等號）
print(5 != 3)    # True  不等於
print(5 > 3)     # True  大於
print(5 < 3)     # False 小於
print(5 >= 5)    # True  大於等於
print(5 <= 3)    # False 小於等於
```
"""),
        ("🔗 邏輯運算子", """```python
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
"""),
        ("💡 實務範例", """```python
age = 25
has_license = True

# 判斷能不能開車
can_drive = age >= 18 and has_license
print(f"可以開車嗎？ {can_drive}")
```
"""),
        ("❗ 常見錯誤", """1. **`=` 跟 `==` 搞混**：`=` 是賦值，`==` 是比較
2. **除法 vs 整除**：`/` 回傳 float，`//` 回傳 int
3. **鏈式比較**：Python 支援 `1 < x < 10` 但新手不熟
"""),
        ("✏️ 練習題", """1. 算 17 除以 5 的商跟餘數
2. 寫一個判斷「年齡在 18-65 之間」的運算式
3. 試試看 `True + True` 的結果（提示：布林是 int 的子型別）
4. 寫一個 BMI 公式 `體重 / 身高²`
"""),
    ]),
}

# 寫入
for relpath, (chap, h1, time, level, blocks) in SECTIONS.items():
    out = header(chap, h1, time, level=level)
    for sec_title, sec_content in blocks:
        out += f"## {sec_title}\n\n{sec_content}\n\n"
    full = ROOT / relpath
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(out, encoding="utf-8")
    print(f"✅ {relpath} ({len(out)} chars)")

print(f"\n完成 {len(SECTIONS)} 個檔案")
