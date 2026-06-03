---
title: "小專案: 記帳程式"
---

<div class="lesson-header">
  <span class="chapter-tag">第 2 章 · 進階基礎</span>
  <h1>小專案: 記帳程式</h1>
  <div class="meta">
    <span>⏱️ 90 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 專案目標

做一個**檔案儲存**的記帳程式，學會：

- 讀寫 JSON
- 類別設計
- 例外處理


## 📋 需求

1. 新增支出（日期、類別、金額、備註）
2. 列出所有支出
3. 統計各類別總額
4. 刪除支出
5. 存成 JSON 檔


## 💻 完整程式碼

```python
"""記帳程式 — 第 2 章小專案"""
import json
from datetime import datetime
from pathlib import Path

DATA_FILE = Path("expenses.json")

class Expense:
    def __init__(self, date, category, amount, note=""):
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note

    def to_dict(self):
        return {"date": self.date, "category": self.category,
                "amount": self.amount, "note": self.note}

    @classmethod
    def from_dict(cls, d):
        return cls(d["date"], d["category"], d["amount"], d["note"])

def load_expenses():
    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Expense.from_dict(d) for d in data]
    except json.JSONDecodeError:
        return []

def save_expenses(expenses):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump([e.to_dict() for e in expenses], f,
                  ensure_ascii=False, indent=2)

def add_expense(expenses):
    date = input("日期 (YYYY-MM-DD，預設今天): ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category = input("類別: ").strip()
    amount = int(input("金額: "))
    note = input("備註: ").strip()
    expenses.append(Expense(date, category, amount, note))
    print("✅ 已新增")

def list_expenses(expenses):
    if not expenses:
        print("(沒有紀錄)")
        return
    for i, e in enumerate(expenses, 1):
        print(f"{i}. {e.date} | {e.category} | NT${e.amount} | {e.note}")

def main():
    expenses = load_expenses()
    while True:
        print("\n1. 新增  2. 列表  3. 統計  4. 刪除  5. 離開")
        cmd = input("> ").strip()
        if cmd == "1":
            add_expense(expenses)
            save_expenses(expenses)
        elif cmd == "2":
            list_expenses(expenses)
        elif cmd == "5":
            save_expenses(expenses)
            print("掰掰")
            break

if __name__ == "__main__":
    main()
```


## 🚀 挑戰版

1. 月份篩選
2. 圖表統計（用 matplotlib）
3. 從 CSV 匯入
4. 加上預算上限提醒


