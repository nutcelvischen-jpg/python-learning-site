---
title: "5.7 合併"
---

<div class="lesson-header">
  <span class="chapter-tag">第 5 章 · pandas</span>
  <h1>5.7 合併</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- merge / join / concat
- 各種 join 方式


## 🔗 merge

```python
# inner join（預設）
result = df1.merge(df2, on="id")

# left join
result = df1.merge(df2, on="id", how="left")

# 不同 key 名
result = df1.merge(df2, left_on="user_id", right_on="id")
```


## 📚 concat

```python
# 垂直合併（疊行）
all_df = pd.concat([df1, df2, df3], ignore_index=True)

# 水平合併（加欄）
wide = pd.concat([df1, df2], axis=1)
```


## ✏️ 練習題

1. 把空汙跟實價登錄 merge（用縣市）
2. concat 三個季度的資料


