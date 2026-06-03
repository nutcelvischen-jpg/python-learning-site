---
title: "0.2 安裝 Python"
---

<div class="lesson-header">
  <span class="chapter-tag">第 0 章 · 環境準備</span>
  <h1>安裝 Python</h1>
  <div class="meta">
    <span>⏱️ 10 分鐘</span>
    <span>🛠️ 必做</span>
    <span>💻 macOS / Windows / Linux</span>
  </div>
</div>

## 🎯 學習目標

- 在你的作業系統上**安裝 Python 3.11+**
- 驗證安裝成功（`python3 --version`）
- 知道 **pip** 怎麼用
- 避開常見的安裝雷

## 🍎 macOS 安裝（推薦 Homebrew）

```bash
# 1. 安裝 Homebrew（如果還沒裝）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. 安裝 Python
brew install python

# 3. 驗證
python3 --version
# 輸出：Python 3.13.7
```

!!! tip "Homebrew 是什麼？"

    macOS 的「套件管理員」，就像 App Store 但裝的是開發者工具。 [https://brew.sh](https://brew.sh)

### 替代方法：python.org 安裝檔

不想用 Homebrew 的人：

1. 開瀏覽器到 [https://www.python.org/downloads/macos/](https://www.python.org/downloads/macos/)
2. 點 **"Download Python 3.13.x"**（最新穩定版）
3. 開啟下載的 `.pkg`
4. 一直按「繼續」到底
5. 安裝完成後開啟**新的終端機視窗**（重要！）

## 🪟 Windows 安裝

### 方法 1：python.org 安裝檔（推薦新手）

1. 開瀏覽器到 [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. 點 **"Download Python 3.13.x"**
3. **⚠️ 重要**：在第一個畫面**勾選「Add Python to PATH」**（很多人忘記！）
4. 點「Install Now」
5. 安裝完成後，**關閉再開** PowerShell 或 cmd

### 方法 2：Microsoft Store

1. 開 Microsoft Store
2. 搜尋 "Python 3.11" 或更新版本
3. 點「取得」安裝

```powershell
# PowerShell 驗證
python --version
# 輸出：Python 3.13.7
```

## 🐧 Linux 安裝

大部份 Linux 發行版預設就有 Python。 如果要新版本：

=== "Ubuntu / Debian"

    ```bash
    sudo apt update
    sudo apt install python3.11 python3-pip
    python3 --version
    ```

=== "Fedora / RHEL"

    ```bash
    sudo dnf install python3.11 python3-pip
    python3 --version
    ```

=== "Arch"

    ```bash
    sudo pacman -S python python-pip
    python3 --version
    ```

## ✅ 驗證安裝

打開**新的**終端機（macOS Terminal / Windows PowerShell），執行：

```bash
python3 --version
# 應該看到 Python 3.11 以上

pip3 --version
# 應該看到 pip 23.0 以上
```

如果 `python3` 沒反應但 `python` 有，**那也是 OK 的** — Windows 上慣用 `python`，macOS / Linux 慣用 `python3`。

## 🚀 第一個互動式 Python

```bash
python3
```

你會看到類似：

```text
Python 3.13.7 (main, Aug 14 2025, 00:00:00)
[GCC 14.2.0] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>`.
```

這是 **Python REPL**（Read-Eval-Print Loop）— 你輸入一行 Python 程式，Python 立刻執行並顯示結果。

試試輸入：

```python
>>> print("Hello, Python!")
Hello, Python!
>>> 2 + 3
5
>>> import this
```

按 `Ctrl+D`（macOS / Linux）或 `Ctrl+Z` 然後 Enter（Windows）離開。

## ❗ 常見錯誤

### 1. 安裝完但 `python3` 找不到

**原因**：舊的 PATH 還在

**修正**：

- macOS / Linux：關閉終端機再開新的
- Windows：對「本機」按右鍵 → 內容 → 進階系統設定 → 環境變數 → 確認 Python 路徑有在 PATH

### 2. 裝了 Python 2.x

**修正**：用 `python3` 而不是 `python`，或重新裝 Python 3.11+

### 3. pip 報「permission denied」

**修正**：不要用 `sudo pip`！ 用虛擬環境（[第 2.6 章](../chapter02_intermediate/06-venv.md)）：

```bash
python3 -m venv myenv
source myenv/bin/activate
pip install 套件名
```

## 📚 延伸閱讀

- [Python 官方安裝教學](https://wiki.python.org/moin/BeginnersGuide/Download)
- [Homebrew 官網](https://brew.sh)
- [Real Python: Install Python](https://realpython.com/installing-python/)

---

下一課：[0.3 VS Code 設定](03-vscode.md) — 寫程式的好用編輯器 ✏️
