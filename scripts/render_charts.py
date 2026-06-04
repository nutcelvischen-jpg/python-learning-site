#!/usr/bin/env python3
"""
render_charts.py v2.0 — 為 Python 學堂產生所有視覺化圖表
- 自動載入 Noto Sans TC 中文字型
- 為第 6/7/8 章 + 8.5 章補更多視覺化圖
"""
import os
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.lines import Line2D
from scipy import stats
import numpy as np
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud

# 載入中文字型
FONT_PATH = 'docs/assets/fonts/NotoSansTC-Regular.otf'
font_manager.fontManager.addfont(FONT_PATH)
_prop = font_manager.FontProperties(fname=FONT_PATH)
_FONT_NAME = _prop.get_name()

plt.rcParams['font.sans-serif'] = [_FONT_NAME, 'sans-serif']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 110
plt.rcParams['savefig.dpi'] = 110
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor'] = 'white'
plt.rcParams['axes.edgecolor'] = '#E2E8F0'
plt.rcParams['axes.labelcolor'] = '#1E293B'
plt.rcParams['xtick.color'] = '#475569'
plt.rcParams['ytick.color'] = '#475569'
plt.rcParams['axes.spines.top'] = False
plt.rcParams['axes.spines.right'] = False

# 配色（Open Design 啟發）
PRIMARY = '#3776AB'    # Python 藍
ACCENT = '#FF6B35'     # 創意橘
SUCCESS = '#16A34A'    # 綠
WARNING = '#EAB308'    # 黃
DANGER = '#DC2626'     # 紅
DARK = '#0F172A'
GRAY = '#64748B'

PALETTE = [PRIMARY, ACCENT, SUCCESS, WARNING, DANGER, '#8B5CF6', '#EC4899', '#06B6D4']
sns.set_palette(PALETTE)

OUT = 'docs/assets/images'
os.makedirs(OUT, exist_ok=True)

# 載入資料
air = pd.read_csv('docs/assets/data/taiwan_aqi_latest.csv')
house = pd.read_csv('docs/assets/data/taichung_house_price_2024_2025.csv')

# 清洗 O3 欄位（有些是空字串）
air['o3'] = pd.to_numeric(air['o3'], errors='coerce')
air['pm2_5'] = pd.to_numeric(air['pm2_5'], errors='coerce')
air['pm10'] = pd.to_numeric(air['pm10'], errors='coerce')
air['aqi'] = pd.to_numeric(air['aqi'], errors='coerce')
air = air.dropna(subset=['aqi', 'pm2_5', 'pm10', 'o3', 'latitude', 'longitude'])

def save(name, fig, **kwargs):
    fig.tight_layout()
    fig.savefig(f'{OUT}/{name}', bbox_inches='tight', facecolor='white', **kwargs)
    plt.close(fig)
    print(f'  {name}')

print("=" * 60)
print("渲染 Python 學堂 視覺化圖表 v2.0")
print("=" * 60)

# ==================== 既有 13 張（更新 + 修正字型） ====================
print("\n[1/30] 重新生成既有 13 張圖（含 8.5 章）")

# 1. 全台 AQI 地圖
fig, ax = plt.subplots(figsize=(11, 7))
colors = air['aqi'].apply(lambda x:
    SUCCESS if x <= 50 else
    WARNING if x <= 100 else
    ACCENT if x <= 150 else DANGER
)
ax.scatter(air['longitude'], air['latitude'], c=colors, s=100, alpha=0.75, edgecolors='white', linewidth=1.5)
ax.set_title('全台 84 個 AQI 測站分佈圖', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('經度', fontsize=11)
ax.set_ylabel('緯度', fontsize=11)
ax.grid(True, alpha=0.3, linestyle='--')
# 圖例
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='良好 (≤50)', markerfacecolor=SUCCESS, markersize=10),
    Line2D([0], [0], marker='o', color='w', label='普通 (51-100)', markerfacecolor=WARNING, markersize=10),
    Line2D([0], [0], marker='o', color='w', label='不健康 (101-150)', markerfacecolor=ACCENT, markersize=10),
    Line2D([0], [0], marker='o', color='w', label='非常不健康 (>150)', markerfacecolor=DANGER, markersize=10),
]
ax.legend(handles=legend_elements, loc='lower right', frameon=True, framealpha=0.9)
save('chart1_taiwan_aqi_map.png', fig)

# 2. 縣市 AQI 排名
fig, ax = plt.subplots(figsize=(10, 6))
county_aqi = air.groupby('county')['aqi'].median().sort_values()
colors_bar = [SUCCESS if v <= 50 else WARNING if v <= 100 else ACCENT for v in county_aqi.values]
ax.barh(county_aqi.index, county_aqi.values, color=colors_bar, edgecolor='white')
ax.set_title('全台 22 縣市 AQI 中位數排名', fontsize=14, fontweight='bold')
ax.set_xlabel('AQI 中位數', fontsize=11)
ax.grid(True, axis='x', alpha=0.3, linestyle='--')
for i, v in enumerate(county_aqi.values):
    ax.text(v + 1, i, f'{v:.0f}', va='center', fontsize=9)
save('chart2_county_aqi_rank.png', fig)

# 3. PM2.5 vs O3 散佈
fig, ax = plt.subplots(figsize=(10, 6))
scatter = ax.scatter(air['pm2_5'], air['o3'], c=air['aqi'], cmap='RdYlGn_r',
                     s=80, alpha=0.7, edgecolors='white', linewidth=1)
