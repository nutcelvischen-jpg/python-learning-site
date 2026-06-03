---
title: "5.9 時間序列"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.9 時間序列</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- to_datetime
- resample / rolling
- 時區處理


## 📅 時間處理

```python
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["weekday"] = df["date"].dt.day_name()
```


## 📊 resample

```python
df.set_index("date", inplace=True)

# 每日 → 每月
monthly = df.resample("M").mean()

# 每日 → 每季
quarterly = df.resample("Q").sum()
```


## 📈 rolling

```python
df["rolling_7"] = df["aqi"].rolling(7).mean()
df["rolling_30"] = df["aqi"].rolling(30).mean()
```


## ✏️ 練習題

1. 把 AQI 資料轉成時間序列
2. 算 7 日 / 30 日移動平均
3. 按月 groupby 看趨勢


