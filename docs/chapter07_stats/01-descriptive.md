---
title: "7.1 描述統計"
---

<div class="lesson-header">
  <span class="chapter-tag">第 7 章 · 統計基礎</span>
  <h1>7.1 描述統計</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 統計</span>
  </div>
</div>

## 🎯 學習目標

- 集中趨勢 / 離散度
- 偏態 / 峰態


## 📊 集中趨勢

```python
import numpy as np
import pandas as pd

data = [10, 20, 30, 40, 50, 100]   # 注意 100 是 outlier

print(f"平均: {np.mean(data)}")       # 41.67
print(f"中位數: {np.median(data)}")   # 35
print(f"眾數: {pd.Series(data).mode()[0]}")  # 沒有重複
```

!!! tip "中位數 vs 平均"

    有 outlier 時中位數較穩健。 例如「某城市平均薪資」容易被 CEO 拉高。


## 📏 離散度

```python
data = [1, 2, 3, 4, 5]
print(f"範圍: {max(data) - min(data)}")   # 4
print(f"IQR: Q3 - Q1 = {np.percentile(data, 75) - np.percentile(data, 25)}")
print(f"標準差: {np.std(data):.2f}")        # 1.41
print(f"變異數: {np.var(data):.2f}")        # 2.0
```


## ✏️ 練習題

1. 算一組資料的 mean / median / std
2. 比較有 vs 沒有 outlier 的差異


