---
title: "3.3 conda 簡介"
---

<div class="lesson-header">
  <span class="chapter-tag">第 3 章 · 環境管理</span>
  <h1>3.3 conda 簡介</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 知道 conda 適合什麼場景
- 學會基本 conda 指令
- miniconda vs anaconda


## 📦 conda 是什麼

conda 是跨語言的套件管理員，**特別適合**：

- 資料科學（裝 numpy、pandas 自動解決 C 依賴）
- 生醫（裝 Biopython、scanpy）
- ML（裝 PyTorch 含 CUDA）
- 環境複雜（混合 R + Python）


## 🛠️ conda 指令

```bash
# 建立環境
conda create -n myenv python=3.11

# 啟用
conda activate myenv

# 裝套件
conda install pandas numpy
# 或 pip install （在 conda 環境裡也行）

# 列出環境
conda env list

# 列出套件
conda list

# 離開
conda deactivate

# 移除環境
conda env remove -n myenv
```


## 💡 什麼時候用 venv vs conda

| 情境 | 推薦 |
|---|---|
| 一般 Python 專案 | venv |
| 純資料分析 | venv + pip |
| 裝 PyTorch with CUDA | conda |
| 生醫/化學複雜依賴 | conda |
| 要 R + Python | conda |
| 想用最新 ML 套件 | conda-forge |


## ✏️ 練習題

1. 列出你的 conda 環境
2. 看看哪個適合用 conda，哪個用 venv


