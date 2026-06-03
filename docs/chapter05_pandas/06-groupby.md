---
title: "5.6 groupby + agg"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.6 groupby + agg</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- Split-Apply-Combine 觀念
- groupby + agg


## 🔄 groupby 基礎

```python
# 算每縣市平均 AQI
df.groupby("county")["aqi"].mean()

# 多個聚合
df.groupby("county").agg(
    avg_aqi=("aqi", "mean"),
    max_aqi=("aqi", "max"),
    count=("aqi", "count")
)
```


## 📊 多重 groupby

```python
df.groupby(["county", "status"])["aqi"].mean()
```


## 💡 transform

```python
# 把每組的 mean 加到每一列
df["county_avg"] = df.groupby("county")["aqi"].transform("mean")
```


## ✏️ 練習題

1. 算每縣市 AQI 中位數並排序
2. 找 AQI 最高的 3 個測站（每縣市）
3. 用 transform 算每測站的 z-score


