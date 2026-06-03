---
title: "6.4 子圖佈局"
---

<div class="lesson-header">
  <span class="chapter-tag">第 6 章 · 視覺化</span>
  <h1>6.4 子圖佈局</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- subplots
- GridSpec
- 雙軸


## 🔢 subplots

```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot([1, 2, 3])
axes[0, 1].bar([1, 2, 3], [3, 2, 1])
axes[1, 0].scatter([1, 2, 3], [1, 4, 9])
axes[1, 1].hist(np.random.randn(100))

for ax in axes.flat:
    ax.grid(True, alpha=0.3)

fig.suptitle("4 種基本圖", fontsize=14, fontweight="bold")
plt.tight_layout()
```


## 🔀 GridSpec

```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 6))
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, :])     # 上面整排
ax2 = fig.add_subplot(gs[1, 0])     # 左下
ax3 = fig.add_subplot(gs[1, 1])     # 右下
```


## ⚖️ twinx 雙軸

```python
fig, ax1 = plt.subplots()
ax1.bar(x, vals, color="blue")
ax1.set_ylabel("金額", color="blue")

ax2 = ax1.twinx()
ax2.plot(x, rates, color="red", marker="o")
ax2.set_ylabel("比率", color="red")
```


## ✏️ 練習題

1. 畫 2x2 子圖
2. 雙軸圖：房價 + AQI


