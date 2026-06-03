---
title: "B. 常見錯誤 FAQ"
---

<div class="lesson-header">
  <span class="chapter-tag">附錄 B</span>
  <h1>B. 常見錯誤 FAQ</h1>
  <div class="meta">
    <span>⏱️ 10 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 疑難排解</span>
  </div>
</div>

## 🔥 Top 30 錯誤

| 錯誤 | 原因 | 修正 |
|---|---|---|
| `SyntaxError: EOL` | 沒關引號 | 檢查所有引號 |
| `NameError` | 變數沒定義 | 先宣告 |
| `TypeError: ... + int` | 字串加數字 | 用 str(int) |
| `IndexError` | list 越界 | 檢查 len |
| `KeyError` | dict 沒這 key | 用 .get() |
| `IndentationError` | 縮排錯 | 4 空格統一 |
| `AttributeError: 'NoneType'` | None 呼叫方法 | 檢查 None |
| `ZeroDivisionError` | 除以 0 | 加 if |
| `FileNotFoundError` | 檔不存在 | 檢查路徑 |
| `ModuleNotFoundError` | 套件沒裝 | pip install |


## 🔍 Debug 三步

1. **讀錯誤訊息最後一行**
2. **看 Traceback 行號**
3. **用 print() 看變數**


