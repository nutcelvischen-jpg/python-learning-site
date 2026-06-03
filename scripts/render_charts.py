#!/usr/bin/env python3
"""
render_charts.py — 為 Python 學堂教學網站產生所有視覺化圖表
使用 matplotlib + seaborn + plotly
"""
import os
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.use('Agg')  # No display
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import pandas as pd
import numpy as np

# 中文字型設定（macOS 預設）
import matplotlib.font_manager as fm
plt.rcParams['font.sans-serif'] = ['Noto Sans TC', 'PingFang TC', 'Heiti TC', 'Microsoft JhengHei', 'Arial Unicode MS', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

# 自訂配色（Open Design 啟發）
PY_BLUE = '#3776AB'
CREATIVE_ORANGE = '#FF6B35'
PY_YELLOW = '#FFD43B'
NIGHT = '#0F172A'
GRAY = '#475569'
LIGHT = '#E2E8F0'

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.join(HERE, "..", "docs", "assets", "images")
os.makedirs(OUT_DIR, exist_ok=True)

def save_fig(fig, name, dpi=120, bbox='tight'):
    path = os.path.join(OUT_DIR, name)
    fig.savefig(path, dpi=dpi, bbox_inches=bbox, facecolor='white')
    plt.close(fig)
    size = os.path.getsize(path) / 1024
    print(f"  ✅ {name}  ({size:.0f} KB)")

# 讀真實資料
air = pd.read_csv(os.path.join(HERE, "..", "docs", "assets", "data", "taiwan_aqi_latest.csv"))
house = pd.read_csv(os.path.join(HERE, "..", "docs", "assets", "data", "taichung_house_price_2024_2025.csv"))

# =====================================================
# Chart 1: 8.5 章主視覺 — 全台 AQI 地圖散佈圖
# =====================================================
print("\n📊 圖表 1: 全台 AQI 分佈圖")
fig, ax = plt.subplots(figsize=(11, 7))
colors = air['aqi'].apply(lambda x:
    '#16A34A' if x <= 50 else          # 良好 綠
    '#EAB308' if x <= 100 else          # 普通 黃
    '#FF6B35' if x <= 150 else          # 對敏感族群不健康 橘
    '#DC2626'                          # 不健康 紅
)
sizes = air['pm2_5'].fillna(0) * 8 + 30
scatter = ax.scatter(air['longitude'], air['latitude'], c=colors, s=sizes, alpha=0.75, edgecolors='white', linewidth=1)
for i, row in air.iterrows():
    if row['aqi'] >= 70:  # 只標 AQI 較高的
        ax.annotate(row['sitename'], (row['longitude'], row['latitude']),
                    xytext=(4, 4), textcoords='offset points', fontsize=8, color=NIGHT)

# 圖例
legend_patches = [
    mpatches.Patch(color='#16A34A', label='良好 (0-50)'),
    mpatches.Patch(color='#EAB308', label='普通 (51-100)'),
    mpatches.Patch(color='#FF6B35', label='對敏感族群不健康 (101-150)'),
    mpatches.Patch(color='#DC2626', label='不健康 (151+)'),
]
ax.legend(handles=legend_patches, loc='lower left', frameon=True, fontsize=10, title='AQI 等級')
ax.set_xlabel('經度 (°E)', fontsize=11, color=GRAY)
ax.set_ylabel('緯度 (°N)', fontsize=11, color=GRAY)
ax.set_title('全台 84 個空品測站即時 AQI 分佈（2026-06-04 05:00）',
             fontsize=14, fontweight='bold', color=NIGHT, pad=15)
ax.grid(True, alpha=0.2, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_facecolor('#FAFBFC')
save_fig(fig, 'chart1_taiwan_aqi_map.png')

# =====================================================
# Chart 2: 縣市 AQI 中位數比較
# =====================================================
print("\n📊 圖表 2: 縣市 AQI 排行")
county_avg = air.groupby('county')['aqi'].agg(['median', 'count']).sort_values('median', ascending=False).head(12)
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(county_avg.index, county_avg['median'],
               color=[PY_BLUE if v <= 50 else CREATIVE_ORANGE if v <= 100 else '#DC2626' for v in county_avg['median']])
ax.set_xlabel('AQI 中位數', fontsize=11, color=GRAY)
ax.set_title('全台各縣市 AQI 中位數排名（取前 12 名）', fontsize=13, fontweight='bold', color=NIGHT, pad=15)
ax.invert_yaxis()
ax.grid(True, axis='x', alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# 標數字
for bar, val in zip(bars, county_avg['median']):
    ax.text(val + 1, bar.get_y() + bar.get_height()/2, f'{val:.0f}',
            va='center', fontsize=9, color=GRAY)
ax.set_facecolor('#FAFBFC')
save_fig(fig, 'chart2_county_aqi_ranking.png')

# =====================================================
# Chart 3: PM2.5 vs O3 散佈圖（含顏色分群）
# =====================================================
print("\n📊 圖表 3: PM2.5 vs O3 散佈圖")
fig, ax = plt.subplots(figsize=(10, 6))
data = air.dropna(subset=['pm2_5', 'o3'])
scatter = ax.scatter(data['pm2_5'], data['o3'],
                     c=data['aqi'], cmap='RdYlGn_r', s=120, alpha=0.75,
                     edgecolors='white', linewidth=1.5)
cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label('AQI', fontsize=10, color=GRAY)
# 標出極端值
for i, row in data.nlargest(3, 'pm2_5').iterrows():
    ax.annotate(row['sitename'], (row['pm2_5'], row['o3']),
                xytext=(5, 5), textcoords='offset points', fontsize=9, color=NIGHT)
ax.set_xlabel('PM2.5 (μg/m³)', fontsize=11, color=GRAY)
ax.set_ylabel('O3 臭氧 (ppb)', fontsize=11, color=GRAY)
ax.set_title('PM2.5 vs O3 關聯性（顏色 = AQI）', fontsize=13, fontweight='bold', color=NIGHT, pad=15)
ax.grid(True, alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_facecolor('#FAFBFC')
save_fig(fig, 'chart3_pm25_vs_o3.png')

# =====================================================
# Chart 4: 臺中市各區房價 × AQI 雙軸圖（8.5 章核心）
# =====================================================
print("\n📊 圖表 4: 臺中市房價 × 空汙雙軸圖 (8.5 章主圖)")
# 整合資料：取臺中市各區的中位 AQI（從測站）
taichung_stations = air[air['county'] == '臺中市'].copy()
taichung_aqi = taichung_stations.set_index('sitename')['aqi']

# 對照行政區與測站（簡化對照表）
district_to_station = {
    '中區': '忠明', '東區': '忠明', '南區': '大里', '西區': '西屯',
    '北區': '西屯', '北屯區': '西屯', '西屯區': '西屯', '南屯區': '大里',
    '太平區': '大里', '大里區': '大里', '霧峰區': '南投', '烏日區': '大里',
    '豐原區': '豐原', '后里區': '豐原', '石岡區': '豐原', '東勢區': '豐原',
    '和平區': '豐原', '潭子區': '豐原', '大雅區': '沙鹿', '神岡區': '豐原',
    '大肚區': '沙鹿', '沙鹿區': '沙鹿', '龍井區': '沙鹿', '梧棲區': '沙鹿',
    '清水區': '沙鹿', '大甲區': '沙鹿', '外埔區': '沙鹿', '大安區': '沙鹿'
}
house['avg_aqi'] = house['district'].map(lambda d: taichung_aqi.get(district_to_station.get(d, '西屯'), np.nan))
house_clean = house.dropna(subset=['avg_aqi']).copy()

fig, ax1 = plt.subplots(figsize=(12, 6.5))
# 主軸：房價
ax1.set_xlabel('臺中市行政區', fontsize=11, color=GRAY)
ax1.set_ylabel('中位房價 (NT$ / m²)', fontsize=11, color=PY_BLUE, fontweight='bold')
bars = ax1.bar(house_clean['district'], house_clean['median_price_per_sqm'],
               color=PY_BLUE, alpha=0.75, label='中位房價', edgecolor='white', linewidth=1)
ax1.tick_params(axis='y', labelcolor=PY_BLUE)
ax1.tick_params(axis='x', rotation=45)
# 標中位數
for bar, val in zip(bars, house_clean['median_price_per_sqm']):
    ax1.text(bar.get_x() + bar.get_width()/2, val + 5000, f'{val/1000:.0f}K',
             ha='center', va='bottom', fontsize=8, color=PY_BLUE, fontweight='bold')

# 副軸：AQI
ax2 = ax1.twinx()
ax2.set_ylabel('AQI', fontsize=11, color=CREATIVE_ORANGE, fontweight='bold')
ax2.plot(house_clean['district'], house_clean['avg_aqi'],
         color=CREATIVE_ORANGE, marker='o', markersize=10, linewidth=2.5,
         label='AQI', markeredgecolor='white', markeredgewidth=2)
ax2.tick_params(axis='y', labelcolor=CREATIVE_ORANGE)
ax2.axhline(y=50, color='#16A34A', linestyle='--', alpha=0.5, label='良好閾值 50')
ax2.axhline(y=100, color=CREATIVE_ORANGE, linestyle='--', alpha=0.5, label='不健康閾值 100')

ax1.set_title('臺中市各行政區：中位房價 vs 平均 AQI',
          fontsize=14, fontweight='bold', color=NIGHT, pad=20)
ax1.grid(True, axis='y', alpha=0.2, linestyle='--')
ax1.set_facecolor('#FAFBFC')
# 合併圖例
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right', frameon=True, fontsize=9)
ax1.spines['top'].set_visible(False)
ax2.spines['top'].set_visible(False)
fig.tight_layout()
save_fig(fig, 'chart4_taichung_house_air.png')

# =====================================================
# Chart 5: 相關性散佈圖 + 迴歸線（8.5 章統計）
# =====================================================
print("\n📊 圖表 5: 房價 vs AQI 相關性分析")
fig, ax = plt.subplots(figsize=(10, 6.5))
x = house_clean['avg_aqi']
y = house_clean['median_price_per_sqm']
ax.scatter(x, y, s=house_clean['sample_count']*2, alpha=0.6,
           c=PY_BLUE, edgecolors=CREATIVE_ORANGE, linewidth=2)
# 迴歸線
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
xs = np.linspace(x.min(), x.max(), 100)
ax.plot(xs, p(xs), '--', color=CREATIVE_ORANGE, linewidth=2.5,
        label=f'y = {z[0]:.0f}x + {z[1]:.0f}')
# 算相關係數
corr = np.corrcoef(x, y)[0, 1]
ax.text(0.05, 0.95, f'相關係數 r = {corr:.3f}\n樣本數 n = {len(x)}',
        transform=ax.transAxes, fontsize=12, verticalalignment='top',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='white', edgecolor=PY_BLUE, linewidth=1.5),
        color=NIGHT, fontweight='bold')
# 標出顯著點
for i, row in house_clean.iterrows():
    if row['sample_count'] > 300:
        ax.annotate(row['district'], (row['avg_aqi'], row['median_price_per_sqm']),
                    xytext=(8, 8), textcoords='offset points', fontsize=9,
                    color=NIGHT, fontweight='bold')
ax.set_xlabel('平均 AQI', fontsize=11, color=GRAY)
ax.set_ylabel('中位房價 (NT$ / m²)', fontsize=11, color=GRAY)
ax.set_title('臺中市各區：房價 vs 空氣品質相關性分析',
             fontsize=13, fontweight='bold', color=NIGHT, pad=15)
ax.grid(True, alpha=0.3, linestyle='--')
ax.legend(loc='lower right', fontsize=10, frameon=True)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_facecolor('#FAFBFC')
save_fig(fig, 'chart5_price_air_correlation.png')

# =====================================================
# Chart 6: 教學用 — 基礎 matplotlib 範例
# =====================================================
print("\n📊 圖表 6: 基礎 matplotlib 範例")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
x = np.linspace(0, 10, 100)
axes[0].plot(x, np.sin(x), label='sin(x)', color=PY_BLUE, linewidth=2.5)
axes[0].plot(x, np.cos(x), label='cos(x)', color=CREATIVE_ORANGE, linewidth=2.5)
axes[0].set_title('線圖 (Line Chart)', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].bar(['A', 'B', 'C', 'D', 'E'], [3, 7, 2, 5, 8], color=PY_BLUE, alpha=0.75)
axes[1].set_title('長條圖 (Bar Chart)', fontsize=12, fontweight='bold')
axes[1].grid(True, axis='y', alpha=0.3)

for ax in axes:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
fig.suptitle('matplotlib 基礎圖表範例', fontsize=14, fontweight='bold', color=NIGHT)
fig.tight_layout()
save_fig(fig, 'chart6_matplotlib_basics.png')

# =====================================================
# Chart 7: 教學用 — pandas 樞紐分析
# =====================================================
print("\n📊 圖表 7: 教學用 heatmap")
np.random.seed(42)
data = np.random.rand(8, 6)
fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(data, annot=True, fmt='.2f', cmap='YlOrRd',
            xticklabels=['週一', '週二', '週三', '週四', '週五', '週六'],
            yticklabels=['台北', '台中', '台南', '高雄', '新竹', '基隆', '花蓮', '台東'],
            cbar_kws={'label': '銷售量'}, ax=ax, linewidths=0.5)
ax.set_title('各城市 × 星期 銷售量熱力圖', fontsize=13, fontweight='bold', color=NIGHT, pad=15)
save_fig(fig, 'chart7_heatmap_example.png')

# =====================================================
# Chart 8: NumPy broadcasting 視覺化
# =====================================================
print("\n📊 圖表 8: NumPy broadcasting 視覺化")
fig, ax = plt.subplots(figsize=(9, 5))
A = np.ones((3, 1)) * np.array([1, 2, 3]).reshape(-1, 1)
B = np.ones((1, 4)) * np.array([10, 20, 30, 40]).reshape(1, -1)
C = A * B
im = ax.imshow(C, cmap='viridis', aspect='auto')
ax.set_xticks(range(4))
ax.set_xticklabels([10, 20, 30, 40])
ax.set_yticks(range(3))
ax.set_yticklabels([1, 2, 3])
ax.set_xlabel('B 軸', fontsize=11, color=GRAY)
ax.set_ylabel('A 軸', fontsize=11, color=GRAY)
ax.set_title('NumPy Broadcasting 視覺化：A[3,1] × B[1,4] → C[3,4]',
             fontsize=13, fontweight='bold', color=NIGHT, pad=15)
for i in range(3):
    for j in range(4):
        ax.text(j, i, f'{C[i, j]}', ha='center', va='center',
                color='white' if C[i, j] > 30 else 'black', fontweight='bold')
plt.colorbar(im, ax=ax, label='數值')
save_fig(fig, 'chart8_numpy_broadcasting.png')

# =====================================================
# Chart 9: pandas 時間序列範例
# =====================================================
print("\n📊 圖表 9: pandas 時間序列")
dates = pd.date_range('2025-01-01', periods=180, freq='D')
np.random.seed(42)
values = 100 + np.cumsum(np.random.randn(180) * 2) + np.sin(np.arange(180)/20) * 10
ts = pd.Series(values, index=dates)

fig, ax = plt.subplots(figsize=(11, 5))
ax.plot(ts.index, ts.values, color=PY_BLUE, linewidth=1.5, alpha=0.85, label='原始')
rolling30 = ts.rolling(30).mean()
ax.plot(rolling30.index, rolling30.values, color=CREATIVE_ORANGE, linewidth=3, label='30 日移動平均')
ax.fill_between(ts.index, ts.values, alpha=0.15, color=PY_BLUE)
ax.set_title('pandas 時間序列 + 移動平均（30 日均線）',
             fontsize=13, fontweight='bold', color=NIGHT, pad=15)
ax.set_xlabel('日期', fontsize=11, color=GRAY)
ax.set_ylabel('股價 / 指標值', fontsize=11, color=GRAY)
ax.legend(loc='upper left', frameon=True, fontsize=10)
ax.grid(True, alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_facecolor('#FAFBFC')
save_fig(fig, 'chart9_pandas_timeseries.png')

# =====================================================
# Chart 10: 第 1 章 - 串列視覺化
# =====================================================
print("\n📊 圖表 10: 第 1 章 list 概念圖")
fig, ax = plt.subplots(figsize=(11, 4))
fruits = ['🍎蘋果', '🍌香蕉', '🍇葡萄', '🍊橘子', '🍓草莓', '🥝奇異果', '🍑水蜜桃', '🍒櫻桃']
colors_list = ['#DC2626', '#EAB308', '#7C3AED', '#EA580C', '#EC4899', '#16A34A', '#FB7185', '#BE123C']

for i, (fruit, color) in enumerate(zip(fruits, colors_list)):
    rect = mpatches.FancyBboxPatch((i*1.3, 0.5), 1.2, 0.8,
                                    boxstyle="round,pad=0.05",
                                    facecolor=color, alpha=0.85, edgecolor='white', linewidth=2)
    ax.add_patch(rect)
    ax.text(i*1.3 + 0.6, 0.9, fruit, ha='center', va='center', fontsize=12, color='white', fontweight='bold')
    ax.text(i*1.3 + 0.6, 0.3, f'[{i}]', ha='center', va='center', fontsize=10, color=GRAY, fontweight='bold')

ax.set_xlim(-0.3, 10.4)
ax.set_ylim(0, 1.5)
ax.set_title('Python list（串列）概念圖 — 每個元素都有 index',
             fontsize=13, fontweight='bold', color=NIGHT, pad=15)
ax.axis('off')
save_fig(fig, 'chart10_list_concept.png')

# =====================================================
# Chart 11: 第 1 章 - 字典概念圖
# =====================================================
print("\n📊 圖表 11: 第 1 章 dict 概念圖")
fig, ax = plt.subplots(figsize=(10, 5))
pairs = [('name', 'Elvis'), ('age', '35'), ('job', '教授'),
         ('city', '台中'), ('lang', 'Python'), ('teach', '經濟學')]
for i, (k, v) in enumerate(pairs):
    y = 5 - i * 0.7
    # key 框
    key_box = mpatches.FancyBboxPatch((0.5, y-0.2), 2, 0.5,
                                      boxstyle="round,pad=0.05",
                                      facecolor=PY_BLUE, alpha=0.85, edgecolor='white', linewidth=2)
    ax.add_patch(key_box)
    ax.text(1.5, y + 0.05, f'"{k}"', ha='center', va='center', fontsize=11, color='white', fontweight='bold')
    # 箭頭
    ax.annotate('', xy=(4.5, y + 0.05), xytext=(2.6, y + 0.05),
                arrowprops=dict(arrowstyle='->', color=CREATIVE_ORANGE, lw=2))
    # value 框
    val_box = mpatches.FancyBboxPatch((4.5, y-0.2), 2.5, 0.5,
                                      boxstyle="round,pad=0.05",
                                      facecolor=CREATIVE_ORANGE, alpha=0.85, edgecolor='white', linewidth=2)
    ax.add_patch(val_box)
    ax.text(5.75, y + 0.05, f'"{v}"', ha='center', va='center', fontsize=11, color='white', fontweight='bold')

ax.set_xlim(0, 8)
ax.set_ylim(0, 6)
ax.set_title('Python dict（字典）概念圖 — key:value 配對',
             fontsize=13, fontweight='bold', color=NIGHT, pad=15)
ax.text(1.5, 0.3, 'Key（鍵）', ha='center', fontsize=10, color=PY_BLUE, fontweight='bold')
ax.text(5.75, 0.3, 'Value（值）', ha='center', fontsize=10, color=CREATIVE_ORANGE, fontweight='bold')
ax.axis('off')
save_fig(fig, 'chart11_dict_concept.png')

# =====================================================
# Chart 12: 統計章 - 常態分佈
# =====================================================
print("\n📊 圖表 12: 常態分佈視覺化")
fig, ax = plt.subplots(figsize=(11, 5))
x = np.linspace(-4, 4, 200)
y = np.exp(-x**2/2) / np.sqrt(2*np.pi)
ax.plot(x, y, color=PY_BLUE, linewidth=3, label='常態分佈 N(0,1)')
ax.fill_between(x, y, where=(x >= -1) & (x <= 1), alpha=0.3, color=PY_BLUE, label='±1σ (68.3%)')
ax.fill_between(x, y, where=(x >= -2) & (x <= 2), alpha=0.2, color=CREATIVE_ORANGE, label='±2σ (95.4%)')
ax.fill_between(x, y, where=(x >= -3) & (x <= 3), alpha=0.1, color=PY_YELLOW, label='±3σ (99.7%)')
ax.axvline(0, color=NIGHT, linestyle='--', alpha=0.5)
ax.text(0, 0.42, 'μ=0', ha='center', fontsize=12, color=NIGHT, fontweight='bold')
ax.set_title('標準常態分佈與經驗法則（68-95-99.7）',
             fontsize=13, fontweight='bold', color=NIGHT, pad=15)
ax.set_xlabel('z-score', fontsize=11, color=GRAY)
ax.set_ylabel('機率密度', fontsize=11, color=GRAY)
ax.legend(loc='upper right', fontsize=10, frameon=True)
ax.grid(True, alpha=0.3)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_facecolor('#FAFBFC')
save_fig(fig, 'chart12_normal_distribution.png')

print("\n🎉 全部圖表產出完成！")
print(f"   圖表位置: {OUT_DIR}")
print(f"   總共: {len(os.listdir(OUT_DIR))} 個檔案")
