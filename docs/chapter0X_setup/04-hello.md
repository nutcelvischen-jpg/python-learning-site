---
title: "Hello, Python!"
---

<div class="lesson-header">
  <span class="chapter-tag">第 0 章 · 環境準備</span>
  <h1>Hello, Python!</h1>
  <div class="meta">
    <span>⏱️ 5 分鐘</span>
    <span>📖 🚀 必做</span>
    <span>🎯 寫第一行程式</span>
  </div>
</div>

## 🎯 學習目標
- 用 3 種方式執行你的第一個 Python 程式
- 學會 `print()` 和 `input()`
- 寫一支小程式跟自己打招呼

## 💻 方式 1：直接打 `python3`
在終端機打 `python3`，進入 REPL 模式：
```python
>>> print('Hello, World!')
Hello, World!
```

## 📝 方式 2：寫 .py 檔
新增 `hello.py`：
```python
# 我的第一支 Python 程式
name = input('你叫什麼名字？ ')
print(f'哈囉 {name}！歡迎來到 Python 學堂！ 🐍')
```
在終端機跑：`python3 hello.py`

## 📓 方式 3：Jupyter notebook
新增 cell：
```python
name = 'Elvis'
print(f'哈囉 {name}！')
```
按 `Shift+Enter`

## 🎯 練習：寫自我介紹
用 `input()` 問使用者：
- 名字
- 年齡
- 興趣
然後用 `f-string` 印出一段自我介紹

範例：
```python
name = input('你叫什麼名字？ ')
age = input('你幾歲？ ')
hobby = input('你的興趣是？ ')
print(f'=== 自我介紹 ===')
print(f'你好，我是 {name}')
print(f'{age} 歲')
print(f'興趣是 {hobby}')
print(f'很高興認識你！')
```

## ❗ 常見錯誤
1. `input()` 拿到的都是字串，要 `int(input())` 轉數字
2. `print(f'...')` 前面一定要小寫 f（format string）
3. 單引號跟雙引號要對稱

## 📚 延伸閱讀
- [print() 文件](https://docs.python.org/3/library/functions.html#print)
- [input() 文件](https://docs.python.org/3/library/functions.html#input)

---

下一課：[0.5 怎麼問問題 + Debug](05-how-to-ask.md) — 工程師最重要的技能 🔍