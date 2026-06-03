---
title: "6.2 matplotlib 基礎"
---

<div class="lesson-header">
  <span class="chapter-tag">第 6 章 · 視覺化</span>
  <h1>6.2 matplotlib 基礎</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 資料分析</span>
  </div>
</div>

## 🎯 學習目標

- Figure / Axes 架構
- 基本 plot
- 存檔


## 🖼️ Figure / Axes

```python
import matplotlib.pyplot as plt
import numpy as np

# 兩種寫法
# 1. 簡單
plt.plot([1, 2, 3], [1, 4, 9])
plt.show()

# 2. 推薦（OO 風格）
fig, ax = plt.subplots(figsize=(8, 5))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)')
ax.plot(x, np.cos(x), label='cos(x)')
ax.set_title("三角函數")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("trig.png", dpi=120, bbox_inches="tight")
plt.show()
```


## 🎨 樣式

```python
# 內建樣式
plt.style.use("seaborn-v0_8-whitegrid")
# 或 "ggplot" / "fivethirtyeight" / "bmh"

# 中文字型
plt.rcParams['font.sans-serif'] = ['Noto Sans TC', 'Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
```


## ✏️ 練習題

1. 畫 sin/cos 圖，加圖例跟標題
2. 存成 png 檔


