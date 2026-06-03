---
title: "3.2 venv 完整教學"
---

<div class="lesson-header">
  <span class="chapter-tag">第 3 章 · 環境管理</span>
  <h1>3.2 venv 完整教學</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 完整掌握 venv 操作
- 了解 venv 目錄結構
- 在 IDE 裡選 venv


## 🛠️ 完整 venv 操作

```bash
# 建立
python3 -m venv .venv

# 啟用
source .venv/bin/activate

# 確認在 venv 裡
which python3      # 應該指向 .venv/bin/python3
which pip3         # 應該指向 .venv/bin/pip3

# 安裝套件
pip install pandas numpy

# 凍版本
pip freeze > requirements.txt

# 在別台機器重現
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 退出
deactivate
```


## 📁 .venv 目錄結構

```text
.venv/
├── bin/                    # macOS/Linux
│   ├── python3            # 虛擬 Python
│   ├── pip3
│   └── activate
├── lib/                    # 套件安裝處
├── include/                # C 標頭
└── pyvenv.cfg             # 設定檔
```


## 💻 VS Code 整合

1. `Cmd+Shift+P` → "Python: Select Interpreter"
2. 選 `.venv/bin/python3`
3. 之後 VS Code 就用 venv 跑 Python


## ✏️ 練習題

1. 建立一個 venv，裝 pandas，確認可以 `import pandas`
2. 退出後 `import pandas` 應該失敗
3. 重新啟用 venv 又可以


