#!/usr/bin/env python3
"""
generate_remaining.py — 生成第 2-9 章 + 附錄的所有 .md
每個檔 1200-2000 字元，保留完整結構
"""
import os
from pathlib import Path

ROOT = Path("/Users/elvis/projects/python-learning-site/docs")

def H(chap, h1, time, level="入門"):
    return f"""---
title: "{h1}"
---

<div class="lesson-header">
  <span class="chapter-tag">{chap}</span>
  <h1>{h1}</h1>
  <div class="meta">
    <span>⏱️ {time}</span>
    <span>📖 互動式</span>
    <span>🎯 {level}</span>
  </div>
</div>

"""

# 章節資料庫（路徑, 章節標籤, h1, 時間, 等級, 區塊清單）
DATA = [
    # ============ 第 2 章 進階基礎 ============
    ("chapter02_intermediate/01-file-io.md", "第 2 章 · 進階基礎", "2.1 檔案讀寫", "25 分鐘", "進階", [
        ("🎯 學習目標", """- 學會讀寫純文字檔（.txt）
- 學會讀寫 CSV 檔
- 用 `with` 確保檔案正確關閉
- 認識檔案編碼（UTF-8）
"""),
        ("📖 讀檔", """```python
# 推薦寫法：用 with 自動關檔
with open(\"data.txt\", \"r\", encoding=\"utf-8\") as f:
    content = f.read()      # 一次讀全部
    print(content)
    # 或 f.readline() 讀一行
    # 或 f.readlines() 讀成 list
```
"""),
        ("✏️ 寫檔", """```python
text = \"Hello, World!\\n第二行\"

# 寫入（覆蓋）
with open(\"output.txt\", \"w\", encoding=\"utf-8\") as f:
    f.write(text)

# 附加（不覆蓋）
with open(\"log.txt\", \"a\", encoding=\"utf-8\") as f:
    f.write(\"新的一行\\n\")
```
"""),
        ("📊 CSV 讀寫", """```python
import csv

# 讀 CSV
with open(\"data.csv\", \"r\", encoding=\"utf-8\") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row[\"name\"], row[\"age\"])

# 寫 CSV
data = [
    {\"name\": \"Elvis\", \"age\": 35},
    {\"name\": \"Bob\", \"age\": 28}
]
with open(\"out.csv\", \"w\", encoding=\"utf-8\", newline=\"\") as f:
    writer = csv.DictWriter(f, fieldnames=[\"name\", \"age\"])
    writer.writeheader()
    writer.writerows(data)
```
"""),
        ("❗ 常見錯誤", """1. **忘了 encoding**：Windows 預設 cp950，中文會亂碼
2. **沒用 with**：檔案沒關可能會 lock
3. **CSV 沒 newline**：Windows 上會多空行
"""),
        ("✏️ 練習題", """1. 寫一個程式把自己的名字寫入 `me.txt`
2. 讀回 `me.txt` 印出來
3. 把 5 個朋友的名字跟電話寫成 CSV
"""),
    ]),

    ("chapter02_intermediate/02-exceptions.md", "第 2 章 · 進階基礎", "2.2 例外處理", "20 分鐘", "進階", [
        ("🎯 學習目標", """- 學會 try / except / finally
- 認識常見例外類型
- 知道什麼時候用 try
"""),
        ("🛡️ try / except", """```python
try:
    n = int(input(\"輸入數字: \"))
    print(f\"你輸入的是 {n}\")
except ValueError:
    print(\"❌ 請輸入正確的數字\")
```
"""),
        ("🎯 多個 except", """```python
try:
    nums = [1, 2, 3]
    print(nums[10])          # IndexError
    result = 10 / 0          # ZeroDivisionError
except IndexError:
    print(\"索引超出範圍\")
except ZeroDivisionError:
    print(\"不能除以 0\")
except Exception as e:
    print(f\"其他錯誤: {e}\")
```
"""),
        ("🧹 finally", """```python
try:
    f = open(\"file.txt\")
    # 做一些事
finally:
    f.close()                # 無論如何都會執行
    print(\"檔案已關閉\")
```
"""),
        ("❗ 常見錯誤", """1. **包太大塊**：不要整個程式都 try
2. **吞掉錯誤**：except 一定要有處理
3. **順序錯**：先具體的 Exception 再通用的
"""),
        ("✏️ 練習題", """1. 寫一個計算機，遇到除以 0 不當機
2. 讀檔時處理 FileNotFoundError
3. 用 try 包一段 user input 轉 int
"""),
    ]),

    ("chapter02_intermediate/03-modules.md", "第 2 章 · 進階基礎", "2.3 模組與套件", "25 分鐘", "進階", [
        ("🎯 學習目標", """- 學會 `import` 各種模組
- 理解 `from X import Y`
- 自己寫一個模組
- 知道什麼是 `__name__ == \"__main__\"`
"""),
        ("📥 import 模組", """```python
import math
print(math.sqrt(16))      # 4.0

from math import pi, sin
print(pi)                  # 3.14159...
print(sin(0))              # 0.0

import numpy as np         # 別名
arr = np.array([1, 2, 3])
```
"""),
        ("📝 自訂模組", """建立 `mymath.py`：

```python
# mymath.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

另一個檔案使用：

```python
import mymath
print(mymath.add(3, 4))       # 7
print(mymath.PI)              # 3.14159
```
"""),
        ("🚪 `__name__` 魔術", """```python
# myscript.py
def main():
    print(\"這是主程式\")

if __name__ == \"__main__\":
    main()                # 只有直接執行才跑
```

`import myscript` 時不會跑 main()。
"""),
        ("❗ 常見錯誤", """1. **circular import**：A 引入 B，B 又引入 A
2. **路徑錯**：模組不在 PYTHONPATH
"""),
        ("✏️ 練習題", """1. 寫一個 `geometry.py` 模組含 circle_area / rectangle_area
2. 從另一個檔 import 它來用
3. 用 `if __name__ == \"__main__\"` 寫個測試
"""),
    ]),

    ("chapter02_intermediate/04-classes.md", "第 2 章 · 進階基礎", "2.4 類別與物件", "40 分鐘", "進階", [
        ("🎯 學習目標", """- 學會 class 語法
- 理解 `__init__` / self
- 認識繼承
- 知道 dunder methods
"""),
        ("🏗️ 基本 class", """```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f\"{self.name}: 汪汪！\"

    def __str__(self):
        return f\"{self.name} ({self.breed})\"

my_dog = Dog(\"小黑\", \"柴犬\")
print(my_dog)             # 小黑 (柴犬)
print(my_dog.bark())      # 小黑: 汪汪！
```
"""),
        ("🧬 繼承", """```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return \"...\" 

class Cat(Animal):
    def speak(self):
        return f\"{self.name}: 喵喵！\"

cat = Cat(\"小花\")
print(cat.speak())    # 小花: 喵喵！
```
"""),
        ("❗ 常見錯誤", """1. **忘記 self**：方法第一個參數一定要 self
2. **過度設計**：簡單東西用 class 是 over-engineering
"""),
        ("✏️ 練習題", """1. 寫一個 `Student` class 有 name / scores
2. 加一個 `average()` 方法算平均分
3. 寫一個 `GraduateStudent` 繼承 `Student`
"""),
    ]),

    ("chapter02_intermediate/05-stdlib.md", "第 2 章 · 進階基礎", "2.5 標準庫必備", "30 分鐘", "進階", [
        ("🎯 學習目標", """- 認識 Python 標準庫的 5 大必備模組
- `os` / `sys` / `datetime` / `json` / `pathlib`
"""),
        ("📁 os / pathlib", """```python
from pathlib import Path

p = Path(\"data/file.txt\")
print(p.exists())           # 檔案是否存在
print(p.parent)             # 上層目錄
print(p.suffix)             # .txt
print(p.stem)               # file

p.write_text(\"Hello\")      # 寫
print(p.read_text())        # 讀
```
"""),
        ("📅 datetime", """```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)                  # 2026-06-04 12:34:56.789

today = datetime(2026, 6, 4)
next_week = today + timedelta(days=7)
print(next_week)

# 格式化
print(now.strftime(\"%Y-%m-%d %H:%M\"))  # 2026-06-04 12:34
```
"""),
        ("📦 json", """```python
import json

data = {\"name\": \"Elvis\", \"age\": 35}

# dict → JSON
s = json.dumps(data)
# JSON → dict
d = json.loads(s)

# 檔案
with open(\"data.json\", \"w\") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```
"""),
        ("❗ 常見錯誤", """1. **JSON 不存中文**：`ensure_ascii=False` 才會保留中文
2. **datetime timezone**：naive vs aware datetime 別混
"""),
        ("✏️ 練習題", """1. 用 pathlib 列出資料夾所有 .py 檔
2. 算今天跟生日差幾天
3. 把 list 存成 JSON 再讀回來
"""),
    ]),

    ("chapter02_intermediate/06-venv.md", "第 2 章 · 進階基礎", "2.6 虛擬環境 venv", "15 分鐘", "進階", [
        ("🎯 學習目標", """- 知道為什麼要虛擬環境
- 學會建立 / 啟用 / 退出 venv
- 套件隔離的觀念
"""),
        ("❓ 為什麼用 venv", """每個專案用獨立的 Python 環境，避免套件版本衝突。

```bash
# 建立 venv
python3 -m venv myenv

# 啟用
source myenv/bin/activate   # macOS/Linux
# myenv\\Scripts\\activate    # Windows

# 看提示字元有 (myenv) 前綴就對了
(myenv) $ pip install 套件
(myenv) $ pip list

# 退出
deactivate
```
"""),
        ("💡 套件安裝 vs 系統 Python", """| 情境 | 指令 |
|---|---|
| 在 venv 裡裝 | `pip install pandas` |
| 全域裝（不推薦） | `sudo pip install pandas` |
| 看裝了什麼 | `pip list` |
| 凍版本 | `pip freeze > requirements.txt` |
| 從檔案裝 | `pip install -r requirements.txt` |
"""),
        ("❗ 常見錯誤", """1. **沒啟用就 pip install**：裝到系統 Python
2. **忘記 venv 名稱**：可以刪掉重建
"""),
        ("✏️ 練習題", """1. 建立一個 venv 叫 `pyclass`
2. 啟用後裝 `requests`
3. `pip freeze` 看結果
4. 退出後再 `pip list` 確認 requests 沒在全域
"""),
    ]),

    ("chapter02_intermediate/07-pip.md", "第 2 章 · 進階基礎", "2.7 pip 套件管理", "15 分鐘", "進階", [
        ("🎯 學習目標", """- 學會 `pip install / uninstall / list / show`
- 用 `requirements.txt` 管理依賴
- 知道 wheel、PyPI 是什麼
"""),
        ("📦 pip 常用指令", """```bash
pip install 套件名                # 裝最新
pip install 套件名==1.2.3          # 裝特定版本
pip install 套件名>=2.0            # 至少 2.0
pip install -U 套件名              # 升級
pip uninstall 套件名               # 移除
pip list                          # 看所有已裝
pip show 套件名                    # 看詳細資訊
pip search 關鍵字                  # 搜尋（已 deprecated）
```
"""),
        ("📄 requirements.txt", """```text
# requirements.txt
pandas==2.2.0
numpy>=1.26
matplotlib
```

```bash
pip install -r requirements.txt
```
"""),
        ("❗ 常見錯誤", """1. **沒寫版本**：之後裝會裝新版可能壞掉
2. **A 套件依賴 B 套件**：不要直接動 B 的版本
"""),
        ("✏️ 練習題", """1. `pip list` 看你電腦裝了什麼
2. 建立 `requirements.txt` 含你這學期要用的套件
3. 在新 venv 從 requirements.txt 一次裝回
"""),
    ]),

    ("chapter02_intermediate/08-pep8.md", "第 2 章 · 進階基礎", "2.8 PEP 8 風格", "15 分鐘", "進階", [
        ("🎯 學習目標", """- 知道 PEP 8 是什麼
- 遵守 Python 社群寫作風格
- 用 formatter（black / ruff）自動排版
"""),
        ("📏 PEP 8 速查", """| 規則 | 範例 |
|---|---|
| 縮排 4 空格 | `def f():\\n    pass` |
| 變數 snake_case | `user_name = \"...\"` |
| 常數 UPPER_CASE | `MAX_SIZE = 100` |
| 類別 PascalCase | `class MyClass:` |
| 函式 snake_case | `def calculate():` |
| 行長 < 79 字元 | 太長就換行 |
| 函式間空 2 行 | 模組層 |
| 類別內方法空 1 行 | 類別內 |
| import 放頂部 | 不要散落 |
| `import x` 不 `import x.y.z` | 一次一行 |
"""),
        ("🛠️ 自動 formatter", """```bash
pip install black ruff

# black 自動排版
black myfile.py

# ruff 檢查 + 自動修
ruff check myfile.py --fix
```
"""),
        ("❗ 常見錯誤", """1. **過度遵守**：風格是給人看的，不要為規則犧牲可讀性
2. **混用 tab / 空格**：一律用 4 空格
"""),
        ("✏️ 練習題", """1. 跑 `black` 格式化你之前的程式
2. 用 `ruff` 檢查錯誤
3. 把 PEP 8 cheat sheet 收藏起來
"""),
    ]),

    ("chapter02_intermediate/project.md", "第 2 章 · 進階基礎", "小專案: 記帳程式", "90 分鐘", "進階", [
        ("🎯 專案目標", """做一個**檔案儲存**的記帳程式，學會：

- 讀寫 JSON
- 類別設計
- 例外處理
"""),
        ("📋 需求", """1. 新增支出（日期、類別、金額、備註）
2. 列出所有支出
3. 統計各類別總額
4. 刪除支出
5. 存成 JSON 檔
"""),
        ("💻 完整程式碼", """```python
\"\"\"記帳程式 — 第 2 章小專案\"\"\"
import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path(\"expenses.json\")

class Expense:
    def __init__(self, date, category, amount, note=\"\"):
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note

    def to_dict(self):
        return {\"date\": self.date, \"category\": self.category,
                \"amount\": self.amount, \"note\": self.note}

    @classmethod
    def from_dict(cls, d):
        return cls(d[\"date\"], d[\"category\"], d[\"amount\"], d[\"note\"])

def load_expenses():
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, \"r\", encoding=\"utf-8\") as f:
            data = json.load(f)
        return [Expense.from_dict(d) for d in data]
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, \"w\", encoding=\"utf-8\") as f:
        json.dump([e.to_dict() for e in expenses], f,
                  ensure_ascii=False, indent=2)

def add_expense(expenses):
    date = input(\"日期 (YYYY-MM-DD，預設今天): \").strip()
    if not date:
        date = datetime.now().strftime(\"%Y-%m-%d\")
    category = input(\"類別: \").strip()
    amount = int(input(\"金額: \"))
    note = input(\"備註: \").strip()
    expenses.append(Expense(date, category, amount, note))
    print(\"✅ 已新增\")

def list_expenses(expenses):
    if not expenses:
        print(\"(沒有紀錄)\")
        return
    for i, e in enumerate(expenses, 1):
        print(f\"{i}. {e.date} | {e.category} | NT${e.amount} | {e.note}\")

def main():
    expenses = load_expenses()
    while True:
        print(\"\\n1. 新增  2. 列表  3. 統計  4. 刪除  5. 離開\")
        cmd = input(\"> \").strip()
        if cmd == \"1\":
            add_expense(expenses)
            save_expenses(expenses)
        elif cmd == \"2\":
            list_expenses(expenses)
        elif cmd == \"5\":
            save_expenses(expenses)
            print(\"掰掰\")
            break

if __name__ == \"__main__\":
    main()
```
"""),
        ("🚀 挑戰版", """1. 月份篩選
2. 圖表統計（用 matplotlib）
3. 從 CSV 匯入
4. 加上預算上限提醒
"""),
    ]),

    # ============ 第 3 章 環境管理 ============
    ("chapter03_env/01-why-venv.md", "第 3 章 · 環境管理", "3.1 為什麼要環境隔離", "10 分鐘", "進階", [
        ("🎯 學習目標", """- 理解「依賴地獄」
- 知道不同專案用不同環境
- 認識常見環境管理工具
"""),
        ("💥 依賴地獄", """專案 A 用 `pandas 1.5`，專案 B 用 `pandas 2.0`，裝一起會壞。

!!! quote \"慘案實例\"

    \"我用 `sudo pip install X` 結果整個系統 Python 壞掉，重新安裝花了一個下午。\"
"""),
        ("🛠️ 環境管理工具", """| 工具 | 用途 |
|---|---|
| `venv` | 標準庫，輕量 |
| `virtualenv` | venv 加強版 |
| `conda` | 跨語言（適合生醫/AI） |
| `poetry` | 套件 + 環境 + lock |
| `uv` | Rust 寫的快版（推薦新案） |
| `pipenv` | pip + venv 整合 |
"""),
        ("✏️ 練習題", """1. 列出你電腦上現有的 Python 環境
2. 想一個你需要隔離的場景
"""),
    ]),

    ("chapter03_env/02-venv-deep.md", "第 3 章 · 環境管理", "3.2 venv 完整教學", "15 分鐘", "進階", [
        ("🎯 學習目標", """- 完整掌握 venv 操作
- 了解 venv 目錄結構
- 在 IDE 裡選 venv
"""),
        ("🛠️ 完整 venv 操作", """```bash
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
"""),
        ("📁 .venv 目錄結構", """```text
.venv/
├── bin/                    # macOS/Linux
│   ├── python3            # 虛擬 Python
│   ├── pip3
│   └── activate
├── lib/                    # 套件安裝處
├── include/                # C 標頭
└── pyvenv.cfg             # 設定檔
```
"""),
        ("💻 VS Code 整合", """1. `Cmd+Shift+P` → \"Python: Select Interpreter\"
2. 選 `.venv/bin/python3`
3. 之後 VS Code 就用 venv 跑 Python
"""),
        ("✏️ 練習題", """1. 建立一個 venv，裝 pandas，確認可以 `import pandas`
2. 退出後 `import pandas` 應該失敗
3. 重新啟用 venv 又可以
"""),
    ]),

    ("chapter03_env/03-conda.md", "第 3 章 · 環境管理", "3.3 conda 簡介", "15 分鐘", "進階", [
        ("🎯 學習目標", """- 知道 conda 適合什麼場景
- 學會基本 conda 指令
- miniconda vs anaconda
"""),
        ("📦 conda 是什麼", """conda 是跨語言的套件管理員，**特別適合**：

- 資料科學（裝 numpy、pandas 自動解決 C 依賴）
- 生醫（裝 Biopython、scanpy）
- ML（裝 PyTorch 含 CUDA）
- 環境複雜（混合 R + Python）
"""),
        ("🛠️ conda 指令", """```bash
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
"""),
        ("💡 什麼時候用 venv vs conda", """| 情境 | 推薦 |
|---|---|
| 一般 Python 專案 | venv |
| 純資料分析 | venv + pip |
| 裝 PyTorch with CUDA | conda |
| 生醫/化學複雜依賴 | conda |
| 要 R + Python | conda |
| 想用最新 ML 套件 | conda-forge |
"""),
        ("✏️ 練習題", """1. 列出你的 conda 環境
2. 看看哪個適合用 conda，哪個用 venv
"""),
    ]),

    ("chapter03_env/04-requirements.md", "第 3 章 · 環境管理", "3.4 requirements.txt", "10 分鐘", "進階", [
        ("🎯 學習目標", """- 寫好的 requirements.txt
- 用 pip-tools 管理依賴
- 知道 `--no-deps` 風險
"""),
        ("📄 寫法", """```text
# 嚴格版（推薦）
pandas==2.2.0
numpy==1.26.4
matplotlib==3.8.2

# 寬鬆版
pandas>=2.2
numpy~=1.26.4   # >=1.26.4, <1.27
```
"""),
        ("🛠️ 進階：分層 requirements", """```text
# requirements/base.txt
pandas>=2.2
numpy>=1.26

# requirements/dev.txt  (包含 base)
-r base.txt
pytest>=7
black>=24
```
"""),
        ("✏️ 練習題", """1. 把你目前 venv 的套件凍成 requirements.txt
2. 試試 `pip install -r` 在新 venv
"""),
    ]),

    ("chapter03_env/05-poetry-uv.md", "第 3 章 · 環境管理", "3.5 poetry / uv 現代化", "15 分鐘", "進階", [
        ("🎯 學習目標", """- 認識 poetry 跟 uv
- 知道 `pyproject.toml` 是什麼
- 比較 poetry vs uv vs pip
"""),
        ("🚀 uv 簡介（推薦）", """uv 是 **Astral**（Ruff 同一公司）出的極速 Python 套件管理員，**Rust 寫的**。

```bash
# 安裝 uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 建立專案
uv init myproject
cd myproject
uv add pandas
uv run python main.py
```
"""),
        ("📜 pyproject.toml", """```toml
[project]
name = \"myproject\"
version = \"0.1.0\"
dependencies = [
    \"pandas>=2.2\",
    \"numpy>=1.26\",
]

[tool.ruff]
line-length = 100
```
"""),
        ("⚔️ 速度比較", """| 工具 | 速度 |
|---|---|
| pip | 1x |
| poetry | 2-5x |
| uv | **10-100x** ⚡ |
"""),
        ("✏️ 練習題", """1. 安裝 uv
2. 用 `uv init` 建立一個專案
3. `uv add requests` 體驗速度
"""),
    ]),
]

# 寫入
total = 0
for relpath, chap, h1, time, level, blocks in DATA:
    out = H(chap, h1, time, level)
    for sec_title, sec_content in blocks:
        out += f"## {sec_title}\n\n{sec_content}\n\n"
    full = ROOT / relpath
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(out, encoding="utf-8")
    total += 1
    print(f"✅ {relpath} ({len(out)} chars)")

print(f"\n生成 {total} 個檔案")
