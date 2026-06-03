---
title: "5.5 轉換"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.5 轉換</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- apply / map / replace
- 新增衍生欄位


## 🔧 apply

```python
# 對 Series
df["age"].apply(lambda x: x * 2)

# 對 DataFrame
df.apply(lambda row: row["a"] + row["b"], axis=1)
```


## 🗺️ map / replace

```python
df["city"].map({"台北": "北", "台中": "中", "高雄": "南"})
df["status"].replace({"good": "好", "bad": "差"})
```


## ✏️ 練習題

1. 算每個測站 PM2.5 的四分位距
2. 新增「嚴重程度」欄：>100 嚴重, 50-100 中等, <50 良好


