---
title: "2.7 pip 套件管理"
---

<div class="lesson-header">
  <span class="chapter-tag">第 2 章 · 進階基礎</span>
  <h1>2.7 pip 套件管理</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 學會 `pip install / uninstall / list / show`
- 用 `requirements.txt` 管理依賴
- 知道 wheel、PyPI 是什麼


## 📦 pip 常用指令

```bash
pip install 套件名                # 裝最新
pip install 套件名==1.2.3          # 裝特定版本
pip install 套件名>=2.0            # 至少 2.0
pip install -U 套件名              # 升級
pip uninstall 套件名               # 移除
pip list                          # 看所有已裝
pip show 套件名                    # 看詳細資訊
pip search 關鍵字                  # 搜尋（已 deprecated）
```


## 📄 requirements.txt

```text
# requirements.txt
pandas==2.2.0
numpy>=1.26
matplotlib
```

```bash
pip install -r requirements.txt
```


## ❗ 常見錯誤

1. **沒寫版本**：之後裝會裝新版可能壞掉
2. **A 套件依賴 B 套件**：不要直接動 B 的版本


## ✏️ 練習題

1. `pip list` 看你電腦裝了什麼
2. 建立 `requirements.txt` 含你這學期要用的套件
3. 在新 venv 從 requirements.txt 一次裝回


