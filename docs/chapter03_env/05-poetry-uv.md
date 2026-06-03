---
title: "3.5 poetry / uv 現代化"
---

<div class="lesson-header">
  <span class="chapter-tag">第 3 章 · 環境管理</span>
  <h1>3.5 poetry / uv 現代化</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 認識 poetry 跟 uv
- 知道 `pyproject.toml` 是什麼
- 比較 poetry vs uv vs pip


## 🚀 uv 簡介（推薦）

uv 是 **Astral**（Ruff 同一公司）出的極速 Python 套件管理員，**Rust 寫的**。

```bash
# 安裝 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 建立專案
uv init myproject
cd myproject
uv add pandas
uv run python main.py
```


## 📜 pyproject.toml

```toml
[project]
name = "myproject"
version = "0.1.0"
dependencies = [
    "pandas>=2.2",
    "numpy>=1.26",
]

[tool.ruff]
line-length = 100
```


## ⚔️ 速度比較

| 工具 | 速度 |
|---|---|
| pip | 1x |
| poetry | 2-5x |
| uv | **10-100x** ⚡ |


## ✏️ 練習題

1. 安裝 uv
2. 用 `uv init` 建立一個專案
3. `uv add requests` 體驗速度


