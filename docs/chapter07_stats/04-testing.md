---
title: "7.4 假設檢定"
---

<div class="lesson-header">
  <span class="chapter-tag">第 7 章 · 統計基礎</span>
  <h1>7.4 假設檢定</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 統計</span>
  </div>
</div>

## 🎯 學習目標

- t-test / chi-square / ANOVA
- p-value 解讀


## 🧪 t-test

```python
from scipy import stats
import numpy as np

# 兩組比較
group_a = np.random.normal(100, 10, 30)
group_b = np.random.normal(105, 10, 30)

t, p = stats.ttest_ind(group_a, group_b)
print(f"t = {t:.3f}, p = {p:.4f}")
if p < 0.05:
    print("✅ 顯著差異")
else:
    print("❌ 無顯著差異")
```


## 📊 卡方檢定（類別）

```python
# 列聯表
observed = [[10, 20], [30, 40]]
chi2, p, dof, expected = stats.chi2_contingency(observed)
print(f"χ² = {chi2:.2f}, p = {p:.4f}")
```


## 📈 ANOVA（多組）

```python
group1 = np.random.normal(100, 10, 30)
group2 = np.random.normal(105, 10, 30)
group3 = np.random.normal(110, 10, 30)

f, p = stats.f_oneway(group1, group2, group3)
print(f"F = {f:.2f}, p = {p:.4f}")
```


## ⚠️ p-value 注意事項

- p < 0.05 不代表「重要」
- p > 0.05 不代表「無效」
- 樣本大才有統計意義
- 多重檢定要修正（Bonferroni）


## ✏️ 練習題

1. 兩組模擬資料做 t-test
2. 3 組做 ANOVA
3. 試試看 p-hacking 的危險


