---
title: "8.3 Threads 文字探勘"
---

<div class="lesson-header">
  <span class="chapter-tag">第 8 章 · 實戰專案</span>
  <h1>8.3 Threads 文字探勘</h1>
  <div class="meta">
    <span>⏱️ 90 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 整合運用</span>
  </div>
</div>

## 🎯 專案目標

用 jieba 做中文文字探勘：

- 抓 Threads 文字
- 斷詞
- 詞頻統計
- 文字雲


## 📦 安裝

```bash
pip install jieba wordcloud
```


## 💻 完整程式碼

```python
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 模擬文字
texts = [
    "今天天氣真好",
    "Python 學堂很讚",
    "資料分析好難",
    "台北今天下雨",
    "Python 是最好的語言",
]
all_text = " ".join(texts)

# 斷詞
words = jieba.lcut(all_text)
print(words)

# 詞頻
freq = Counter(words)
print(freq.most_common(10))

# 文字雲
wc = WordCloud(
    font_path="NotoSansTC-Regular.otf",
    width=800, height=400,
    background_color="white"
).generate_from_frequencies(freq)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
```


## 🚀 挑戰版

1. 從 Threads 抓真實資料（用 API）
2. 加 stop words
3. 情緒分析


