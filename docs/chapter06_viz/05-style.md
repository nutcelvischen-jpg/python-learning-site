---
title: "6.5 樣式客製"
---

<div class="lesson-header">
  <span class="chapter-tag">第 6 章 · 視覺化</span>
  <h1>6.5 樣式客製</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- 顏色 / 字型 / 標註
- 客製化樣式


## 🎨 顏色

```python
# 命名色
plt.plot(x, y, color="steelblue")

# HEX
plt.plot(x, y, color="#3776AB")

# RGB tuple
plt.plot(x, y, color=(0.2, 0.4, 0.7))

# colormap
cmap = plt.cm.viridis
colors = [cmap(i/10) for i in range(10)]
```


## 🏷️ 標註

```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.annotate("重要點", xy=(5, 5), xytext=(6, 6),
            arrowprops=dict(arrowstyle="->", color="red"))
ax.text(2, 8, "文字說明", fontsize=12, color="blue")
```


## ✏️ 練習題

1. 客製化一個圖的顏色 / 字型 / 標註
2. 加上資料點標籤


