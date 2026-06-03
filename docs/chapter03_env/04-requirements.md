---
title: "3.4 requirements.txt"
---

<div class="lesson-header">
  <span class="chapter-tag">第 3 章 · 環境管理</span>
  <h1>3.4 requirements.txt</h1>
  <div class="meta">
    <span>⏱️ 10 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 寫好的 requirements.txt
- 用 pip-tools 管理依賴
- 知道 `--no-deps` 風險


## 📄 寫法

```text
# 嚴格版（推薦）
pandas==2.2.0
numpy==1.26.4
matplotlib==3.8.2

# 寬鬆版
pandas>=2.2
numpy~=1.26.4   # >=1.26.4, <1.27
```


## 🛠️ 進階：分層 requirements

```text
# requirements/base.txt
pandas>=2.2
numpy>=1.26

# requirements/dev.txt  (包含 base)
-r base.txt
pytest>=7
black>=24
```


## ✏️ 練習題

1. 把你目前 venv 的套件凍成 requirements.txt
2. 試試 `pip install -r` 在新 venv


