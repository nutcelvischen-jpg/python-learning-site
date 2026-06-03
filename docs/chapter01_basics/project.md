---
title: "小專案: 通訊錄管理"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>小專案: 通訊錄管理</h1>
  <div class="meta">
    <span>⏱️ 60 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 專案目標

做一個命令列的**通訊錄管理程式**，整合本章所有概念：

- ✅ 變數、list、dict
- ✅ 函式
- ✅ 迴圈 + 條件
- ✅ f-string
- ✅ 串列推導式（加分）


## 📋 需求

| 功能 | 指令 | 說明 |
|---|---|---|
| 新增聯絡人 | `add` | 輸入名字、電話 |
| 查詢聯絡人 | `find` | 用名字查電話 |
| 列出全部 | `list` | 印出所有聯絡人 |
| 刪除聯絡人 | `delete` | 用名字刪 |
| 離開 | `quit` | 結束程式 |


## 💻 完整程式碼

```python
"""通訊錄管理 — 第 1 章小專案"""

contacts = {}  # name -> phone

def add_contact():
    name = input("姓名: ").strip()
    phone = input("電話: ").strip()
    contacts[name] = phone
    print(f"✅ 已新增 {name}")

def find_contact():
    name = input("要查詢的姓名: ").strip()
    phone = contacts.get(name)
    if phone:
        print(f"📞 {name}: {phone}")
    else:
        print(f"❌ 找不到 {name}")

def list_contacts():
    if not contacts:
        print("(通訊錄是空的)")
        return
    print("=== 通訊錄 ===")
    for name, phone in contacts.items():
        print(f"  {name}: {phone}")
    print(f"共 {len(contacts)} 個聯絡人")

def delete_contact():
    name = input("要刪除的姓名: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"🗑️ 已刪除 {name}")
    else:
        print(f"❌ 找不到 {name}")

def main():
    actions = {
        "add": add_contact,
        "find": find_contact,
        "list": list_contacts,
        "delete": delete_contact,
    }
    while True:
        cmd = input("\n指令 (add/find/list/delete/quit): ").strip().lower()
        if cmd == "quit":
            print("掰掰！")
            break
        action = actions.get(cmd)
        if action:
            action()
        else:
            print("❓ 未知指令")

if __name__ == "__main__":
    main()
```


## 🚀 挑戰版（給想加碼的人）

加上這些功能：

1. **電話格式驗證**：10 碼數字
2. **匯出 CSV**：把所有聯絡人存成 `.csv`
3. **從 CSV 載入**：開程式時讀取
4. **搜尋關鍵字**：用 `in` 模糊查
5. **分頁**：聯絡人太多時分頁顯示


## ✅ 完成清單

- [x] 我能解釋每行程式在做什麼
- [x] 我能新增、查詢、刪除聯絡人
- [x] 我加了至少 1 個挑戰版功能
- [x] 我把程式 push 到 GitHub


## 📚 延伸閱讀

- [Python 官方教學：資料結構](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python: List Comprehensions](https://realpython.com/list-comprehension-python/)


