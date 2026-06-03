---
title: "1.5 字典 dict 與集合 set"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.5 字典 dict 與集合 set</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 學會 dict（字典）的建立與操作
- 理解 key-value 配對
- 認識 set（集合）的去重特性
- 知道 dict.get() 的好處


## 📖 dict — 字典

```python
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


## 🔄 走訪 dict

```python
person = {"name": "Elvis", "age": 35, "city": "台中"}

for key in person:                # 走 key
    print(f"{key} = {person[key]}")

for key, value in person.items(): # 走 (key, value)
    print(f"{key}: {value}")

for value in person.values():     # 只走 value
    print(value)
```


## 🔧 dict 常用方法

```python
d = {"a": 1, "b": 2}
print(d.keys())       # dict_keys(['a', 'b'])
print(d.values())     # dict_values([1, 2])
print(d.items())      # dict_items([('a', 1), ('b', 2)])

d.update({"c": 3})    # 合併另一個 dict
d.pop("a")            # 移除並回傳
d.clear()             # 清空
```


## 🎯 set — 集合

set 是**無序、不重複**的元素集合，適合去重與集合運算。

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


## ❗ 常見錯誤

1. **KeyError**：用 `d[key]` 找不到會錯，用 `d.get(key, default)` 不會
2. **dict 沒有順序保證**（Python 3.7+ 維護插入順序但別依賴）
3. **set 不可索引**：`s[0]` 會錯，要 `list(s)[0]`


## ✏️ 練習題

1. 寫一個 dict 裝 3 個朋友的名字跟年齡
2. 走訪 dict 印出 `name: age` 格式
3. 把 list `[1,1,2,3,3,3,4]` 轉 set 看看
4. 算兩個 set 的交集、聯集、差集
5. 用 dict 計數一段文字中每個字出現幾次


