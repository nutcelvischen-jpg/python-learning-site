#!/usr/bin/env python3
"""只重跑 chart28 — 從 render_charts.py 抽出來的最小版本。"""
import os
import warnings
warnings.filterwarnings('ignore')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
from wordcloud import WordCloud

# 字型
FONT_PATH = 'docs/assets/fonts/NotoSansTC-Regular.otf'
font_manager.fontManager.addfont(FONT_PATH)
_prop = font_manager.FontProperties(fname=FONT_PATH)
plt.rcParams['font.sans-serif'] = [_prop.get_name(), 'sans-serif']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

OUT = 'docs/assets/images'
os.makedirs(OUT, exist_ok=True)

words_data = {
    'Python': 100, '資料分析': 85, 'pandas': 75, '教學': 70, '學生': 65,
    'Noto': 60, '字型': 55, 'github': 50, '台中': 48, 'AI': 45,
    'ChatGPT': 42, '機器學習': 40, '教授': 38, '大學': 35, '環境': 32,
    '經濟': 30, '視覺化': 28, 'plotly': 26, 'matplotlib': 25, 'seaborn': 22,
    'streamlit': 20, 'deployment': 18, 'OpenDesign': 16, 'statsmodels': 15, 'numpy': 14,
}

wc = WordCloud(
    font_path=FONT_PATH,
    width=1600, height=900,
    background_color='white',
    colormap='viridis',
    max_words=200,
    relative_scaling=0.55,
    min_font_size=12,
    max_font_size=140,
    prefer_horizontal=0.85,
    random_state=42,
    collocations=False,
    margin=6,
).generate_from_frequencies(words_data)

fig, ax = plt.subplots(figsize=(13, 7))
ax.imshow(wc, interpolation='bilinear')
ax.axis('off')
ax.set_title('8.3 Threads 文字雲 — Python 學堂熱門關鍵字',
             fontsize=15, fontweight='bold', pad=15)
fig.tight_layout()
fig.savefig(f'{OUT}/chart28_threads_wordcloud.png',
            bbox_inches='tight', facecolor='white', dpi=110)
plt.close(fig)
print('  chart28_threads_wordcloud.png  OK')
