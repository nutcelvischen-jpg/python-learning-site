---
title: "怎麼問問題 + Debug"
---

<div class="lesson-header">
  <span class="chapter-tag">第 0 章 · 環境準備</span>
  <h1>怎麼問問題 + Debug</h1>
  <div class="meta">
    <span>⏱️ 5 分鐘</span>
    <span>📖 🔍 必讀</span>
    <span>🎯 工程師最重要的 skill</span>
  </div>
</div>

## 🎯 學習目標
- 學會**看懂錯誤訊息**
- 知道**怎麼搜尋**錯誤
- 學會**怎麼問問題**（MCVE 原則）
- 學會用 `print()` debug

## 🔍 看懂錯誤訊息
Python 錯誤訊息有 3 個關鍵：
```
Traceback (most recent call last):
  File 'hello.py', line 3    ← 第幾行
    print(name)
NameError: name 'name' is not defined    ← 什麼錯
```
記住：**Traceback 最後一行才是錯誤類型**，上面的行號是「在哪裡發生」。

## 🔎 怎麼搜尋錯誤
1. **複製錯誤訊息最後一行**
2. **Google 搜尋**：`python NameError: name is not defined`
3. **前三個結果**通常有解答（Stack Overflow 為主）

## 📝 怎麼問問題（MCVE 原則）
**M**inimal **C**omplete **V**erifiable **E**xample — 最小可重現範例

好的問題：
```python
# 我想問：為什麼這個會錯？
x = 5
y = 0
print(x / y)  # 預期輸出 5，實際跳 ZeroDivisionError
```

不好的問題：
> 「我的程式壞了，怎麼辦？」 ← 沒人幫得了你

## 🦆 橡皮鴨法
把你的程式**一行一行唸給橡皮鴨聽**（或任何不會動的東西）。
當你試著解釋時，**自己就會發現 bug 在哪**。

這是工程師最常用的除錯技巧，聽起來很蠢但超有效。

## 🐛 print() Debug 大法
```python
def calculate(x, y):
    print(f'DEBUG: x={x}, y={y}')    # 追蹤變數
    result = x * y
    print(f'DEBUG: result={result}')
    return result

answer = calculate(3, 4)
```
在每個關鍵點 print，**找出哪裡不如預期**。

## ❗ 常見錯誤類型速查
| 錯誤 | 原因 | 修正 |
|---|---|---|
| `NameError` | 用到沒定義的變數 | 先檢查拼字 |
| `SyntaxError` | 語法錯（少括號、引號） | 看錯誤指標的位置 |
| `IndentationError` | 縮排錯 | Python 用 4 空格 |
| `TypeError` | 型別不對（字串+數字） | 轉型 str() / int() |
| `IndexError` | list 索引超出範圍 | 檢查長度 `len(list)` |
| `KeyError` | dict 沒這個 key | 用 `dict.get(key, default)` |
| `ZeroDivisionError` | 除以 0 | 加 if 判斷 |
| `FileNotFoundError` | 檔案不存在 | 檢查路徑 |

## 📚 延伸閱讀
- [How to ask questions](https://stackoverflow.com/help/how-to-ask)
- [Python 官方錯誤說明](https://docs.python.org/3/tutorial/errors.html)
- [Rubber duck debugging](https://en.wikipedia.org/wiki/Rubber_duck_debugging)

---

準備好了嗎？ → [第 1 章 基礎語法](../chapter01_basics/01-variables-types.md) 🚀