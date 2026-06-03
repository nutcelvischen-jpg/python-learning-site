---
title: "7.3 抽樣與信賴區間"
---

<div class="lesson-header">
  <span class="chapter-tag">第 7 章 · 統計基礎</span>
  <h1>7.3 抽樣與信賴區間</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 統計</span>
  </div>
</div>

## 🎯 學習目標

- 抽樣誤差
- 信賴區間算法


## 🎯 抽樣分佈

```python
import numpy as np
from scipy import stats

# 母體 N(100, 15)
np.random.seed(42)
pop = np.random.normal(100, 15, 100000)

# 抽 n=30 樣本 1000 次
means = [np.mean(np.random.choice(pop, 30)) for _ in range(1000)]
print(f"樣本平均的 SD: {np.std(means):.3f}")
print(f"理論 SE: {15 / np.sqrt(30):.3f}")
```


## 📏 信賴區間

```python
data = np.random.normal(100, 15, 30)
mean = np.mean(data)
se = stats.sem(data)  # 標準誤

# 95% CI
ci = stats.t.interval(0.95, len(data)-1, mean, se)
print(f"95% CI: ({ci[0]:.2f}, {ci[1]:.2f})")
```


## ✏️ 練習題

1. 抽 50 個樣本算 95% CI
2. 驗證 95% CI 真的覆蓋母體平均 95% 次


