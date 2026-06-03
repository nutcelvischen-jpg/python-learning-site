---
title: "5.1 Series 與 DataFrame"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.1 Series 與 DataFrame</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 認識 Series 與 DataFrame
- 從 list / dict 建立
- 基本屬性與方法


## 🐼 pandas 是什麼

```python
import pandas as pd

# Series: 一維（像有 index 的 list）
s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)
# a    10
# b    20
# c    30
# d    40

# DataFrame: 二維（像 Excel 表）
df = pd.DataFrame({
    "name": ["Elvis", "Bob", "Carol"],
    "age": [35, 28, 42],
    "city": ["台中", "台北", "高雄"]
})
print(df)
```


## 🔍 探索 DataFrame

```python
print(df.head())       # 前 5 筆
print(df.tail(3))      # 末 3 筆
print(df.shape)        # (3, 3) — 3 筆 3 欄
print(df.dtypes)       # 各欄型別
print(df.columns)      # 欄位名
print(df.index)        # index
print(df.describe())   # 數值統計摘要
print(df.info())       # 結構 + 型別 + 非空數
```


## ✏️ 練習題

1. 從 dict 建立一個 DataFrame
2. 印出 head / tail / describe