ax.set_title('PM2.5 vs O3 — 兩大污染物關係', fontsize=14, fontweight='bold')
ax.set_xlabel('PM2.5 (μg/m³)', fontsize=11)
ax.set_ylabel('O3 (ppb)', fontsize=11)
ax.grid(True, alpha=0.3)
plt.colorbar(scatter, label='AQI')
save('chart3_pm25_vs_o3.png', fig)

# 4. 臺中市房價 vs AQI 雙軸圖
fig, ax1 = plt.subplots(figsize=(11, 6))
tcc = house.groupby('district').agg(median_price=('median_price_per_sqm', 'median')).reset_index().sort_values('median_price', ascending=False)
ax1.bar(tcc['district'], tcc['median_price'], color=PRIMARY, alpha=0.8, label='中位房價')
ax1.set_xlabel('行政區', fontsize=11)
ax1.set_ylabel('中位房價 (NT$/m²)', color=PRIMARY, fontsize=11)
ax1.tick_params(axis='y', labelcolor=PRIMARY)
plt.xticks(rotation=45, ha='right')
ax1.grid(True, axis='y', alpha=0.3, linestyle='--')

# 假設的 AQI 對比
np.random.seed(42)
taichung_districts_aqi = {
    '西屯區': 68, '北屯區': 62, '南屯區': 65, '中區': 72, '東區': 70,
    '西區': 70, '南區': 60, '北區': 64, '北區': 64
}
ax2 = ax1.twinx()
ax2.plot(tcc['district'], [taichung_districts_aqi.get(d, 60) for d in tcc['district']],
         color=ACCENT, marker='o', linewidth=2, markersize=8, label='平均 AQI')
ax2.set_ylabel('平均 AQI', color=ACCENT, fontsize=11)
ax2.tick_params(axis='y', labelcolor=ACCENT)
ax2.spines['top'].set_visible(False)

plt.title('臺中市 28 行政區：房價 vs 空氣品質 AQI', fontsize=14, fontweight='bold', pad=15)
fig.tight_layout()
save('chart4_taichung_house_air.png', fig)

# 5. 房價 vs AQI 相關性 + 迴歸線
fig, ax = plt.subplots(figsize=(10, 6))
np.random.seed(42)
n = 28
x = np.random.uniform(50, 90, n)
y = 200000 + 1500 * x + np.random.normal(0, 80000, n)
slope, intercept, r, p, se = stats.linregress(x, y)
ax.scatter(x, y, c=ACCENT, s=80, alpha=0.7, edgecolors='white', linewidth=1.5)
ax.plot(x, slope * x + intercept, color=PRIMARY, linewidth=2.5,
        label=f'y = {slope:.0f}x + {intercept:.0f}\nR² = {r**2:.3f}, p = {p:.3f}')
ax.set_title('空汙 vs 房價：線性迴歸分析', fontsize=14, fontweight='bold')
ax.set_xlabel('平均 AQI', fontsize=11)
ax.set_ylabel('中位房價 (NT$)', fontsize=11)
ax.legend(loc='upper left', fontsize=10, frameon=True, framealpha=0.9)
ax.grid(True, alpha=0.3, linestyle='--')
save('chart5_house_aqi_regression.png', fig)

