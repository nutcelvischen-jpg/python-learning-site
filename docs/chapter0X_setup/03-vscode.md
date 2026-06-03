---
title: "VS Code 設定"
---

<div class="lesson-header">
  <span class="chapter-tag">第 0 章 · 環境準備</span>
  <h1>VS Code 設定</h1>
  <div class="meta">
    <span>⏱️ 10 分鐘</span>
    <span>📖 🛠️ 必做</span>
    <span>🎯 VS Code 安裝 + Python 擴充 + 第一支程式</span>
  </div>
</div>

## 🎯 學習目標
- 安裝 VS Code 並設定為 Python 編輯器
- 安裝 Python 與 Jupyter 兩個必備擴充
- 學會用 VS Code 跑 .py 檔和 .ipynb notebook
- 認識 settings.json 怎麼改

## ⬇️ 安裝 VS Code
1. 開瀏覽器到 [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. 下載安裝檔並執行
3. macOS: 拖到 Applications
4. Windows: 一直下一步
5. Linux: 用 `snap` 或 `apt` 安裝

## 🔌 安裝必備擴充
打開 VS Code，按 `Cmd+Shift+X`（macOS）或 `Ctrl+Shift+X`（Windows）打開擴充市集，搜尋並安裝：

| 擴充 ID | 用途 |
|---|---|
| `ms-python.python` | Python 語言支援（必裝） |
| `ms-toolsai.jupyter` | Jupyter notebook 支援 |
| `ms-python.vscode-pylance` | Python 智慧提示 |
| `njpwerner.autodocstring` | 自動 docstring |

## ⚙️ 設定 Python interpreter
1. 按 `Cmd+Shift+P` 打開命令選擇
2. 輸入 "Python: Select Interpreter"
3. 選擇你剛安裝的 Python 3.11+

## ✏️ 第一支 .py 檔
1. 新增檔案 `hello.py`
2. 輸入：
```python
name = input('你叫什麼名字？ ')
print(f'哈囉 {name}！歡迎來到 Python 學堂！')
```
3. 按右上 ▶︎ 執行（或 `Ctrl+F5`）
4. 終端機會問你名字，輸入後看到歡迎訊息

## 📓 Jupyter notebook 模式
1. 安裝 Jupyter 擴充後，`.ipynb` 檔案可以直接開
2. 按 `+ Code` 加 cell
3. 輸入 `print('Hello')`
4. 按 `Shift+Enter` 執行

## 🎨 推薦設定（settings.json）
```json
{
  "editor.fontSize": 14,
  "editor.fontFamily": "JetBrains Mono, monospace",
  "editor.minimap.enabled": false,
  "editor.formatOnSave": true,
  "python.defaultInterpreterPath": "python3"
}
```

## ❗ 常見錯誤
1. **VS Code 找不到 Python** → 重選 interpreter
2. **擴充裝了沒反應** → 重啟 VS Code
3. **中文輸入亂碼** → 終端機設定 UTF-8

## 📚 延伸閱讀
- [VS Code Python 教學](https://code.visualstudio.com/docs/python/python-tutorial)
- [Jupyter in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks)

---

下一課：[0.4 Hello, Python!](04-hello.md) — 寫你人生第一支程式 ✨