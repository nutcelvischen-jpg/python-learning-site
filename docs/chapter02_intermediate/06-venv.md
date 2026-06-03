---
title: "2.6 虛擬環境 venv"
---

<div class="lesson-header">
  <span class="chapter-tag">第 2 章 · 進階基礎</span>
  <h1>2.6 虛擬環境 venv</h1>
  <div class="meta">
    <span>⏱️ 15 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 知道為什麼要虛擬環境
- 學會建立 / 啟用 / 退出 venv
- 套件隔離的觀念


## ❓ 為什麼用 venv

每個專案用獨立的 Python 環境，避免套件版本衝突。

```bash
# 建立 venv
python3 -m venv myenv

# 啟用
source myenv/bin/activate   # macOS/Linux
# myenv\Scripts\activate    # Windows

# 看提示字元有 (myenv) 前綴就對了
(myenv) $ pip install 套件
(myenv) $ pip list

# 退出
deactivate
```


## 💡 套件安裝 vs 系統 Python

| 情境 | 指令 |
|---|---|
| 在 venv 裡裝 | `pip install pandas` |
| 全域裝（不推薦） | `sudo pip install pandas` |
| 看裝了什麼 | `pip list` |
| 凍版本 | `pip freeze > requirements.txt` |
| 從檔案裝 | `pip install -r requirements.txt` |


## ❗ 常見錯誤

1. **沒啟用就 pip install**：裝到系統 Python
2. **忘記 venv 名稱**：可以刪掉重建


## ✏️ 練習題

1. 建立一個 venv 叫 `pyclass`
2. 啟用後裝 `requests`
3. `pip freeze` 看結果
4. 退出後再 `pip list` 確認 requests 沒在全域


