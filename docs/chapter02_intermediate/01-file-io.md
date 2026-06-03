---
title: "2.1 檔案讀寫"
---

<div class="lesson-header">
  <span class="chapter-tag">第 2 章 · 進階基礎</span>
  <h1>2.1 檔案讀寫</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 學會讀寫純文字檔（.txt）
- 學會讀寫 CSV 檔
- 用 `with` 確保檔案正確關閉
- 認識檔案編碼（UTF-8）


## 📖 讀檔

```python
# 推薦寫法：用 with 自動關檔
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()      # 一次讀全部
    print(content)
    # 或 f.readline() 讀一行
    # 或 f.readlines() 讀成 list
```


## ✏️ 寫檔

```python
text = "Hello, World!\n第二行"

# 寫入（覆蓋）
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(text)

# 附加（不覆蓋）
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("新的一行\n")
```


## 📊 CSV 讀寫

```python
import csv

# 讀 CSV
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# 寫 CSV
data = [
    {"name": "Elvis", "age": 35},
    {"name": "Bob", "age": 28}
]
with open("out.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerows(data)
```


## ❗ 常見錯誤

1. **忘了 encoding**：Windows 預設 cp950，中文會亂碼
2. **沒用 with**：檔案沒關可能會 lock
3. **CSV 沒 newline**：Windows 上會多空行


## ✏️ 練習題

1. 寫一個程式把自己的名字寫入 `me.txt`
2. 讀回 `me.txt` 印出來
3. 把 5 個朋友的名字跟電話寫成 CSV


