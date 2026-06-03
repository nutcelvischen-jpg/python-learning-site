---
title: "5.8 樞紐分析表"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.8 樞紐分析表</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- pivot / pivot_table
- melt（寬轉長）


## 🔄 pivot_table

```python
# 縣市 × 狀態 的平均 AQI
pivot = df.pivot_table(
    values="aqi",
    index="county",
    columns="status",
    aggfunc="mean"
)
```


## ↔️ melt

```python
# 寬轉長（適合 ggplot / seaborn）
long = wide.melt(
    id_vars="date",
    value_vars=["A", "B", "C"],
    var_name="category",
    value_name="value"
)
```


## ✏️ 練習題

1. 做縣市 × 月份的 AQI pivot
2. melt 回長格式


