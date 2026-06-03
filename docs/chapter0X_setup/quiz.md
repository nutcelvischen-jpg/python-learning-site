---
title: "第 0 章 小測驗"
---

<div class="lesson-header">
  <span class="chapter-tag">第 0 章 · 環境準備</span>
  <h1>第 0 章 小測驗</h1>
  <div class="meta">
    <span>⏱️ 10 分鐘</span>
    <span>📖 📝 自我檢測</span>
    <span>🎯 複習 + 確認學習成效</span>
  </div>
</div>

## 📝 選擇題（10 題）

??? question "Q1. 為什麼要學 Python？"
    - A) Python 是最快的程式語言
    - B) Python 語法簡潔、套件多、社群大
    - C) 只能用 Python 做網站
    - D) 只能在 macOS 用

    ??? success "答案"
        ✅ **B** — Python 的優勢在語法簡潔、套件多、社群大。

??? question "Q2. Python 官方網站是哪個？"
    - A) python.com
    - B) python.org
    - C) python.dev
    - D) python.net

    ??? success "答案"
        ✅ **B** — [https://www.python.org](https://www.python.org)

??? question "Q3. macOS 安裝 Python 最推的方式是？"
    - A) Microsoft Store
    - B) 下載 .pkg 從官網
    - C) Homebrew
    - D) 不用裝，macOS 內建就有

    ??? success "答案"
        ✅ **C** — Homebrew 是 macOS 開發者最常用方式。

??? question "Q4. VS Code 必裝的 Python 擴充 ID 是？"
    - A) python-vscode
    - B) ms-python.python
    - C) python-extension
    - D) py-vscode

    ??? success "答案"
        ✅ **B** — `ms-python.python`

??? question "Q5. `print('Hi')` 的輸出是？"
    - A) Hi（無引號）
    - B) 'Hi'
    - C) \"Hi\"
    - D) error

    ??? success "答案"
        ✅ **A** — 螢幕只印 Hi 兩個字元

??? question "Q6. `input()` 拿到的值是什麼型別？"
    - A) 數字
    - B) 浮點數
    - C) 字串
    - D) 布林

    ??? success "答案"
        ✅ **C** — `input()` 永遠回傳字串，要數字要 `int(input())`

??? question "Q7. Python 錯誤訊息的最後一行是什麼？"
    - A) 發生錯誤的行號
    - B) 錯誤類型
    - C) 函式名
    - D) 變數名

    ??? success "答案"
        ✅ **B** — 最後一行是錯誤類型（如 NameError、TypeError）

??? question "Q8. 哪個不是 Python 編輯器？"
    - A) VS Code
    - B) PyCharm
    - C) Jupyter Notebook
    - D) Microsoft Word

    ??? success "答案"
        ✅ **D** — Word 是文書處理軟體，不能寫程式

??? question "Q9. 問問題的 MCVE 是什麼縮寫？"
    - A) Most Common Version Editor
    - B) Minimal Complete Verifiable Example
    - C) My Code Very Easy
    - D) Module Class Variable Error

    ??? success "答案"
        ✅ **B** — Minimal Complete Verifiable Example（最小可重現範例）

??? question "Q10. 哪個 Python 版本推薦使用？"
    - A) Python 2.7
    - B) Python 3.6
    - C) Python 3.11+
    - D) Python 4.0

    ??? success "答案"
        ✅ **C** — Python 3.11+ 推薦，2.7 已停止維護

## 💻 實作題（5 題）
完整答案在 [附錄 E](../appendix/E-answers.md)，**先自己寫再看**。

### 練習 1：自我介紹
寫一個程式問使用者 3 個問題（名字、年齡、興趣），然後印出自我介紹。

### 練習 2：簡單計算機
寫一個程式問使用者兩個數字，印出他們的和、差、積、商。

### 練習 3：溫度轉換
寫一個程式把攝氏轉華氏：`F = C * 9/5 + 32`

### 練習 4：BMI 計算
輸入體重 (kg) 跟身高 (cm)，輸出 BMI。 `BMI = 體重 / (身高/100)²`

### 練習 5：Debug 練習
這段程式有 3 個錯，請找出來並修正：
```python
name = input(你叫什麼名字？)
age = int(input('你幾歲？ ')
print(f'你是 {name}, {Age} 歲')
```

## 🎯 過關標準
- 選擇題 ≥ 8 題對（80%）
- 實作題至少完成 3 題

**達標了？** → [第 1 章 基礎語法](../chapter01_basics/01-variables-types.md) 🚀
**沒達標？** → 回去重看 [0.2](02-install.md) / [0.3](03-vscode.md) / [0.4](04-hello.md)