# 6. matplotlib 基礎 — 三角函數
fig, ax = plt.subplots(figsize=(10, 5))
x = np.linspace(0, 10, 100)
ax.plot(x, np.sin(x), label='sin(x)', linewidth=2, color=PRIMARY)
ax.plot(x, np.cos(x), label='cos(x)', linewidth=2, color=ACCENT, linestyle='--')
ax.set_title('matplotlib 基礎範例 — 三角函數', fontsize=14, fontweight='bold')
ax.set_xlabel('x (rad)', fontsize=11)
ax.set_ylabel('y', fontsize=11)
ax.legend(loc='upper right', fontsize=11, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--')
save('chart6_matplotlib_basics.png', fig)

# 7. 銷售熱力圖
fig, ax = plt.subplots(figsize=(8, 6))
np.random.seed(42)
data = np.random.rand(7, 5) * 100
months = ['週一', '週二', '週三', '週四', '週五', '週六', '週日']
hours = ['10時', '12時', '14時', '16時', '18時']
sns.heatmap(data, xticklabels=hours, yticklabels=months, annot=True, fmt='.0f',
            cmap='YlOrRd', cbar_kws={'label': '營業額 (千)'}, ax=ax)
ax.set_title('一週各時段營業額熱力圖', fontsize=14, fontweight='bold')
ax.set_xlabel('時段', fontsize=11)
ax.set_ylabel('星期', fontsize=11)
save('chart7_sales_heatmap.png', fig)

# 8. NumPy broadcasting 視覺化
fig, ax = plt.subplots(figsize=(9, 6))
a = np.array([[1], [2], [3]])
b = np.array([10, 20, 30, 40])
c = a + b
im = ax.imshow(c, cmap='viridis', aspect='auto')
ax.set_title('NumPy Broadcasting 視覺化 (3,1) + (1,4) → (3,4)', fontsize=13, fontweight='bold')
ax.set_xlabel('b 的維度 (0-3)', fontsize=11)
ax.set_ylabel('a 的維度 (0-2)', fontsize=11)
for i in range(3):
    for j in range(4):
        ax.text(j, i, f'{c[i, j]}', ha='center', va='center', color='white', fontsize=12, fontweight='bold')
plt.colorbar(im, ax=ax, label='a + b')
save('chart8_numpy_broadcasting.png', fig)

# 9. pandas 時間序列
fig, ax = plt.subplots(figsize=(11, 5))
np.random.seed(42)
dates = pd.date_range('2025-01-01', periods=180)
ts = 50 + 20 * np.sin(np.arange(180) / 30) + np.random.randn(180) * 8
df_ts = pd.DataFrame({'aqi': ts}, index=dates)
ax.plot(df_ts.index, df_ts['aqi'], alpha=0.4, label='日 AQI', color=PRIMARY, linewidth=1)
ax.plot(df_ts.index, df_ts['aqi'].rolling(7).mean(), label='7 日均線', color=ACCENT, linewidth=2)
ax.plot(df_ts.index, df_ts['aqi'].rolling(30).mean(), label='30 日均線', color=DANGER, linewidth=2.5)
ax.set_title('pandas 時間序列：移動平均線分析', fontsize=14, fontweight='bold')
ax.set_xlabel('日期', fontsize=11)
ax.set_ylabel('AQI', fontsize=11)
ax.legend(loc='upper right', fontsize=10, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--')
save('chart9_pandas_timeseries.png', fig)

# 10. list 概念圖
fig, ax = plt.subplots(figsize=(10, 4))
fruits = ['蘋果', '香蕉', '葡萄', '橘子', '草莓']
y_pos = np.arange(len(fruits))
colors_list = [PRIMARY, ACCENT, SUCCESS, WARNING, DANGER]
ax.barh(y_pos, [1]*5, color=colors_list, edgecolor='white', linewidth=2)
for i, (fruit, color) in enumerate(zip(fruits, colors_list)):
    ax.text(0.5, i, f'{i}: {fruit}', ha='center', va='center', fontsize=14,
            fontweight='bold', color='white')
ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_title('Python list 概念：有序索引的容器', fontsize=14, fontweight='bold', pad=10)
save('chart10_list_concept.png', fig)

# 11. dict 概念圖
fig, ax = plt.subplots(figsize=(10, 4.5))
keys = ['name', 'age', 'city', 'job']
values = ['Elvis', '35', '台中', '教授']
colors_dict = [PRIMARY, ACCENT, SUCCESS, WARNING]
y_pos = np.arange(len(keys))
ax.barh(y_pos, [1]*4, color=colors_dict, edgecolor='white', linewidth=2)
for i, (k, v, c) in enumerate(zip(keys, values, colors_dict)):
    ax.text(0.25, i, k, ha='center', va='center', fontsize=13, fontweight='bold', color='white')
    ax.text(0.75, i, f'→ {v}', ha='center', va='center', fontsize=13, fontweight='bold', color='white')
ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0, 1)
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_title('Python dict 概念：key-value 對映', fontsize=14, fontweight='bold', pad=10)
save('chart11_dict_concept.png', fig)

# 12. 常態分佈
fig, ax = plt.subplots(figsize=(10, 5))
x = np.linspace(-4, 4, 200)
y = (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2)
ax.plot(x, y, color=PRIMARY, linewidth=2.5, label='標準常態 N(0,1)')
ax.fill_between(x, y, where=(x >= -1) & (x <= 1), alpha=0.4, color=SUCCESS, label='68.2% (±1σ)')
ax.fill_between(x, y, where=(x >= -2) & (x <= 2), alpha=0.3, color=WARNING, label='95.4% (±2σ)')
ax.fill_between(x, y, where=(x >= -3) & (x <= 3), alpha=0.2, color=ACCENT, label='99.7% (±3σ)')
ax.set_title('常態分佈：68-95-99.7 法則', fontsize=14, fontweight='bold')
ax.set_xlabel('Z-score', fontsize=11)
ax.set_ylabel('機率密度', fontsize=11)
ax.legend(loc='upper right', fontsize=10, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--')
save('chart12_normal_distribution.png', fig)

# 13. NumPy 統計
fig, ax = plt.subplots(figsize=(10, 5))
np.random.seed(42)
data = np.random.normal(100, 15, 1000)
ax.hist(data, bins=40, color=PRIMARY, edgecolor='white', alpha=0.7)
ax.axvline(np.mean(data), color=DANGER, linestyle='--', linewidth=2, label=f'平均 = {np.mean(data):.1f}')
ax.axvline(np.median(data), color=ACCENT, linestyle='--', linewidth=2, label=f'中位數 = {np.median(data):.1f}')
ax.axvline(np.mean(data) + np.std(data), color=GRAY, linestyle=':', linewidth=1.5, label=f'±1σ = {np.std(data):.1f}')
ax.axvline(np.mean(data) - np.std(data), color=GRAY, linestyle=':', linewidth=1.5)
ax.set_title('NumPy 統計：1000 個 N(100, 15) 樣本', fontsize=14, fontweight='bold')
ax.set_xlabel('數值', fontsize=11)
ax.set_ylabel('頻次', fontsize=11)
ax.legend(loc='upper right', fontsize=10, frameon=True)
ax.grid(True, alpha=0.3)
save('chart13_numpy_stats.png', fig)

# ==================== 新增第 6 章圖表 ====================
print("\n[2/30] 第 6 章 — 視覺化 7 張新圖")

# 14. 6.1 設計原則好壞對比
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# 壞的
x = ['A', 'B', 'C', 'D']
y = [3, 5, 2, 7]
axes[0].bar(x, y, color=['red', 'yellow', 'green', 'purple'])
axes[0].set_title('❌ 差：彩虹配色、無單位、無排序', fontsize=12, color=DANGER, fontweight='bold')
axes[0].set_ylabel('數量 (??)')

# 好的
sorted_idx = np.argsort(y)[::-1]
axes[1].bar([x[i] for i in sorted_idx], [y[i] for i in sorted_idx], color=PRIMARY, edgecolor='white', linewidth=2)
axes[1].set_title('✅ 好：單色 + 排序 + 清楚標籤', fontsize=12, color=SUCCESS, fontweight='bold')
axes[1].set_ylabel('銷售量 (千件)')
axes[1].grid(True, axis='y', alpha=0.3, linestyle='--')
for i, v in enumerate([y[j] for j in sorted_idx]):
    axes[1].text(i, v + 0.2, f'{v}', ha='center', fontsize=10, fontweight='bold')

fig.suptitle('設計原則：好圖 vs 壞圖', fontsize=15, fontweight='bold')
save('chart14_good_vs_bad.png', fig)

# 15. 6.3 圖表類型 8 合 1
fig, axes = plt.subplots(2, 4, figsize=(16, 7))
np.random.seed(42)
x = np.arange(5)
vals = [3, 7, 2, 5, 8]
axes[0, 0].plot(x, vals, marker='o', color=PRIMARY, linewidth=2)
axes[0, 0].set_title('折線圖 (Line)\n看趨勢', fontsize=11, fontweight='bold')

axes[0, 1].bar(x, vals, color=ACCENT, edgecolor='white')
axes[0, 1].set_title('長條圖 (Bar)\n比較類別', fontsize=11, fontweight='bold')

axes[0, 2].scatter(np.random.rand(30), np.random.rand(30), c=np.random.rand(30),
                   cmap='viridis', s=80, alpha=0.7)
axes[0, 2].set_title('散佈圖 (Scatter)\n兩變數關係', fontsize=11, fontweight='bold')

axes[0, 3].hist(np.random.randn(500), bins=30, color=SUCCESS, edgecolor='white')
axes[0, 3].set_title('直方圖 (Histogram)\n看分布', fontsize=11, fontweight='bold')

axes[1, 0].boxplot([np.random.randn(100) + i for i in range(5)], patch_artist=True,
                   boxprops=dict(facecolor=WARNING, alpha=0.7))
axes[1, 0].set_title('箱型圖 (Box)\n分位數 + 離群值', fontsize=11, fontweight='bold')

axes[1, 1].pie(vals, labels=list('ABCDE'), autopct='%1.1f%%',
               colors=PALETTE, startangle=90)
axes[1, 1].set_title('圓餅圖 (Pie)\n占比', fontsize=11, fontweight='bold')

axes[1, 2].fill_between(x, vals, alpha=0.5, color='#8B5CF6')
axes[1, 2].plot(x, vals, color='#8B5CF6', linewidth=2)
axes[1, 2].set_title('面積圖 (Area)\n累積', fontsize=11, fontweight='bold')

axes[1, 3].step(x, vals, where='mid', color=DANGER, linewidth=2)
axes[1, 3].set_title('階梯圖 (Step)\n離散變化', fontsize=11, fontweight='bold')

fig.suptitle('8 種基本圖表類型速覽', fontsize=16, fontweight='bold', y=1.01)
save('chart15_8_chart_types.png', fig)

# 16. 6.4 子圖佈局範例
fig = plt.figure(figsize=(12, 7))
gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.3)
ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

x = np.linspace(0, 10, 100)
ax1.plot(x, np.sin(x), label='sin', color=PRIMARY, linewidth=2)
ax1.plot(x, np.cos(x), label='cos', color=ACCENT, linewidth=2)
ax1.set_title('上方整排：兩條線比較', fontsize=12, fontweight='bold')
ax1.legend()
ax1.grid(True, alpha=0.3)

ax2.bar(['A', 'B', 'C', 'D'], [3, 7, 2, 5], color=SUCCESS)
ax2.set_title('左下：長條圖', fontsize=12, fontweight='bold')

ax3.scatter(np.random.rand(20), np.random.rand(20), s=100, c=range(20), cmap='plasma')
ax3.set_title('右下：散佈圖', fontsize=12, fontweight='bold')

fig.suptitle('GridSpec 子圖佈局範例', fontsize=15, fontweight='bold')
save('chart16_subplots_gridspec.png', fig)

# 17. 6.5 樣式客製 — 顏色 + 標註
fig, ax = plt.subplots(figsize=(11, 6))
np.random.seed(42)
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
revenue = [120, 135, 150, 180, 220, 250, 280, 290, 260, 230, 200, 180]
bars = ax.bar(months, revenue, color=PRIMARY, edgecolor='white', linewidth=1.5)
# 標示最高點
max_idx = revenue.index(max(revenue))
bars[max_idx].set_color(ACCENT)
ax.annotate('年度最高！',
            xy=(max_idx, revenue[max_idx]),
            xytext=(max_idx - 2, revenue[max_idx] + 30),
            fontsize=12, color=DANGER, fontweight='bold',
            arrowprops=dict(arrowstyle='->', color=DANGER, lw=2))
# 平均線
ax.axhline(np.mean(revenue), color=GRAY, linestyle='--', linewidth=1.5,
           label=f'平均 {np.mean(revenue):.0f}')
ax.set_title('2025 每月營收：顏色標註 + 文字標註', fontsize=14, fontweight='bold')
ax.set_xlabel('月份', fontsize=11)
ax.set_ylabel('營收 (萬 NT$)', fontsize=11)
ax.legend()
ax.grid(True, axis='y', alpha=0.3, linestyle='--')
plt.xticks(rotation=30)
save('chart17_styled_chart.png', fig)

# 18. 6.6 seaborn 範例
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
np.random.seed(42)

# 1. boxplot
df_demo = pd.DataFrame({
    '城市': np.repeat(['台北', '台中', '高雄', '花蓮'], 50),
    '房價': np.concatenate([
        np.random.normal(450, 100, 50),
        np.random.normal(280, 70, 50),
        np.random.normal(220, 60, 50),
        np.random.normal(180, 50, 50),
    ])
})
sns.boxplot(data=df_demo, x='城市', y='房價', palette='Set2', ax=axes[0, 0])
axes[0, 0].set_title('seaborn boxplot：四城市房價', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('房價 (萬 NT$)')

# 2. scatter
df_demo['坪數'] = np.random.uniform(20, 60, 200)
df_demo['房價'] = df_demo['房價'] * (df_demo['坪數'] / 40)
sns.scatterplot(data=df_demo, x='坪數', y='房價', hue='城市', palette='Set2', ax=axes[0, 1], s=60, alpha=0.7)
axes[0, 1].set_title('seaborn scatter：坪數 vs 房價', fontsize=12, fontweight='bold')

# 3. violin
sns.violinplot(data=df_demo, x='城市', y='房價', palette='muted', ax=axes[1, 0])
axes[1, 0].set_title('seaborn violin：分布形狀', fontsize=12, fontweight='bold')

# 4. heatmap
corr = df_demo[['房價', '坪數']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0, ax=axes[1, 1],
            cbar_kws={'label': '相關係數'})
axes[1, 1].set_title('seaborn heatmap：相關性', fontsize=12, fontweight='bold')

fig.suptitle('seaborn 4 種經典圖表', fontsize=15, fontweight='bold', y=1.00)
save('chart18_seaborn_examples.png', fig)

# 19. 6.7 plotly 互動範例（用 matplotlib 模擬 plotly 風格）
fig, ax = plt.subplots(figsize=(11, 6))
np.random.seed(42)
n = 200
x = np.random.randn(n)
y = x * 0.7 + np.random.randn(n) * 0.5
sizes = np.random.uniform(30, 300, n)
colors = np.random.uniform(0, 1, n)
scatter = ax.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.6, edgecolors='white', linewidth=0.5)
ax.set_title('plotly 風格：互動式散佈圖 (Hover / Zoom / Pan)', fontsize=14, fontweight='bold')
ax.set_xlabel('變數 X', fontsize=11)
ax.set_ylabel('變數 Y', fontsize=11)
ax.grid(True, alpha=0.3, linestyle='--')
plt.colorbar(scatter, label='第三維度')
save('chart19_plotly_style.png', fig)

# 20. 6.8 發表品質
fig, axes = plt.subplots(1, 2, figsize=(13, 5))
# PNG 風格
ax1 = axes[0]
ax1.bar(['2019', '2020', '2021', '2022'], [10, 15, 20, 25], color=PRIMARY)
ax1.set_title('螢幕用 (72 dpi)', fontsize=12)
# 期刊風格
ax2 = axes[1]
ax2.bar(['2019', '2020', '2021', '2022'], [10, 15, 20, 25], color=PRIMARY, edgecolor='black', linewidth=1.2)
ax2.set_title('期刊用 (300 dpi + 黑框)', fontsize=12, fontname='serif')
ax2.set_xlabel('年份', fontname='serif')
ax2.set_ylabel('指標值', fontname='serif')
fig.suptitle('發表品質：解析度與格式', fontsize=14, fontweight='bold')
save('chart20_publication_quality.png', fig)

# ==================== 新增第 7 章圖表 ====================
print("\n[3/30] 第 7 章 — 統計 5 張新圖")

# 21. 7.1 描述統計
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
np.random.seed(42)
no_outlier = [50, 52, 48, 51, 49, 53, 50, 52, 48, 51, 49, 50, 52, 51, 49]
with_outlier = no_outlier + [200]  # 異常值

axes[0].hist(no_outlier, bins=8, color=PRIMARY, edgecolor='white')
axes[0].axvline(np.mean(no_outlier), color=DANGER, linestyle='--', linewidth=2, label=f'平均 {np.mean(no_outlier):.1f}')
axes[0].axvline(np.median(no_outlier), color=ACCENT, linestyle='--', linewidth=2, label=f'中位數 {np.median(no_outlier):.1f}')
axes[0].set_title('無異常值\n平均 ≈ 中位數', fontsize=11)
axes[0].legend()
axes[0].set_xlabel('數值')

axes[1].hist(with_outlier, bins=8, color=PRIMARY, edgecolor='white')
axes[1].axvline(np.mean(with_outlier), color=DANGER, linestyle='--', linewidth=2, label=f'平均 {np.mean(with_outlier):.1f}')
axes[1].axvline(np.median(with_outlier), color=ACCENT, linestyle='--', linewidth=2, label=f'中位數 {np.median(with_outlier):.1f}')
axes[1].set_title('有異常值 (200)\n平均被拉高，中位數穩健', fontsize=11)
axes[1].legend()
axes[1].set_xlabel('數值')

axes[2].boxplot([no_outlier, with_outlier], labels=['無', '有'], patch_artist=True,
                boxprops=dict(facecolor=PRIMARY, alpha=0.7),
                medianprops=dict(color=DANGER, linewidth=2))
axes[2].set_title('箱型圖：一眼看出離群值', fontsize=11)
axes[2].set_ylabel('數值')

fig.suptitle('描述統計：平均 vs 中位數，離群值的影響', fontsize=14, fontweight='bold')
save('chart21_descriptive_stats.png', fig)

# 22. 7.2 機率分佈比較
fig, ax = plt.subplots(figsize=(11, 6))
x = np.linspace(-4, 4, 200)
ax.plot(x, (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2),
        color=PRIMARY, linewidth=2.5, label='標準常態 N(0,1)')

# already imported via stats
for df in [3, 10, 30]:
    ax.plot(x, stats.t.pdf(x, df), linewidth=1.5,
            label=f't 分佈 (df={df})', linestyle='--', alpha=0.8)

ax.set_title('機率分佈比較：常態 vs t 分佈', fontsize=14, fontweight='bold')
ax.set_xlabel('x', fontsize=11)
ax.set_ylabel('機率密度', fontsize=11)
ax.legend(loc='upper right', fontsize=10, frameon=True)
ax.grid(True, alpha=0.3, linestyle='--')
ax.text(-3, 0.2, '樣本小 (df小)\n→ 尾巴厚', fontsize=10, color=DANGER,
        bbox=dict(boxstyle='round', facecolor='white', edgecolor=DANGER))
ax.text(1, 0.2, 'df 越大\n→ 越接近常態', fontsize=10, color=SUCCESS,
        bbox=dict(boxstyle='round', facecolor='white', edgecolor=SUCCESS))
save('chart22_distribution_comparison.png', fig)

# 23. 7.3 抽樣分佈
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
np.random.seed(42)
pop = np.random.normal(100, 15, 100000)
axes[0].hist(pop, bins=50, color=PRIMARY, edgecolor='white', alpha=0.7)
axes[0].set_title('母體分佈 N(100, 15)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('數值')
axes[0].set_ylabel('頻次')

means = [np.mean(np.random.choice(pop, 30)) for _ in range(2000)]
axes[1].hist(means, bins=40, color=ACCENT, edgecolor='white', alpha=0.7)
axes[1].axvline(np.mean(means), color=DANGER, linestyle='--', linewidth=2,
                label=f'樣本平均的 SD = {np.std(means):.2f}')
axes[1].set_title('抽樣分佈 (n=30, 重抽 2000 次)', fontsize=12, fontweight='bold')
axes[1].set_xlabel('樣本平均')
axes[1].set_ylabel('頻次')
axes[1].legend()
fig.suptitle('中央極限定理：樣本平均的分布', fontsize=14, fontweight='bold')
save('chart23_sampling_distribution.png', fig)

# 24. 7.4 假設檢定
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
x = np.linspace(-4, 4, 200)
y = (1/np.sqrt(2*np.pi)) * np.exp(-x**2/2)
axes[0].plot(x, y, color=PRIMARY, linewidth=2)
x_shaded = x[x >= 1.96]
axes[0].fill_between(x_shaded, (1/np.sqrt(2*np.pi)) * np.exp(-x_shaded**2/2),
                     alpha=0.5, color=DANGER, label='拒絕域 (α=0.05)')
axes[0].fill_between(x[x <= -1.96], (1/np.sqrt(2*np.pi)) * np.exp(-x[x <= -1.96]**2/2),
                     alpha=0.5, color=DANGER)
axes[0].set_title('雙尾檢定 (α = 0.05)', fontsize=12, fontweight='bold')
axes[0].axvline(1.96, color=DARK, linestyle='--', linewidth=1)
axes[0].axvline(-1.96, color=DARK, linestyle='--', linewidth=1)
axes[0].text(2.5, 0.05, '拒絕 H0', fontsize=11, color=DANGER, fontweight='bold')
axes[0].legend()

# p-value 示意
axes[1].plot(x, y, color=PRIMARY, linewidth=2)
x_obs = x[x >= 2.5]
axes[1].fill_between(x_obs, (1/np.sqrt(2*np.pi)) * np.exp(-x_obs**2/2),
                     alpha=0.6, color=ACCENT, label=f'p = 0.0062')
axes[1].axvline(2.5, color=DARK, linestyle='--', linewidth=2, label='觀察值 z=2.5')
axes[1].set_title('p-value：觀察值右側的面積', fontsize=12, fontweight='bold')
axes[1].legend()

fig.suptitle('假設檢定視覺化', fontsize=14, fontweight='bold')
save('chart24_hypothesis_testing.png', fig)

# 25. 7.5 相關性 + 迴歸
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
np.random.seed(42)
x1 = np.random.randn(100)
y1 = 0.8 * x1 + np.random.randn(100) * 0.3
axes[0].scatter(x1, y1, c=PRIMARY, s=60, alpha=0.6, edgecolors='white')
slope, intercept, r, p, se = stats.linregress(x1, y1)
axes[0].plot(x1, slope * x1 + intercept, color=ACCENT, linewidth=2,
             label=f'r = {r:.3f}, R² = {r**2:.3f}')
axes[0].set_title('正向相關 r = 0.8+ (強)', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

x2 = np.random.randn(100)
y2 = -0.6 * x2 + np.random.randn(100) * 0.5
slope2, intercept2, r2, p2, se2 = stats.linregress(x2, y2)
axes[1].scatter(x2, y2, c=DANGER, s=60, alpha=0.6, edgecolors='white')
axes[1].plot(x2, slope2 * x2 + intercept2, color=PRIMARY, linewidth=2,
             label=f'r = {r2:.3f}, R² = {r2**2:.3f}')
axes[1].set_title('負向相關 r = -0.6 (中)', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

fig.suptitle('相關分析：正相關 vs 負相關', fontsize=14, fontweight='bold')
save('chart25_correlation_examples.png', fig)

# ==================== 新增第 8 章實戰圖 ====================
print("\n[4/30] 第 8 章 — 4 個實戰 + 8.5 章 補強圖")

# 26. 8.1 空氣品質 — 污染物雷達 / 綜合
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
# 雷達圖：各測站污染物平均
pollutants = ['PM2.5', 'PM10', 'O3', 'NO2', 'SO2', 'CO']
# 計算全台平均
pollutants_data = {
    'PM2.5': air['pm2_5'].mean(),
    'PM10': air['pm10'].mean(),
    'O3': air['o3'].mean() / 10,  # scale down
    'NO2': air.get('no2', pd.Series([15]*84)).mean() if 'no2' in air.columns else 15,
    'SO2': air.get('so2', pd.Series([5]*84)).mean() if 'so2' in air.columns else 5,
    'CO': air.get('co', pd.Series([0.5]*84)).mean() if 'co' in air.columns else 0.5,
}
# 正常化
values = [pollutants_data[p] for p in pollutants]
max_v = max(values) if max(values) > 0 else 1
values_norm = [v / max_v for v in values]
values_norm += values_norm[:1]  # 閉合
angles = np.linspace(0, 2*np.pi, len(pollutants), endpoint=False).tolist()
angles += angles[:1]

ax1 = axes[0]
ax1 = plt.subplot(121, projection='polar')
ax1.plot(angles, values_norm, color=ACCENT, linewidth=2.5)
ax1.fill(angles, values_norm, color=ACCENT, alpha=0.3)
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(pollutants, fontsize=11)
ax1.set_title('全台 84 測站平均污染物雷達圖', fontsize=12, fontweight='bold', pad=20)

# 長條圖
ax2 = axes[1]
ax2.bar(pollutants, values, color=[SUCCESS if v < 20 else WARNING if v < 50 else ACCENT for v in values], edgecolor='white')
ax2.set_title('各污染物平均值 (原始單位)', fontsize=12, fontweight='bold')
ax2.set_ylabel('濃度')
ax2.grid(True, axis='y', alpha=0.3, linestyle='--')
plt.setp(ax2.xaxis.get_majorticklabels(), rotation=30, ha='right')

fig.suptitle('8.1 空氣品質分析：全台污染物分佈', fontsize=14, fontweight='bold')
save('chart26_air_radar.png', fig)

# 27. 8.2 銷售儀表板 - 月度熱度 + RFM
fig, axes = plt.subplots(2, 2, figsize=(14, 9))
np.random.seed(42)
n = 500
df_sales = pd.DataFrame({
    'product': np.random.choice(['筆電', '手機', '耳機', '平板'], n),
    'region': np.random.choice(['北區', '中區', '南區', '東區'], n),
    'quantity': np.random.randint(1, 10, n),
    'price': np.random.randint(500, 50000, n),
    'month': np.random.choice(range(1, 13), n),
})
df_sales['revenue'] = df_sales['quantity'] * df_sales['price']

# 1. 月營收
monthly = df_sales.groupby('month')['revenue'].sum() / 1e6
axes[0, 0].plot(monthly.index, monthly.values, marker='o', color=PRIMARY, linewidth=2.5, markersize=8)
axes[0, 0].fill_between(monthly.index, monthly.values, alpha=0.3, color=PRIMARY)
axes[0, 0].set_title('月營收趨勢 (百萬 NT$)', fontsize=11, fontweight='bold')
axes[0, 0].set_xlabel('月份')
axes[0, 0].grid(True, alpha=0.3)

# 2. 產品營收
prod = df_sales.groupby('product')['revenue'].sum() / 1e6
axes[0, 1].barh(prod.index, prod.values, color=[PRIMARY, ACCENT, SUCCESS, WARNING], edgecolor='white')
axes[0, 1].set_title('產品營收總計', fontsize=11, fontweight='bold')
axes[0, 1].set_xlabel('營收 (百萬)')

# 3. 地區分布
region = df_sales.groupby('region')['revenue'].sum() / 1e6
axes[1, 0].bar(region.index, region.values, color=PALETTE[:4], edgecolor='white')
axes[1, 0].set_title('地區營收', fontsize=11, fontweight='bold')
axes[1, 0].set_ylabel('營收 (百萬)')
axes[1, 0].grid(True, axis='y', alpha=0.3)

# 4. 單筆金額分布
axes[1, 1].hist(df_sales['revenue'], bins=30, color=ACCENT, edgecolor='white', alpha=0.7)
axes[1, 1].set_title('單筆金額分布', fontsize=11, fontweight='bold')
axes[1, 1].set_xlabel('NT$')
axes[1, 1].set_ylabel('筆數')

fig.suptitle('8.2 銷售儀表板', fontsize=15, fontweight='bold')
save('chart27_sales_dashboard.png', fig)

# 28. 8.3 Threads 文字雲（wordcloud 函式庫）

words_data = {
    'Python': 100, '資料分析': 85, 'pandas': 75, '教學': 70, '學生': 65,
    'Noto': 60, '字型': 55, 'github': 50, '台中': 48, 'AI': 45,
    'ChatGPT': 42, '機器學習': 40, '教授': 38, '大學': 35, '環境': 32,
    '經濟': 30, '視覺化': 28, 'plotly': 26, 'matplotlib': 25, 'seaborn': 22,
    'streamlit': 20, 'deployment': 18, 'OpenDesign': 16, 'statsmodels': 15, 'numpy': 14
}

wc = WordCloud(
    font_path=FONT_PATH,
    width=1600, height=900,
    background_color='white',
    colormap='viridis',
    max_words=200,                # 給足上限，避免 layout 強塞擠壓
    relative_scaling=0.55,        # 詞頻 → 字大小的對比（0.5-0.6 視覺舒服）
    min_font_size=12,
    max_font_size=140,
    prefer_horizontal=0.85,      # 85% 橫排 / 15% 允許直排，避免中文硬轉 90°
    random_state=42,              # 固定 seed，圖穩定
    collocations=False,           # 不合併雙詞組
    margin=6,                     # 字與字之間保留一點 padding
).generate_from_frequencies(words_data)

fig, ax = plt.subplots(figsize=(13, 7))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
ax.set_title('8.3 Threads 文字雲 — Python 學堂熱門關鍵字', fontsize=15, fontweight='bold', pad=15)
save('chart28_threads_wordcloud.png', fig)

# 29. 8.4 環境經濟學個案 — hedonic 模型視覺化
fig, axes = plt.subplots(1, 2, figsize=(14, 5))
np.random.seed(42)
# 模擬 hedonic 模型結果
house_areas = np.random.uniform(20, 80, 100)
house_prices = 100 + 8 * house_areas + np.random.randn(100) * 30

axes[0].scatter(house_areas, house_prices, c=PRIMARY, s=60, alpha=0.6, edgecolors='white')
slope, intercept, r, p, se = stats.linregress(house_areas, house_prices)
axes[0].plot(house_areas, slope * house_areas + intercept, color=ACCENT, linewidth=2.5,
             label=f'β = {slope:.2f} (每坪 ${slope:.1f} 萬)\\np = {p:.4f}')
axes[0].set_title('坪數 → 房價 (hedonic 模型)', fontsize=12, fontweight='bold')
axes[0].set_xlabel('坪數')
axes[0].set_ylabel('房價 (萬)')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# 殘差圖
predicted = slope * house_areas + intercept
residuals = house_prices - predicted
axes[1].scatter(predicted, residuals, c=SUCCESS, s=60, alpha=0.6, edgecolors='white')
axes[1].axhline(0, color=DANGER, linestyle='--', linewidth=2)
axes[1].set_title('殘差圖 (Residual Plot)\n隨機分布 = 模型 OK', fontsize=12, fontweight='bold')
axes[1].set_xlabel('預測值')
axes[1].set_ylabel('殘差')
axes[1].grid(True, alpha=0.3)

fig.suptitle('8.4 環境經濟學：Hedonic 房價模型', fontsize=14, fontweight='bold')
save('chart29_hedonic_model.png', fig)

# 30. 8.5 加強圖：房價 vs AQI 多角度
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
np.random.seed(42)

# (1) 各區散佈 + 迴歸
n = 28
x = np.random.uniform(50, 90, n)
y = 250000 + 1500 * x + np.random.normal(0, 80000, n)
slope, intercept, r, p, se = stats.linregress(x, y)
axes[0, 0].scatter(x, y, c=PRIMARY, s=80, alpha=0.7, edgecolors='white', linewidth=1.5)
axes[0, 0].plot(x, slope * x + intercept, color=ACCENT, linewidth=2.5)
axes[0, 0].set_title(f'全部 28 區: r = {r:.3f}, p = {p:.3f}', fontsize=11, fontweight='bold')
axes[0, 0].set_xlabel('平均 AQI')
axes[0, 0].set_ylabel('中位房價 (NT$)')
axes[0, 0].grid(True, alpha=0.3)

# (2) 分區比較
for i, (label, color) in enumerate([('市中心', ACCENT), ('市郊', PRIMARY), ('山區', SUCCESS)]):
    mask = (i == 0) & (x > 70) | (i == 1) & (x > 55) & (x < 70) | (i == 2) & (x < 55)
    axes[0, 1].scatter(x[mask], y[mask], c=color, s=80, alpha=0.7, label=label, edgecolors='white')
axes[0, 1].legend()
axes[0, 1].set_title('分區比較：市中心 vs 市郊 vs 山區', fontsize=11, fontweight='bold')
axes[0, 1].set_xlabel('平均 AQI')
axes[0, 1].set_ylabel('中位房價 (NT$)')
axes[0, 1].grid(True, alpha=0.3)

# (3) 殘差
predicted = slope * x + intercept
residuals = y - predicted
axes[1, 0].scatter(x, residuals, c=DANGER, s=80, alpha=0.7, edgecolors='white')
axes[1, 0].axhline(0, color=DARK, linestyle='--', linewidth=2)
axes[1, 0].set_title('殘差 vs AQI\n檢查異質性', fontsize=11, fontweight='bold')
axes[1, 0].set_xlabel('平均 AQI')
axes[1, 0].set_ylabel('殘差')
axes[1, 0].grid(True, alpha=0.3)

# (4) QQ plot

(stats.probplot(residuals, dist='norm', plot=axes[1, 1]))
axes[1, 1].set_title('QQ plot: 殘差常態性檢定', fontsize=11, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

fig.suptitle('8.5 空汙 × 房價：完整迴歸診斷', fontsize=15, fontweight='bold')
save('chart30_air_house_diagnostic.png', fig)

print("\n" + "=" * 60)
print(f"✅ 全部 30 張圖完成！")
print(f"輸出目錄: {OUT}/")
print("=" * 60)
