---
title: "5.4 資料清理"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.4 資料清理</h1>
  <div class="meta">
    <span>⏱️ 35 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 處理缺失值
- 處理重複
- 型別轉換


## 🕳️ 缺失值

```python
df.isna()           # True/False 矩陣
df.isna().sum()     # 各欄缺失值數量

df.dropna()         # 丟掉有缺失的列
df.dropna(subset=["age"])  # 只看 age

df.fillna(0)        # 填 0
df["age"].fillna(df["age"].mean())  # 填平均
```


## 🔁 重複值

```python
df.duplicated()            # 布林 mask
df.drop_duplicates()       # 丟重複
df.drop_duplicates(subset=["name"])  # 只看 name
```


## 🔄 型別轉換

```python
df["age"].astype(int)
df["date"].astype("datetime64[ns]")
df["price"].astype(float)
pd.to_numeric(df["x"], errors="coerce")  # 轉不了變 NaN
```


## ✏️ 練習題

1. 找 AQI 資料的缺失值
2. 用平均值填 PM2.5 缺失
3. 移除重複測站


