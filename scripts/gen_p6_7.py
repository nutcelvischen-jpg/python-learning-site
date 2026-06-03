#!/usr/bin/env python3
"""生成第 6-9 章 + 第 8 章實戰 + 附錄"""
import os
from pathlib import Path

ROOT = Path("/Users/elvis/projects/python-learning-site/docs")

def H(chap, h1, time, level="入門"):
    return f"""---
title: "{h1}"
---

<div class="lesson-header">
  <span class="chapter-tag">{chap}</span>
  <h1>{h1}</h1>
  <div class="meta">
    <span>⏱️ {time}</span>
    <span>📖 互動式</span>
    <span>🎯 {level}</span>
  </div>
</div>

"""

DATA = [
    # ========== 第 6 章 視覺化 ==========
    ("chapter06_viz/01-principles.md", "第 6 章 · 視覺化", "6.1 設計原則", "20 分鐘", "資料分析", [
        ("🎯 學習目標", """- 知道好的圖表原則
- 避開常見誤導
- 設計資料故事
"""),
        ("📊 設計原則", """1. **清楚勝於花俏**：先求正確再求美
2. **資料墨水比**（Tufte）：刪掉不必要的元素
3. **一張圖一個訊息**：不要塞太多 series
4. **配色有意義**：分類用不同色，連續用漸層
5. **標籤清楚**：軸標、單位、資料來源
"""),
        ("❌ 常見錯誤", """- Y 軸從 0 開始（除非你刻意）
- 3D 效果（會扭曲比例）
- 雙 Y 軸（容易被誤導）
- 太多顏色（彩虹圖）
- 缺單位（NT$ vs NT$ 萬）
"""),
        ("✏️ 練習題", """1. 找 3 個你覺得好的圖表 + 3 個不好的
2. 解釋為什麼好/不好
"""),
    ]),

    ("chapter06_viz/02-matplotlib-basics.md", "第 6 章 · 視覺化", "6.2 matplotlib 基礎", "30 分鐘", "資料分析", [
        ("🎯 學習目標", """- Figure / Axes 架構
- 基本 plot
- 存檔
"""),
        ("🖼️ Figure / Axes", """```python
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
ax.set_title(\"三角函數\")
ax.set_xlabel(\"x\")
ax.set_ylabel(\"y\")
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(\"trig.png\", dpi=120, bbox_inches=\"tight\")
plt.show()
```
"""),
        ("🎨 樣式", """```python
# 內建樣式
plt.style.use(\"seaborn-v0_8-whitegrid\")
# 或 \"ggplot\" / \"fivethirtyeight\" / \"bmh\"

# 中文字型
plt.rcParams['font.sans-serif'] = ['Noto Sans TC', 'Microsoft JhengHei']
plt.rcParams['axes.unicode_minus'] = False
```
"""),
        ("✏️ 練習題", """1. 畫 sin/cos 圖，加圖例跟標題
2. 存成 png 檔
"""),
    ]),

    ("chapter06_viz/03-chart-types.md", "第 6 章 · 視覺化", "6.3 圖表類型", "35 分鐘", "資料分析", [
        ("🎯 學習目標", """- 8 種基本圖表
- 怎麼選
"""),
        ("📊 圖表速查", """```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
vals = [3, 7, 2, 5, 8]

fig, axes = plt.subplots(2, 4, figsize=(16, 8))

# 1. Line
axes[0, 0].plot(x, vals)
axes[0, 0].set_title(\"Line\")

# 2. Bar
axes[0, 1].bar(x, vals)
axes[0, 1].set_title(\"Bar\")

# 3. Scatter
axes[0, 2].scatter(np.random.rand(20), np.random.rand(20))
axes[0, 2].set_title(\"Scatter\")

# 4. Hist
axes[0, 3].hist(np.random.randn(1000), bins=30)
axes[0, 3].set_title(\"Histogram\")

# 5. Box
axes[1, 0].boxplot([np.random.randn(100) for _ in range(5)])
axes[1, 0].set_title(\"Box\")

# 6. Pie
axes[1, 1].pie(vals, labels=list(\"ABCDE\"), autopct='%1.1f%%')
axes[1, 1].set_title(\"Pie\")

# 7. Area
axes[1, 2].fill_between(x, vals, alpha=0.5)
axes[1, 2].set_title(\"Area\")

# 8. Step
axes[1, 3].step(x, vals)
axes[1, 3].set_title(\"Step\")

plt.tight_layout()
plt.show()
```
"""),
        ("🤔 怎麼選圖表", """| 想看什麼 | 用什麼圖 |
|---|---|
| 趨勢（隨時間） | Line |
| 比較類別 | Bar |
| 兩變數關係 | Scatter |
| 分布 | Histogram / Box |
| 占比 | Pie（謹慎） |
| 部分佔整體 | Stacked Bar |
| 地理 | Map / Choropleth |
"""),
        ("✏️ 練習題", """1. 用 AQI 資料畫 5 個縣市 AQI 比較 bar
2. 畫 AQI 分布 histogram
3. 試試 pie 圖的限制
"""),
    ]),

    ("chapter06_viz/04-subplots.md", "第 6 章 · 視覺化", "6.4 子圖佈局", "25 分鐘", "資料分析", [
        ("🎯 學習目標", """- subplots
- GridSpec
- 雙軸
"""),
        ("🔢 subplots", """```python
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

axes[0, 0].plot([1, 2, 3])
axes[0, 1].bar([1, 2, 3], [3, 2, 1])
axes[1, 0].scatter([1, 2, 3], [1, 4, 9])
axes[1, 1].hist(np.random.randn(100))

for ax in axes.flat:
    ax.grid(True, alpha=0.3)

fig.suptitle(\"4 種基本圖\", fontsize=14, fontweight=\"bold\")
plt.tight_layout()
```
"""),
        ("🔀 GridSpec", """```python
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(10, 6))
gs = GridSpec(2, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, :])     # 上面整排
ax2 = fig.add_subplot(gs[1, 0])     # 左下
ax3 = fig.add_subplot(gs[1, 1])     # 右下
```
"""),
        ("⚖️ twinx 雙軸", """```python
fig, ax1 = plt.subplots()
ax1.bar(x, vals, color=\"blue\")
ax1.set_ylabel(\"金額\", color=\"blue\")

ax2 = ax1.twinx()
ax2.plot(x, rates, color=\"red\", marker=\"o\")
ax2.set_ylabel(\"比率\", color=\"red\")
```
"""),
        ("✏️ 練習題", """1. 畫 2x2 子圖
2. 雙軸圖：房價 + AQI
"""),
    ]),

    ("chapter06_viz/05-style.md", "第 6 章 · 視覺化", "6.5 樣式客製", "25 分鐘", "資料分析", [
        ("🎯 學習目標", """- 顏色 / 字型 / 標註
- 客製化樣式
"""),
        ("🎨 顏色", """```python
# 命名色
plt.plot(x, y, color=\"steelblue\")

# HEX
plt.plot(x, y, color=\"#3776AB\")

# RGB tuple
plt.plot(x, y, color=(0.2, 0.4, 0.7))

# colormap
cmap = plt.cm.viridis
colors = [cmap(i/10) for i in range(10)]
```
"""),
        ("🏷️ 標註", """```python
fig, ax = plt.subplots()
ax.plot(x, y)
ax.annotate(\"重要點\", xy=(5, 5), xytext=(6, 6),
            arrowprops=dict(arrowstyle=\"->\", color=\"red\"))
ax.text(2, 8, \"文字說明\", fontsize=12, color=\"blue\")
```
"""),
        ("✏️ 練習題", """1. 客製化一個圖的顏色 / 字型 / 標註
2. 加上資料點標籤
"""),
    ]),

    ("chapter06_viz/06-seaborn.md", "第 6 章 · 視覺化", "6.6 seaborn 進階", "30 分鐘", "資料分析", [
        ("🎯 學習目標", """- seaborn 美化
- heatmap / pairplot / violinplot
"""),
        ("🌊 seaborn 是什麼", """```python
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 內建資料集練習
df = sns.load_dataset(\"tips\")
print(df.head())
```
"""),
        ("🔥 heatmap", """```python
import numpy as np

data = np.random.rand(8, 6)
sns.heatmap(data, annot=True, cmap=\"YlOrRd\")
plt.title(\"熱力圖\")
```
"""),
        ("📊 常見圖", """```python
# 類別 vs 數值
sns.boxplot(data=df, x=\"day\", y=\"total_bill\")

# 散佈 + 分類
sns.scatterplot(data=df, x=\"total_bill\", y=\"tip\", hue=\"sex\")

# 配對圖
sns.pairplot(df, hue=\"sex\")

# 分布
sns.violinplot(data=df, x=\"day\", y=\"total_bill\")
```
"""),
        ("✏️ 練習題", """1. 用 AQI 資料畫 seaborn boxplot（按縣市）
2. 畫 heatmap 看縣市 × 污染物
"""),
    ]),

    ("chapter06_viz/07-plotly.md", "第 6 章 · 視覺化", "6.7 plotly 互動", "20 分鐘", "資料分析", [
        ("🎯 學習目標", """- 互動式圖表
- plotly express
- 存成 HTML
"""),
        ("🎮 為什麼用 plotly", """matplotlib 是**靜態**圖表（PNG），plotly 是**互動**（hover / zoom / pan）。 網頁上必備。
"""),
        ("💫 快速上手", """```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    \"x\": [1, 2, 3, 4, 5],
    \"y\": [1, 4, 9, 16, 25]
})

fig = px.line(df, x=\"x\", y=\"y\", title=\"平方數\")
fig.show()
fig.write_html(\"plot.html\")
```
"""),
        ("📊 真實範例", """```python
# 用 AQI 資料
fig = px.scatter(
    air, x=\"longitude\", y=\"latitude\",
    color=\"aqi\", size=\"pm2_5\",
    hover_name=\"sitename\",
    color_continuous_scale=\"RdYlGn_r\",
    title=\"全台 AQI 分佈\"
)
fig.show()
```
"""),
        ("✏️ 練習題", """1. 用 plotly 畫 AQI 散佈圖
2. 存成 HTML
"""),
    ]),

    ("chapter06_viz/08-publication.md", "第 6 章 · 視覺化", "6.8 發表品質", "15 分鐘", "資料分析", [
        ("🎯 學習目標", """- 解析度
- 格式選擇
- 期刊投稿要求
"""),
        ("🖼️ 解析度", """```python
# 螢幕 72-100 dpi
# 海報 300 dpi
# 期刊通常要求 300 dpi

fig.savefig(\"output.png\", dpi=300, bbox_inches=\"tight\")
```
"""),
        ("📁 格式選擇", """| 格式 | 用途 | 優點 |
|---|---|---|
| PNG | 網頁 / 簡報 | 無損、透明背景 |
| JPG | 照片 | 檔案小 |
| SVG | 期刊 / 海報 | 矢量、無限放大 |
| PDF | 論文 | 矢量、LaTeX 友好 |
"""),
        ("✏️ 練習題", """1. 把一張圖存成 PNG 跟 SVG
2. 比較檔案大小
"""),
    ]),

    # ========== 第 7 章 統計基礎 ==========
    ("chapter07_stats/01-descriptive.md", "第 7 章 · 統計基礎", "7.1 描述統計", "20 分鐘", "統計", [
        ("🎯 學習目標", """- 集中趨勢 / 離散度
- 偏態 / 峰態
"""),
        ("📊 集中趨勢", """```python
import numpy as np
import pandas as pd

data = [10, 20, 30, 40, 50, 100]   # 注意 100 是 outlier

print(f\"平均: {np.mean(data)}\")       # 41.67
print(f\"中位數: {np.median(data)}\")   # 35
print(f\"眾數: {pd.Series(data).mode()[0]}\")  # 沒有重複
```

!!! tip \"中位數 vs 平均\"

    有 outlier 時中位數較穩健。 例如「某城市平均薪資」容易被 CEO 拉高。
"""),
        ("📏 離散度", """```python
data = [1, 2, 3, 4, 5]
print(f\"範圍: {max(data) - min(data)}\")   # 4
print(f\"IQR: Q3 - Q1 = {np.percentile(data, 75) - np.percentile(data, 25)}\")
print(f\"標準差: {np.std(data):.2f}\")        # 1.41
print(f\"變異數: {np.var(data):.2f}\")        # 2.0
```
"""),
        ("✏️ 練習題", """1. 算一組資料的 mean / median / std
2. 比較有 vs 沒有 outlier 的差異
"""),
    ]),

    ("chapter07_stats/02-distributions.md", "第 7 章 · 統計基礎", "7.2 機率分佈", "25 分鐘", "統計", [
        ("🎯 學習目標", """- 常態 / t / 卡方 / F 分佈
- 知道何時用哪個
"""),
        ("📊 常態分佈", """```python
from scipy import stats
import numpy as np

# 標準常態 N(0, 1)
x = np.linspace(-4, 4, 100)
y = stats.norm.pdf(x, 0, 1)

# 算 z-score
z = stats.norm.ppf(0.975)   # 1.96（95% CI 邊界）
print(f\"95% CI z = {z:.2f}\")
```
"""),
        ("📐 t 分佈（小樣本）", """```python
# 樣本數 < 30 用 t 分佈
df = 10  # 自由度
t = stats.t.ppf(0.975, df)
print(f\"t(10) at 0.975 = {t:.3f}\")   # 2.228
```
"""),
        ("📊 卡方分佈（類別資料）", """```python
# 用於適合度檢定
chi = stats.chi2.ppf(0.95, df=4)
print(f\"χ²(4) at 0.95 = {chi:.3f}\")   # 9.488
```
"""),
        ("✏️ 練習題", """1. 模擬 10000 個 N(100, 15) 樣本
2. 算 P(X > 120)
3. 視覺化 t 分佈
"""),
    ]),

    ("chapter07_stats/03-sampling.md", "第 7 章 · 統計基礎", "7.3 抽樣與信賴區間", "20 分鐘", "統計", [
        ("🎯 學習目標", """- 抽樣誤差
- 信賴區間算法
"""),
        ("🎯 抽樣分佈", """```python
import numpy as np
from scipy import stats

# 母體 N(100, 15)
np.random.seed(42)
pop = np.random.normal(100, 15, 100000)

# 抽 n=30 樣本 1000 次
means = [np.mean(np.random.choice(pop, 30)) for _ in range(1000)]
print(f\"樣本平均的 SD: {np.std(means):.3f}\")
print(f\"理論 SE: {15 / np.sqrt(30):.3f}\")
```
"""),
        ("📏 信賴區間", """```python
data = np.random.normal(100, 15, 30)
mean = np.mean(data)
se = stats.sem(data)  # 標準誤

# 95% CI
ci = stats.t.interval(0.95, len(data)-1, mean, se)
print(f\"95% CI: ({ci[0]:.2f}, {ci[1]:.2f})\")
```
"""),
        ("✏️ 練習題", """1. 抽 50 個樣本算 95% CI
2. 驗證 95% CI 真的覆蓋母體平均 95% 次
"""),
    ]),

    ("chapter07_stats/04-testing.md", "第 7 章 · 統計基礎", "7.4 假設檢定", "30 分鐘", "統計", [
        ("🎯 學習目標", """- t-test / chi-square / ANOVA
- p-value 解讀
"""),
        ("🧪 t-test", """```python
from scipy import stats
import numpy as np

# 兩組比較
group_a = np.random.normal(100, 10, 30)
group_b = np.random.normal(105, 10, 30)

t, p = stats.ttest_ind(group_a, group_b)
print(f\"t = {t:.3f}, p = {p:.4f}\")
if p < 0.05:
    print(\"✅ 顯著差異\")
else:
    print(\"❌ 無顯著差異\")
```
"""),
        ("📊 卡方檢定（類別）", """```python
# 列聯表
observed = [[10, 20], [30, 40]]
chi2, p, dof, expected = stats.chi2_contingency(observed)
print(f\"χ² = {chi2:.2f}, p = {p:.4f}\")
```
"""),
        ("📈 ANOVA（多組）", """```python
group1 = np.random.normal(100, 10, 30)
group2 = np.random.normal(105, 10, 30)
group3 = np.random.normal(110, 10, 30)

f, p = stats.f_oneway(group1, group2, group3)
print(f\"F = {f:.2f}, p = {p:.4f}\")
```
"""),
        ("⚠️ p-value 注意事項", """- p < 0.05 不代表「重要」
- p > 0.05 不代表「無效」
- 樣本大才有統計意義
- 多重檢定要修正（Bonferroni）
"""),
        ("✏️ 練習題", """1. 兩組模擬資料做 t-test
2. 3 組做 ANOVA
3. 試試看 p-hacking 的危險
"""),
    ]),

    ("chapter07_stats/05-correlation-regression.md", "第 7 章 · 統計基礎", "7.5 相關與迴歸", "30 分鐘", "統計", [
        ("🎯 學習目標", """- Pearson / Spearman 相關
- 簡單線性迴歸
"""),
        ("🔗 相關分析", """```python
from scipy import stats
import numpy as np

x = np.random.randn(100)
y = 0.5 * x + np.random.randn(100) * 0.5

# Pearson
r, p = stats.pearsonr(x, y)
print(f\"Pearson r = {r:.3f}, p = {p:.4f}\")

# Spearman（單調關係）
rho, p = stats.spearmanr(x, y)
print(f\"Spearman ρ = {rho:.3f}, p = {p:.4f}\")
```
"""),
        ("📈 簡單線性迴歸", """```python
slope, intercept, r, p, se = stats.linregress(x, y)
print(f\"y = {slope:.3f} x + {intercept:.3f}\")
print(f\"R² = {r**2:.3f}\")
```
"""),
        ("💡 用 statsmodels", """```python
import statsmodels.api as sm

X = sm.add_constant(x)
model = sm.OLS(y, X).fit()
print(model.summary())
```
"""),
        ("✏️ 練習題", """1. 算兩變數的 Pearson + Spearman
2. 畫散佈圖 + 迴歸線
3. 用 8.5 章的房價 vs AQI 算相關
"""),
    ]),

    ("chapter07_stats/06-misuse.md", "第 7 章 · 統計基礎", "7.6 統計誤用警示", "20 分鐘", "統計", [
        ("🎯 學習目標", """- p-hacking
- 辛普森悖論
- 相關 vs 因果
"""),
        ("⚠️ p-hacking", """一直做統計檢定直到 p < 0.05，**一定會找到顯著結果**。 這就是 p-hacking。

!!! warning \"修正\"

    1. 先註冊研究設計
    2. 多重比較用 Bonferroni 修正
    3. 報告效應量不只是 p-value
"""),
        ("🌀 辛普森悖論", """分組看 vs 整體看會得到**相反**的結論。

!!! example \"範例\"

    治療 A 對男性有效、對女性也有效。 但把男女加總後，「A 反而比 B 差」！

    原因：**分組比例不同**。
"""),
        ("🔗 相關 ≠ 因果", """X 跟 Y 相關不代表 X 引起 Y。

- 可能是巧合
- 可能 Z 引起 X 跟 Y
- 可能反向因果
"""),
        ("✏️ 練習題", """1. 找一個 p-hacking 的真實案例
2. 解釋一個辛普森悖論例子
"""),
    ]),
]

# 寫入
total = 0
for relpath, chap, h1, time, level, blocks in DATA:
    out = H(chap, h1, time, level)
    for sec_title, sec_content in blocks:
        out += f"## {sec_title}\n\n{sec_content}\n\n"
    full = ROOT / relpath
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(out, encoding="utf-8")
    total += 1
    print(f"✅ {relpath} ({len(out)} chars)")

print(f"\n生成 {total} 個檔案")
