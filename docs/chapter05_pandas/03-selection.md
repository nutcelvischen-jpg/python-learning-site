---
title: "5.3 選取資料"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.3 選取資料</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 熟練 loc / iloc
- 條件過濾
- 多條件


## 🔪 選取欄

```python
df["name"]              # 一欄（Series）
df[["name", "age"]]     # 多欄（DataFrame）
```


## 📍 loc vs iloc

```python
# loc: 用 label
df.loc[0]                 # 第一列
df.loc[0:3]               # 0 到 3
df.loc[0, "name"]       # 0 列的 name
df.loc[df["age"] > 30]  # 條件

# iloc: 用位置
df.iloc[0]                # 第一列
df.iloc[0:3]              # 0, 1, 2
df.iloc[0, 1]             # 0 列 1 欄
```


## 🔍 條件過濾

```python
# 單條件
adult = df[df["age"] >= 18]

# 多條件（注意括號）
tcc = df[(df["city"] == "台中") & (df["age"] > 30)]

# isin
big_city = df[df["city"].isin(["台北", "台中", "高雄"])]

# str.contains
df[df["name"].str.contains("明")]
```


## ✏️ 練習題

1. 過濾出 AQI > 70 的測站
2. 找出特定縣市的所有測站
3. 用 iloc 取前 5 列


