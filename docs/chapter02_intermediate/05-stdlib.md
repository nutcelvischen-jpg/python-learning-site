---
title: "2.5 標準庫必備"
---

<div class="lesson-header">
  <span class="chapter-tag">第 2 章 · 進階基礎</span>
  <h1>2.5 標準庫必備</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 認識 Python 標準庫的 5 大必備模組
- `os` / `sys` / `datetime` / `json` / `pathlib`


## 📁 os / pathlib

```python
from pathlib import Path

p = Path("data/file.txt")
print(p.exists())           # 檔案是否存在
print(p.parent)             # 上層目錄
print(p.suffix)             # .txt
print(p.stem)               # file

p.write_text("Hello")      # 寫
print(p.read_text())        # 讀
```


## 📅 datetime

```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)                  # 2026-06-04 12:34:56.789

today = datetime(2026, 6, 4)
next_week = today + timedelta(days=7)
print(next_week)

# 格式化
print(now.strftime("%Y-%m-%d %H:%M"))  # 2026-06-04 12:34
```


## 📦 json

```python
import json

data = {"name": "Elvis", "age": 35}

# dict → JSON
s = json.dumps(data)
# JSON → dict
d = json.loads(s)

# 檔案
with open("data.json", "w") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```


## ❗ 常見錯誤

1. **JSON 不存中文**：`ensure_ascii=False` 才會保留中文
2. **datetime timezone**：naive vs aware datetime 別混


## ✏️ 練習題

1. 用 pathlib 列出資料夾所有 .py 檔
2. 算今天跟生日差幾天
3. 把 list 存成 JSON 再讀回來


