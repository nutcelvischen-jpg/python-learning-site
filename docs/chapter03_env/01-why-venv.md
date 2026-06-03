---
title: "3.1 為什麼要環境隔離"
---

<div class="lesson-header">
  <span class="chapter-tag">第 3 章 · 環境管理</span>
  <h1>3.1 為什麼要環境隔離</h1>
  <div class="meta">
    <span>⏱️ 10 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 理解「依賴地獄」
- 知道不同專案用不同環境
- 認識常見環境管理工具


## 💥 依賴地獄

專案 A 用 `pandas 1.5`，專案 B 用 `pandas 2.0`，裝一起會壞。

!!! quote "慘案實例"

    "我用 `sudo pip install X` 結果整個系統 Python 壞掉，重新安裝花了一個下午。"


## 🛠️ 環境管理工具

| 工具 | 用途 |
|---|---|
| `venv` | 標準庫，輕量 |
| `virtualenv` | venv 加強版 |
| `conda` | 跨語言（適合生醫/AI） |
| `poetry` | 套件 + 環境 + lock |
| `uv` | Rust 寫的快版（推薦新案） |
| `pipenv` | pip + venv 整合 |


## ✏️ 練習題

1. 列出你電腦上現有的 Python 環境
2. 想一個你需要隔離的場景


