---
title: "1.3 字串處理"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.3 字串處理</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 學會字串建立、索引、切片
- 常用字串方法：upper/lower/split/replace/strip
- 學會 f-string 格式化
- 處理中文與特殊字元


## 📜 字串建立

```python
s1 = '單引號'
s2 = "雙引號"
s3 = '''三引號可以
跨多行'''
print(s3)
```


## 🔪 索引與切片

```python
s = "Hello, World!"
#    0123456789...

print(s[0])      # 'H'  第一個字
print(s[-1])     # '!'  最後一個
print(s[0:5])    # 'Hello' 切片 [起:訖]
print(s[7:])     # 'World!' 從 7 開始到最後
print(s[:5])     # 'Hello' 從頭到 5
print(s[::2])    # 'Hlo ol!' 步長 2
```


## 🎨 f-string 格式化（必學！）

```python
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


## 🔧 常用字串方法

```python
s = "  Hello, Python!  "
print(s.strip())           # 去掉頭尾空白
print(s.upper())           # 全大寫
print(s.lower())           # 全小寫
print(s.replace("Hello", "Hi"))
print("a,b,c".split(","))  # ['a', 'b', 'c']
print(",".join(['a','b','c']))  # "a,b,c"
print("Hello" in s)        # True（包含檢查）
```


## ❗ 常見錯誤

1. **中英文混用索引**：中文一個字佔 3 bytes，但 `len()` 看字元數
2. **字串不可改**：`s[0] = 'h'` 會錯！ 要用 replace
3. **f-string 忘了 f**：`"Hello {name}"` 不會格式化


## ✏️ 練習題

1. 把 `"  python  "` 用 `strip()` 清乾淨
2. 用 slice 反轉字串 `"Hello"` → `"olleH"`
3. f-string 印出 1/3 保留 4 位小數
4. `"a,b,c,d".split(",")` 的結果是什麼？
5. 寫一個程式問名字，印出名字的長度


