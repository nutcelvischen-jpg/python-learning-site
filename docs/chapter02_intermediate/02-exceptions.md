---
title: "2.2 例外處理"
---

<div class="lesson-header">
  <span class="chapter-tag">第 2 章 · 進階基礎</span>
  <h1>2.2 例外處理</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 學會 try / except / finally
- 認識常見例外類型
- 知道什麼時候用 try


## 🛡️ try / except

```python
try:
    n = int(input("輸入數字: "))
    print(f"你輸入的是 {n}")
except ValueError:
    print("❌ 請輸入正確的數字")
```


## 🎯 多個 except

```python
try:
    nums = [1, 2, 3]
    print(nums[10])          # IndexError
    result = 10 / 0          # ZeroDivisionError
except IndexError:
    print("索引超出範圍")
except ZeroDivisionError:
    print("不能除以 0")
except Exception as e:
    print(f"其他錯誤: {e}")
```


## 🧹 finally

```python
try:
    f = open("file.txt")
    # 做一些事
finally:
    f.close()                # 無論如何都會執行
    print("檔案已關閉")
```


## ❗ 常見錯誤

1. **包太大塊**：不要整個程式都 try
2. **吞掉錯誤**：except 一定要有處理
3. **順序錯**：先具體的 Exception 再通用的


## ✏️ 練習題

1. 寫一個計算機，遇到除以 0 不當機
2. 讀檔時處理 FileNotFoundError
3. 用 try 包一段 user input 轉 int


