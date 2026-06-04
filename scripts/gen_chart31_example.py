"""
gen_chart31_example.py
生一張「PTT 空汙文字雲」範例圖，塞進 8.5 章

不真打 PTT（避免被 ban + CI 跑），用「模擬 PTT 風格」的中文範例文字
jieba 切詞 → 統計 → wordcloud 畫圖
"""
import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from collections import Counter
import os
import random

random.seed(42)  # 固定結果

# ---------- ① 模擬 PTT 風格的「空汙」討論 ----------
# 仿 8.3 章 Threads 文字雲那種「看起來像真實討論」的句型
# 這不是真實 PTT 抓的, 是教學示範資料
TEMPLATES = [
    "台中火力發電廠空汙真的很嚴重 每天出門都看到灰濛濛一片",
    "中火不減煤 肺癌人數只會繼續增加 經濟部到底在想什麼",
    "空氣品質紅害 學校戶外課全部取消 學生家長都很擔心",
    "PM2.5 超標 口罩戴好戴滿 還要買空氣清淨機才安全",
    "中部空汙問題 根本是結構性問題 要從能源政策下手",
    "咳嗽兩週都沒好 醫生說是空汙引起的過敏 真的崩潰",
    "為什麼台中空氣品質一直這麼差 環保署有在做事嗎",
    "空汙稅應該要開徵 才會有誘因讓企業改善排放",
    "我搬到台中之後氣喘變嚴重 確定跟空汙有關係",
    "火力發電廠和空汙的關係 政府不要再裝睡",
    "空汙指標 AQI 已經紫爆 老人小孩盡量別出門",
    "咳嗽過敏氣喘 空汙真的是慢性病殺手",
    "台中 PM2.5 濃度 每年都超標 居民真的很無奈",
    "中火擴建 環評過關 空汙只會更嚴重",
    "經濟部說要增氣減煤 但時程一直延 到底有沒有效",
    "空汙嚴重的時候 心血管疾病發作率會上升",
    "學校老師說今天空氣品質太差 戶外活動取消",
    "台中火力發電廠 真的是中部空汙的最大兇手",
    "口罩空氣清淨機 已經是家裡標配 不然活不下去",
    "空汙到底要怎麼解決 政府人民都該一起努力",
    "經濟發展和空汙不應該是 trade-off 技術可以解",
    "我支持減煤 但要給台電足夠的時間和配套",
    "空汙問題不解決 台灣的醫療負擔只會越來越重",
    "肺癌已經是新國病 空汙是重要危險因子",
    "中火空汙 受害最深的是彰化南投的居民",
]

# 擴展到約 80 篇文章 (重複抽)
articles = random.choices(TEMPLATES, k=80)
raw = "\n".join(articles)

# ---------- ② 切詞 ----------
text = re.sub(r"[^\u4e00-\u9fff]+", " ", raw)
words = jieba.lcut(text)

# ---------- ③ 停用詞 ----------
STOP = {
    "的", "了", "是", "在", "也", "都", "就", "和", "與", "或",
    "有", "沒", "沒有", "一個", "一些", "什麼", "怎麼", "為什麼",
    "我", "你", "他", "她", "它", "我們", "你們", "他們",
    "這個", "那個", "這樣", "那樣", "可以", "可能", "會",
    "但", "不過", "因為", "所以", "如果", "雖然",
    "今天", "明天", "昨天", "現在", "以前", "之後",
    "真的", "要", "從", "到", "把", "被", "讓",
    "應該", "繼續", "到底", "一直", "已經",
    "https", "http", "com", "www", "ptt", "cc", "html",
    "推", "噓", "→", "※", "看板", "標題", "時間",
}
words = [w for w in words if len(w) >= 2 and w not in STOP]

counter = Counter(words)

print("📊 Top 20 關鍵字 (範例):")
for word, count in counter.most_common(20):
    print(f"  {word:8s}  {count:4d}")

# ---------- ④ 畫文字雲 ----------
font_path = "/Users/elvis/projects/python-learning-site/docs/assets/fonts/NotoSansTC-Regular.otf"
if not os.path.exists(font_path):
    raise SystemExit(f"❌ 找不到字型 {font_path}")

# mpl 標題也要中文字型
from matplotlib import font_manager
font_manager.fontManager.addfont(font_path)
_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams['font.sans-serif'] = [_prop.get_name(), 'sans-serif']
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['axes.unicode_minus'] = False

wc = WordCloud(
    font_path=font_path,
    width=1200,
    height=600,
    background_color="white",
    max_words=150,
    colormap="viridis",
    prefer_horizontal=0.9,
).generate_from_frequencies(counter)

plt.figure(figsize=(14, 7))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("PTT「空汙」討論文字雲 (範例) — 80 篇模擬文章",
          fontsize=15, fontweight="bold", pad=20)
plt.tight_layout()

OUT = "/Users/elvis/projects/python-learning-site/docs/assets/images/chart31_ptt_air_wordcloud_example.png"
plt.savefig(OUT, dpi=120, bbox_inches="tight")
print(f"\n💾 存成 {OUT}")
print(f"   檔案大小: {os.path.getsize(OUT)} bytes")
