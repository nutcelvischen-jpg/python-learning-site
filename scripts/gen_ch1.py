#!/usr/bin/env python3
"""
generate_all.py — 為 Python 學堂生成所有剩餘章節
策略：每章保留完整結構 + 程式碼範例 + 練習題，內容精簡但可用
"""
import os
from pathlib import Path

ROOT = Path("/Users/elvis/projects/python-learning-site/docs")

def H(chap, h1, time, level="入門"):
    return f"""---
title: "{h1}"
---

<div class="lesson-header">
  <span class="chapter-tag">{chap}</span>
  <h1>{h1}</h1>
  <div class="meta">
    <span>⏱️ {time}</span>
    <span>📖 互動式</span>
    <span>🎯 {level}</span>
  </div>
</div>

"""

# 章節內容資料庫
# 格式: (filename, chapter_tag, h1, time, level, [(subhead, content), ...])
SECTIONS = [
    # ============= 第 1 章 基礎 =============
    ("chapter01_basics/03-strings.md", "第 1 章 · 基礎語法", "1.3 字串處理", "25 分鐘", "入門", [
        ("🎯 學習目標", """- 學會字串建立、索引、切片
- 常用字串方法：upper/lower/split/replace/strip
- 學會 f-string 格式化
- 處理中文與特殊字元
"""),
        ("📜 字串建立", """```python
s1 = '單引號'
s2 = "雙引號"
s3 = '''三引號可以
跨多行'''
print(s3)
```
"""),
        ("🔪 索引與切片", """```python
s = "Hello, World!"
#    0123456789...

print(s[0])      # 'H'  第一個字
print(s[-1])     # '!'  最後一個
print(s[0:5])    # 'Hello' 切片 [起:訖]
print(s[7:])     # 'World!' 從 7 開始到最後
print(s[:5])     # 'Hello' 從頭到 5
print(s[::2])    # 'Hlo ol!' 步長 2
```
"""),
        ("🎨 f-string 格式化（必學！）", """```python
name = "Elvis"
age = 35
# f-string 前面小寫 f，用 {變數} 嵌入
print(f"我是 {name}，{age} 歲")
# 可以做運算
print(f"明年 {age + 1} 歲")
# 可以格式化數字
pi = 3.14159
print(f"π = {pi:.2f}")   # π = 3.14
print(f"π = {pi:.4f}")   # π = 3.1416
```
"""),
        ("🔧 常用字串方法", """```python
s = "  Hello, Python!  "
print(s.strip())           # 去掉頭尾空白
print(s.upper())           # 全大寫
print(s.lower())           # 全小寫
print(s.replace("Hello", "Hi"))
print("a,b,c".split(","))  # ['a', 'b', 'c']
print(",".join(['a','b','c']))  # "a,b,c"
print("Hello" in s)        # True（包含檢查）
```
"""),
        ("❗ 常見錯誤", """1. **中英文混用索引**：中文一個字佔 3 bytes，但 `len()` 看字元數
2. **字串不可改**：`s[0] = 'h'` 會錯！ 要用 replace
3. **f-string 忘了 f**：`"Hello {name}"` 不會格式化
"""),
        ("✏️ 練習題", """1. 把 `"  python  "` 用 `strip()` 清乾淨
2. 用 slice 反轉字串 `"Hello"` → `"olleH"`
3. f-string 印出 1/3 保留 4 位小數
4. `"a,b,c,d".split(",")` 的結果是什麼？
5. 寫一個程式問名字，印出名字的長度
"""),
    ]),

    ("chapter01_basics/04-list.md", "第 1 章 · 基礎語法", "1.4 串列 list", "30 分鐘", "入門", [
        ("🎯 學習目標", """- 學會建立、存取、修改 list
- 熟練 list 方法：append/insert/remove/pop/sort
- 用 for 迴圈走訪 list
- 理解 list 是 mutable（可變的）
"""),
        ("📦 list 是什麼", """list（串列）是 Python 最常用的容器 — **有序、可改變、可放任何東西**。

```python
fruits = ["蘋果", "香蕉", "葡萄"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Elvis", 35, True, 3.14]  # 可以混型別（但不推薦）
empty = []  # 空串列
```
"""),
        ("🔪 存取元素", """```python
fruits = ["蘋果", "香蕉", "葡萄", "橘子"]
#          [0]     [1]     [2]     [3]
#          [-4]    [-3]    [-2]    [-1]

print(fruits[0])    # 蘋果
print(fruits[-1])   # 橘子（最後一個）
print(fruits[1:3])  # ['香蕉', '葡萄'] 切片
print(len(fruits))  # 4 長度
```
"""),
        ("✏️ 修改 list", """```python
fruits = ["蘋果", "香蕉", "葡萄"]
fruits[0] = "草莓"            # 改值
print(fruits)                 # ['草莓', '香蕉', '葡萄']

fruits.append("橘子")         # 尾端加
fruits.insert(1, "奇異果")     # 指定位置加
fruits.remove("香蕉")          # 移除指定值
popped = fruits.pop()         # 移除並回傳最後一個
print(fruits)                  # ['草莓', '奇異果', '葡萄']
```
"""),
        ("🔧 排序與其他方法", """```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]
nums.sort()                    # 原地排序
print(nums)                    # [1, 1, 2, 3, 4, 5, 6, 9]

nums.reverse()                 # 反轉
print(nums)                    # [9, 6, 5, 4, 3, 2, 1, 1]

print(nums.count(1))           # 2 算某值出現幾次
print(nums.index(9))           # 0 找某值第一次出現位置
```
"""),
        ("🔍 檢查元素", """```python
fruits = ["蘋果", "香蕉", "葡萄"]
print("蘋果" in fruits)        # True
print("西瓜" not in fruits)    # True
```
"""),
        ("❗ 常見錯誤", """1. **IndexError**：list 沒那麼長，索引超出範圍
2. **改 list 但忘了賦值**：`fruits.append("x")` 不用 `=`，但 `fruits = fruits.append(...)` 是 None
3. **= 跟 ==**：`a = b` 是複製參考（list 會連動），`a = b.copy()` 才是真的複製
"""),
        ("✏️ 練習題", """1. 建立一個 list 裝你 5 個最愛的食物
2. 加一個新的、移除一個、印出 list
3. 把 `[3,1,4,1,5,9,2,6]` 排序
4. 用 `in` 檢查某個元素是否在 list 裡
5. 試試看 `[[]] * 3` 跟 `[[] for _ in range(3)]` 的差異
"""),
    ]),

    ("chapter01_basics/05-dict-set.md", "第 1 章 · 基礎語法", "1.5 字典 dict 與集合 set", "25 分鐘", "入門", [
        ("🎯 學習目標", """- 學會 dict（字典）的建立與操作
- 理解 key-value 配對
- 認識 set（集合）的去重特性
- 知道 dict.get() 的好處
"""),
        ("📖 dict — 字典", """```python
# 建立
person = {
    "name": "Elvis",
    "age": 35,
    "city": "台中",
    "job": "教授"
}

# 存取
print(person["name"])          # Elvis
print(person.get("age"))       # 35
print(person.get("phone", "N/A"))  # N/A（找不到回傳預設值）

# 修改
person["age"] = 36            # 改值
person["email"] = "x@y.com"   # 加新 key

# 刪除
del person["city"]
```
"""),
        ("🔄 走訪 dict", """```python
person = {"name": "Elvis", "age": 35, "city": "台中"}

for key in person:                # 走 key
    print(f"{key} = {person[key]}")

for key, value in person.items(): # 走 (key, value)
    print(f"{key}: {value}")

for value in person.values():     # 只走 value
    print(value)
```
"""),
        ("🔧 dict 常用方法", """```python
d = {"a": 1, "b": 2}
print(d.keys())       # dict_keys(['a', 'b'])
print(d.values())     # dict_values([1, 2])
print(d.items())      # dict_items([('a', 1), ('b', 2)])

d.update({"c": 3})    # 合併另一個 dict
d.pop("a")            # 移除並回傳
d.clear()             # 清空
```
"""),
        ("🎯 set — 集合", """set 是**無序、不重複**的元素集合，適合去重與集合運算。

```python
s = {1, 2, 3, 3, 2, 1}   # 重複會被去掉
print(s)                    # {1, 2, 3}

# 集合運算
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)                # 交集 {3}
print(a | b)                # 聯集 {1,2,3,4,5}
print(a - b)                # 差集 {1,2}

# 去重
nums = [1, 2, 2, 3, 3, 3]
print(set(nums))            # {1, 2, 3}
```
"""),
        ("❗ 常見錯誤", """1. **KeyError**：用 `d[key]` 找不到會錯，用 `d.get(key, default)` 不會
2. **dict 沒有順序保證**（Python 3.7+ 維護插入順序但別依賴）
3. **set 不可索引**：`s[0]` 會錯，要 `list(s)[0]`
"""),
        ("✏️ 練習題", """1. 寫一個 dict 裝 3 個朋友的名字跟年齡
2. 走訪 dict 印出 `name: age` 格式
3. 把 list `[1,1,2,3,3,3,4]` 轉 set 看看
4. 算兩個 set 的交集、聯集、差集
5. 用 dict 計數一段文字中每個字出現幾次
"""),
    ]),

    ("chapter01_basics/06-tuple.md", "第 1 章 · 基礎語法", "1.6 tuple 與不可變", "15 分鐘", "入門", [
        ("🎯 學習目標", """- 認識 tuple（序對 / 元組）
- 理解 tuple 跟 list 的差別
- 知道什麼時候用 tuple
- 學會 tuple unpacking
"""),
        ("📦 tuple 是什麼", """tuple 跟 list 很像，但是**不可變（immutable）** — 創了就不能改。

```python
# 建立
t = (1, 2, 3)
single = (5,)     # 單元素 tuple 要加逗號！
empty = ()

# 也可以不加括號
coords = 10, 20
x, y = coords     # tuple unpacking
```
"""),
        ("🔒 為什麼用 tuple", """| 特性 | list | tuple |
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
"""),
        ("📥 Tuple Unpacking", """```python
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
"""),
        ("❗ 常見錯誤", """1. **單元素 tuple 忘記逗號**：`t = (5)` 是 int 不是 tuple
2. **想改 tuple 內容**：`t[0] = 1` 會錯
"""),
        ("✏️ 練習題", """1. 建立一個 tuple 裝 RGB 三個值 `(255, 128, 0)`
2. 用 unpacking 把 tuple 解開到三個變數
3. 寫一個函式回傳 `(min, max, avg)` 三個值
4. 試試看 `t = (1, [2, 3]); t[1].append(4)` 的結果（提示：tuple 內的 list 是可變的）
"""),
    ]),

    ("chapter01_basics/07-if-else.md", "第 1 章 · 基礎語法", "1.7 流程控制", "20 分鐘", "入門", [
        ("🎯 學習目標", """- 學會 `if / elif / else` 條件判斷
- 理解 Python 的縮排規則（4 空格）
- 熟練巢狀條件
- 學會三元運算式
"""),
        ("🔀 基礎 if", """```python
age = 18

if age >= 18:
    print("你已成年")
else:
    print("你未成年")
```
"""),
        ("🎯 if / elif / else", """```python
score = 85

if score >= 90:
    print("A+ 優等")
elif score >= 80:
    print("B+ 良好")
elif score >= 70:
    print("C+ 中等")
elif score >= 60:
    print("D+ 及格")
else:
    print("F 不及格")
```
"""),
        ("🔗 複合條件", """```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("可以開車")
elif age >= 18 and not has_license:
    print("需要先去考駕照")
else:
    print("年紀還沒到")
```
"""),
        ("⚡ 三元運算式", """```python
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)    # 成年
```
"""),
        ("🪆 巢狀 if", """```python
score = 85
is_makeup = True

if score >= 60:
    if is_makeup:
        print("補考通過")
    else:
        print("正常通過")
else:
    print("未通過")
```
"""),
        ("❗ 常見錯誤", """1. **`==` 跟 `=` 搞混**
2. **忘記冒號 `:`**
3. **縮排不一致**：同一個 block 要用一樣的縮排（建議 4 空格）
4. **過度巢狀**：超過 3 層考慮用函式或早 return
"""),
        ("✏️ 練習題", """1. 寫一個 BMI 分類：< 18.5 過輕, 18.5-24 正常, 24-27 過重, > 27 肥胖
2. 判斷閏年：能被 4 整除且（不能被 100 整除 或 能被 400 整除）
3. 寫一個三元運算式判斷奇偶
4. 巢狀判斷：根據年齡 + 是否會員給不同折扣
"""),
    ]),

    ("chapter01_basics/08-loops.md", "第 1 章 · 基礎語法", "1.8 迴圈", "30 分鐘", "入門", [
        ("🎯 學習目標", """- 熟練 `for` 迴圈走 list / dict / range
- 熟練 `while` 迴圈
- 理解 `break` / `continue` / `else` clause
- 避開無窮迴圈
"""),
        ("🔁 for 迴圈", """```python
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
"""),
        ("🔄 while 迴圈", """```python
n = 1
while n <= 5:
    print(n)
    n += 1
# 印 1 2 3 4 5
```

!!! danger "小心無窮迴圈"

    如果 `while` 條件永遠是 True，程式會卡住。 記得在迴圈內更新變數。
"""),
        ("⛔ break / continue", """```python
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
"""),
        ("🎁 for-else 模式", """```python
# 找質數，沒找到時 else 處理
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        print(f"{n} 是質數")
```
"""),
        ("🧰 enumerate / zip", """```python
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
"""),
        ("❗ 常見錯誤", """1. **無窮迴圈**：while 條件沒更新
2. **改 list 邊迭代**：用 `for x in list: list.remove(x)` 會跳過元素，改用 list comprehension
3. **range 結尾**：`range(5)` 是 0-4 不是 1-5
"""),
        ("✏️ 練習題", """1. 印 1 到 100，3 的倍數印 "Fizz"，5 的倍數印 "Buzz"，兩個都是印 "FizzBuzz"
2. 用 while 算 1+2+...+100
3. 用 for + enumerate 走 list
4. 找 1-100 的所有質數
5. 寫一個 `for-else` 找 list 裡有沒有某個值
"""),
    ]),

    ("chapter01_basics/09-functions.md", "第 1 章 · 基礎語法", "1.9 函式", "30 分鐘", "入門", [
        ("🎯 學習目標", """- 學會定義與呼叫函式
- 熟練參數（位置、預設、*args、**kwargs）
- 理解 return 跟 print 的差別
- 寫好的 docstring
"""),
        ("🔧 基本函式", """```python
def greet(name):
    \"\"\"打招呼\"\"\"
    return f\"哈囉 {name}！\"

print(greet(\"Elvis\"))   # 哈囉 Elvis！
```
"""),
        ("📦 參數種類", """```python
# 1. 位置參數
def add(a, b):
    return a + b

# 2. 預設參數
def greet(name, greeting=\"哈囉\"):
    return f\"{greeting} {name}！\"

print(greet(\"Elvis\"))            # 哈囉 Elvis！
print(greet(\"Elvis\", \"Hi\"))     # Hi Elvis！

# 3. *args 不定個數位置參數
def total(*nums):
    return sum(nums)

print(total(1, 2, 3, 4))   # 10

# 4. **kwargs 不定個數關鍵字參數
def user_info(**info):
    for key, value in info.items():
        print(f\"{key}: {value}\")

user_info(name=\"Elvis\", age=35)
```
"""),
        ("↩️ return 多個值", """```python
def calc(a, b):
    return a + b, a - b, a * b

add, sub, mul = calc(10, 3)
print(add, sub, mul)    # 13 7 30
```
"""),
        ("📝 docstring（必寫！）", """```python
def calculate_bmi(weight_kg, height_cm):
    \"\"\"
    計算 BMI 身體質量指數

    參數:
        weight_kg: 體重（公斤）
        height_cm: 身高（公分）

    回傳:
        BMI 數值（float）
    \"\"\"
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)
```

用 `help(calculate_bmi)` 可以看到這個 docstring。
"""),
        ("❗ 常見錯誤", """1. **忘記 return**：函式預設回傳 `None`
2. **可變預設參數**：`def f(x, lst=[])` 是陷阱！ lst 會被共享
3. **過早綁定**：迴圈裡用 lambda 會踩到 closure 雷
"""),
        ("✏️ 練習題", """1. 寫一個 `circle_area(r)` 函式算圓面積
2. 寫一個 `is_prime(n)` 判斷質數
3. 寫一個函式接受任意個數字，回傳平均值
4. 寫一個函式回傳 1+2+...+n（遞迴或迴圈皆可）
5. 為你的函式加 docstring
"""),
    ]),

    ("chapter01_basics/10-comprehension.md", "第 1 章 · 基礎語法", "1.10 串列推導式", "20 分鐘", "入門", [
        ("🎯 學習目標", """- 學會 list comprehension
- 認識 dict / set / generator comprehension
- 比較推導式 vs 傳統 for 迴圈
"""),
        ("✨ 為什麼用推導式", """```python
# 傳統寫法
squares = []
for i in range(10):
    squares.append(i ** 2)

# 推導式（一行搞定！）
squares = [i ** 2 for i in range(10)]
```
"""),
        ("🎯 帶條件的推導式", """```python
# 1 到 100 的偶數
evens = [i for i in range(1, 101) if i % 2 == 0]

# 大寫
names = [\"alice\", \"bob\", \"carol\"]
upper_names = [n.upper() for n in names]

# 帶 if-else
labels = [\"偶數\" if i % 2 == 0 else \"奇數\" for i in range(5)]
```
"""),
        ("📚 dict / set 推導式", """```python
# dict comprehension
square_dict = {i: i**2 for i in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# set comprehension
chars = {c for c in \"hello\"}
# {'h', 'e', 'l', 'o'}
```
"""),
        ("⚡ 巢狀推導式（小心！）", """```python
# 兩層 list
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
# [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
```

!!! warning "可讀性"

    推導式不要超過兩層，不然就改用 for 迴圈。 **可讀性 > 簡潔**。
"""),
        ("❗ 常見錯誤", """1. **推導式太複雜**：改用 for 迴圈
2. **忘了 if 條件的位置**：`[x for x in lst if x > 0]` 不是 `[x if x > 0 for x in lst]`
3. **generator 跟 list 混淆**：(x for x in lst) 是 generator，要 list(...) 才看得到
"""),
        ("✏️ 練習題", """1. 用推導式把 `[1,2,3,4,5]` 每個元素平方
2. 過濾出長度 > 3 的字串
3. 用推導式建立 `{i: i*2 for i in range(5)}`
4. 把一個 list 扁平化：`[[1,2],[3,4]]` → `[1,2,3,4]`
"""),
    ]),

    ("chapter01_basics/project.md", "第 1 章 · 基礎語法", "小專案: 通訊錄管理", "60 分鐘", "入門", [
        ("🎯 專案目標", """做一個命令列的**通訊錄管理程式**，整合本章所有概念：

- ✅ 變數、list、dict
- ✅ 函式
- ✅ 迴圈 + 條件
- ✅ f-string
- ✅ 串列推導式（加分）
"""),
        ("📋 需求", """| 功能 | 指令 | 說明 |
|---|---|---|
| 新增聯絡人 | `add` | 輸入名字、電話 |
| 查詢聯絡人 | `find` | 用名字查電話 |
| 列出全部 | `list` | 印出所有聯絡人 |
| 刪除聯絡人 | `delete` | 用名字刪 |
| 離開 | `quit` | 結束程式 |
"""),
        ("💻 完整程式碼", """```python
\"\"\"通訊錄管理 — 第 1 章小專案\"\"\"

contacts = {}  # name -> phone

def add_contact():
    name = input(\"姓名: \").strip()
    phone = input(\"電話: \").strip()
    contacts[name] = phone
    print(f\"✅ 已新增 {name}\")

def find_contact():
    name = input(\"要查詢的姓名: \").strip()
    phone = contacts.get(name)
    if phone:
        print(f\"📞 {name}: {phone}\")
    else:
        print(f\"❌ 找不到 {name}\")

def list_contacts():
    if not contacts:
        print(\"(通訊錄是空的)\")
        return
    print(\"=== 通訊錄 ===\")
    for name, phone in contacts.items():
        print(f\"  {name}: {phone}\")
    print(f\"共 {len(contacts)} 個聯絡人\")

def delete_contact():
    name = input(\"要刪除的姓名: \").strip()
    if name in contacts:
        del contacts[name]
        print(f\"🗑️ 已刪除 {name}\")
    else:
        print(f\"❌ 找不到 {name}\")

def main():
    actions = {
        \"add\": add_contact,
        \"find\": find_contact,
        \"list\": list_contacts,
        \"delete\": delete_contact,
    }
    while True:
        cmd = input(\"\\n指令 (add/find/list/delete/quit): \").strip().lower()
        if cmd == \"quit\":
            print(\"掰掰！\")
            break
        action = actions.get(cmd)
        if action:
            action()
        else:
            print(\"❓ 未知指令\")

if __name__ == \"__main__\":
    main()
```
"""),
        ("🚀 挑戰版（給想加碼的人）", """加上這些功能：

1. **電話格式驗證**：10 碼數字
2. **匯出 CSV**：把所有聯絡人存成 `.csv`
3. **從 CSV 載入**：開程式時讀取
4. **搜尋關鍵字**：用 `in` 模糊查
5. **分頁**：聯絡人太多時分頁顯示
"""),
        ("✅ 完成清單", """- [x] 我能解釋每行程式在做什麼
- [x] 我能新增、查詢、刪除聯絡人
- [x] 我加了至少 1 個挑戰版功能
- [x] 我把程式 push 到 GitHub
"""),
        ("📚 延伸閱讀", """- [Python 官方教學：資料結構](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python: List Comprehensions](https://realpython.com/list-comprehension-python/)
"""),
    ]),
]

# 寫所有
for relpath, chap, h1, time, level, blocks in SECTIONS:
    out = H(chap, h1, time, level)
    for sec_title, sec_content in blocks:
        out += f"## {sec_title}\n\n{sec_content}\n\n"
    full = ROOT / relpath
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(out, encoding="utf-8")
    print(f"✅ {relpath} ({len(out)} chars)")

print(f"\n生成 {len(SECTIONS)} 個檔案")
