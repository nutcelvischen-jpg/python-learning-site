#!/usr/bin/env python3
"""生成第 8 章（4 個實戰）+ 第 9 章 + 5 個附錄"""
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
    # ========== 第 8 章 實戰專案 ==========
    ("chapter08_projects/01-air-quality.md", "第 8 章 · 實戰專案", "8.1 空氣品質分析", "120 分鐘", "整合運用", [
        ("🎯 專案目標", """用環境部 AQI 資料做完整視覺化分析：

- 全台 AQI 分佈
- 縣市比較
- 污染物相關性
- 趨勢分析
"""),
        ("📥 資料準備", """```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

air = pd.read_csv(\"../assets/data/taiwan_aqi_latest.csv\")
print(air.head())
print(air.describe())
```
"""),
        ("📊 全台 AQI 地圖", """```python
# 見 [8.5 章](../../chapter08_projects_extra/05-air-vs-house/) 的圖表程式碼
fig, ax = plt.subplots(figsize=(11, 7))
colors = air['aqi'].apply(lambda x:
    '#16A34A' if x <= 50 else
    '#EAB308' if x <= 100 else
    '#FF6B35' if x <= 150 else '#DC2626'
)
ax.scatter(air['longitude'], air['latitude'], c=colors, s=100, alpha=0.75)
ax.set_title(\"全台 AQI 分佈\")
plt.show()
```
"""),
        ("📈 縣市比較", """```python
county = air.groupby(\"county\")[\"aqi\"].median().sort_values()
county.plot(kind=\"barh\", figsize=(10, 6))
plt.title(\"縣市 AQI 中位數\")
```
"""),
        ("💡 結論", """- 西部走廊 AQI 普遍較高
- 中南部空品較北部差
- 山區空品最好
"""),
    ]),

    ("chapter08_projects/02-sales-dashboard.md", "第 8 章 · 實戰專案", "8.2 銷售儀表板", "120 分鐘", "整合運用", [
        ("🎯 專案目標", """做一個**互動式銷售儀表板**：

- 月營收趨勢
- 產品暢銷排行
- 地區分布
- KPI 卡片
"""),
        ("💻 完整程式碼", """```python
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

np.random.seed(42)
n = 1000
df = pd.DataFrame({
    \"date\": pd.date_range(\"2025-01-01\", periods=n, freq=\"D\"),
    \"product\": np.random.choice([\"A\", \"B\", \"C\"], n),
    \"region\": np.random.choice([\"北\", \"中\", \"南\", \"東\"], n),
    \"quantity\": np.random.randint(1, 20, n),
    \"price\": np.random.randint(100, 5000, n),
})
df[\"revenue\"] = df[\"quantity\"] * df[\"price\"]

# 4 個子圖
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(\"月營收趨勢\", \"產品營收占比\", \"地區分布\", \"單日分布\")
)

# 1. 月趨勢
monthly = df.groupby(df[\"date\"].dt.to_period(\"M\"))[\"revenue\"].sum()
fig.add_trace(
    go.Scatter(x=monthly.index.astype(str), y=monthly.values, mode=\"lines+markers\"),
    row=1, col=1
)

# 2. 產品
prod = df.groupby(\"product\")[\"revenue\"].sum()
fig.add_trace(
    go.Pie(labels=prod.index, values=prod.values),
    row=1, col=2
)

# 3. 地區
reg = df.groupby(\"region\")[\"revenue\"].sum()
fig.add_trace(
    go.Bar(x=reg.index, y=reg.values),
    row=2, col=1
)

# 4. 單日直方圖
fig.add_trace(
    go.Histogram(x=df[\"revenue\"], nbinsx=30),
    row=2, col=2
)

fig.update_layout(height=800, title_text=\"銷售儀表板\", showlegend=False)
fig.show()
```
"""),
        ("🚀 挑戰版", """1. 加 KPI 卡（總營收、平均客單價、毛利率）
2. 加日期區間選擇
3. 串 Streamlit 做網頁版
"""),
    ]),

    ("chapter08_projects/03-threads-mining.md", "第 8 章 · 實戰專案", "8.3 Threads 文字探勘", "90 分鐘", "整合運用", [
        ("🎯 專案目標", """用 jieba 做中文文字探勘：

- 抓 Threads 文字
- 斷詞
- 詞頻統計
- 文字雲
"""),
        ("📦 安裝", """```bash
pip install jieba wordcloud
```
"""),
        ("💻 完整程式碼", """```python
import jieba
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 模擬文字
texts = [
    \"今天天氣真好\",
    \"Python 學堂很讚\",
    \"資料分析好難\",
    \"台北今天下雨\",
    \"Python 是最好的語言\",
]
all_text = \" \".join(texts)

# 斷詞
words = jieba.lcut(all_text)
print(words)

# 詞頻
freq = Counter(words)
print(freq.most_common(10))

# 文字雲
wc = WordCloud(
    font_path=\"NotoSansTC-Regular.otf\",
    width=800, height=400,
    background_color=\"white\"
).generate_from_frequencies(freq)

plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation=\"bilinear\")
plt.axis(\"off\")
plt.show()
```
"""),
        ("🚀 挑戰版", """1. 從 Threads 抓真實資料（用 API）
2. 加 stop words
3. 情緒分析
"""),
    ]),

    ("chapter08_projects/04-env-econ.md", "第 8 章 · 實戰專案", "8.4 環境經濟學個案", "150 分鐘", "整合運用", [
        ("🎯 專案目標", """環境經濟學的完整研究案例：

- 資料收集（空汙 + 房價 + 人口）
- 描述統計
- 相關分析
- 簡單迴歸
- 政策建議
"""),
        ("📋 研究問題", """「PM2.5 對房價有影響嗎？ 控制人口密度後呢？」

這是 hedonic pricing 模型的入門。
"""),
        ("💻 完整程式碼", """```python
import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

# 載入
air = pd.read_csv(\"../assets/data/taiwan_aqi_latest.csv\")
house = pd.read_csv(\"../assets/data/taichung_house_price_2024_2025.csv\")

# 縣市平均 AQI
county_aqi = air.groupby(\"county\")[\"pm2_5\"].mean().reset_index()
county_aqi.columns = [\"city\", \"avg_pm25\"]

# 模擬人口密度資料
# ... (略)

# 合併
df = house.merge(county_aqi, on=\"city\", how=\"left\")
df.dropna(inplace=True)

# 簡單迴歸
X = sm.add_constant(df[[\"avg_pm25\"]])
y = df[\"median_price_per_sqm\"]
model = sm.OLS(y, X).fit()
print(model.summary())
```
"""),
        ("🚀 挑戰版", """1. 完整 hedonic 模型（多變項）
2. 加入時間序列
3. 跨縣市比較
4. 寫成完整研究報告
"""),
    ]),

    # ========== 第 9 章 進階導讀 ==========
    ("chapter09_advanced/01-ml-path.md", "第 9 章 · 進階導讀", "9.1 機器學習路徑", "20 分鐘", "進階", [
        ("🎯 學習目標", """- 認識機器學習全貌
- 知道下一步學什麼
"""),
        ("🛤️ 學習路徑", """```mermaid
graph LR
  A[Python 基礎] --> B[pandas + sklearn]
  B --> C[監督式學習]
  B --> D[非監督式學習]
  C --> E[深度學習]
  D --> F[實戰專案]
  E --> F
```
"""),
        ("📚 推薦書", """- 周志華《機器學習》（西瓜書）
- Aurélien Géron《Hands-On Machine Learning》
- 吳恩達 Coursera 課
"""),
        ("🎯 起步", """```bash
pip install scikit-learn
```
"""),
    ]),

    ("chapter09_advanced/02-crawling.md", "第 9 章 · 進階導讀", "9.2 進階爬蟲", "20 分鐘", "進階", [
        ("🎯 學習目標", """- requests / BeautifulSoup
- 處理動態網頁
- 反爬蟲對策
"""),
        ("🌐 requests", """```python
import requests

r = requests.get(\"https://example.com\")
print(r.status_code)
print(r.text)
```
"""),
        ("🥣 BeautifulSoup", """```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, \"html.parser\")
titles = soup.find_all(\"h2\")
```
"""),
        ("🎭 Selenium（動態）", """```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get(\"https://example.com\")
```
"""),
        ("⚠️ 注意事項", """- 尊重 robots.txt
- 加 delay
- 不要商業濫用
"""),
    ]),

    ("chapter09_advanced/03-deploy.md", "第 9 章 · 進階導讀", "9.3 部署與分享", "20 分鐘", "進階", [
        ("🎯 學習目標", """- Streamlit / Flask
- Docker
- 雲端部署
"""),
        ("🚀 Streamlit", """```python
import streamlit as st
st.title(\"我的第一個 App\")
st.line_chart([1, 2, 3, 4])
```
"""),
        ("🌐 Flask", """```python
from flask import Flask
app = Flask(__name__)

@app.route(\"/\")
def hello():
    return \"Hello World!\"
```
"""),
        ("🐳 Docker", """```dockerfile
FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD [\"python\", \"app.py\"]
```
"""),
    ]),

    # ========== 附錄 ==========
    ("appendix/A-cheatsheet.md", "附錄 A", "A. 速查表", "5 分鐘", "速查", [
        ("📚 內建函式", """```python
len(obj)         # 長度
type(obj)        # 型別
isinstance(x, t) # 判斷型別
print(*args)     # 印
input(prompt)    # 讀
range(start, stop, step)
enumerate(iter)
zip(*iters)
map(fn, iter)
filter(fn, iter)
sorted(iter, key=fn)
reversed(iter)
all(iter)        # 全 True
any(iter)        # 任一 True
```
"""),
        ("📦 串列方法", """```python
lst.append(x)        # 加到尾
lst.insert(i, x)     # 插入
lst.remove(x)        # 移除第一個
lst.pop(i)           # 移除並回傳
lst.sort()           # 排序
lst.reverse()        # 反轉
lst.count(x)         # 算幾個
lst.index(x)         # 第一個 index
lst.copy()           # 複製
lst.extend(other)    # 合併
```
"""),
        ("📖 字典方法", """```python
d[k] = v             # 設
d.get(k, default)    # 取
d.keys() / values() / items()
d.update(other)
d.pop(k)
d.setdefault(k, v)
```
"""),
        ("🐼 pandas 速查", """```python
df = pd.read_csv(\"f.csv\")
df.head() / tail() / describe() / info()
df[\"col\"] / df[[\"c1\", \"c2\"]]
df.loc[i] / df.iloc[i]
df.query(\"cond\")
df.groupby(\"col\").agg(...)
df.merge(other, on=\"key\")
df.pivot_table(...)
df.fillna(0) / dropna()
df.apply(fn)
```
"""),
    ]),

    ("appendix/B-errors-faq.md", "附錄 B", "B. 常見錯誤 FAQ", "10 分鐘", "疑難排解", [
        ("🔥 Top 30 錯誤", """| 錯誤 | 原因 | 修正 |
|---|---|---|
| `SyntaxError: EOL` | 沒關引號 | 檢查所有引號 |
| `NameError` | 變數沒定義 | 先宣告 |
| `TypeError: ... + int` | 字串加數字 | 用 str(int) |
| `IndexError` | list 越界 | 檢查 len |
| `KeyError` | dict 沒這 key | 用 .get() |
| `IndentationError` | 縮排錯 | 4 空格統一 |
| `AttributeError: 'NoneType'` | None 呼叫方法 | 檢查 None |
| `ZeroDivisionError` | 除以 0 | 加 if |
| `FileNotFoundError` | 檔不存在 | 檢查路徑 |
| `ModuleNotFoundError` | 套件沒裝 | pip install |
"""),
        ("🔍 Debug 三步", """1. **讀錯誤訊息最後一行**
2. **看 Traceback 行號**
3. **用 print() 看變數**
"""),
    ]),

    ("appendix/C-resources.md", "附錄 C", "C. 學習資源", "5 分鐘", "資源", [
        ("📖 官方文件", """- [Python 官方教學](https://docs.python.org/3/tutorial/)
- [pandas 文件](https://pandas.pydata.org/docs/)
- [NumPy 文件](https://numpy.org/doc/)
- [Matplotlib 文件](https://matplotlib.org/stable/contents.html)
"""),
        ("📚 書", """- 《Python 程式設計》深入淺出
- 《Python 資料分析》Wes McKinney
- 《精通 Python》Mark Lutz
- 《統計學》Moore
"""),
        ("🎥 YouTube", """- Corey Schafer（英文，超讚）
- StatQuest（統計）
- 彭彭老師（中文）
"""),
        ("🌐 練習平台", """- LeetCode
- HackerRank
- Kaggle（資料科學）
- Codewars
"""),
        ("🇹🇼 台灣社群", """- PyCon Taiwan
- Taipei.py
- 台灣資料科學社群
- Python Taiwan (FB)
"""),
    ]),

    ("appendix/D-glossary.md", "附錄 D", "D. 術語中英對照", "5 分鐘", "參考", [
        ("📖 常見術語", """| 中文 | English |
|---|---|
| 變數 | variable |
| 函式 | function |
| 類別 | class |
| 物件 | object |
| 串列 | list |
| 字典 | dictionary |
| 元組 / 序對 | tuple |
| 集合 | set |
| 迴圈 | loop |
| 流程控制 | control flow |
| 例外 | exception |
| 套件 | package / library |
| 模組 | module |
| 環境 | environment |
| 虛擬環境 | virtual environment |
| 資料框架 | DataFrame |
| 數據分析 | data analysis |
| 機器學習 | machine learning |
| 深度學習 | deep learning |
| 人工智慧 | artificial intelligence |
| 視覺化 | visualization |
"""),
    ]),

    ("appendix/E-answers.md", "附錄 E", "E. 練習題答案", "30 分鐘", "參考", [
        ("⚠️ 使用說明", """!!! warning \"請先自己做再看\"

    這裡的答案是給「卡關時參考」用的。 強烈建議**先自己寫 30 分鐘再來看**。

    練習題的價值在於**思考過程**，不是「答案長怎樣」。
"""),
        ("📝 第 0 章 答案", """#### 練習 1：自我介紹
```python
name = input(\"你叫什麼名字？ \")
age = input(\"你幾歲？ \")
hobby = input(\"興趣？ \")
print(f\"我是 {name}，{age} 歲，興趣是 {hobby}\")
```

#### 練習 2：計算機
```python
a = float(input(\"第一個數: \"))
b = float(input(\"第二個數: \"))
print(f\"和: {a+b}\")
print(f\"差: {a-b}\")
print(f\"積: {a*b}\")
print(f\"商: {a/b}\" if b != 0 else \"除以 0\")
```

#### 練習 3：溫度轉換
```python
c = float(input(\"攝氏: \"))
f = c * 9/5 + 32
print(f\"華氏: {f}\")
```

#### 練習 4：BMI
```python
kg = float(input(\"體重 kg: \"))
cm = float(input(\"身高 cm: \"))
bmi = kg / (cm/100) ** 2
print(f\"BMI: {bmi:.1f}\")
```

#### 練習 5：Debug
```python
name = input(\"你叫什麼名字？\")   # 補引號
age = int(input(\"你幾歲？ \"))     # 補右括號
print(f\"你是 {name}, {age} 歲\")   # 改 Age → age
```
"""),
        ("📚 各章答案", """完整答案持續更新中。 各章練習題的標準答案放在 [GitHub Repo](https://github.com/nutcelvischen-jpg/python-learning-site/tree/main/answers) 的 `answers/` 目錄。

建議從 **pull request** 提交你的解答，跟社群互動學習！
"""),
        ("💡 提交流程", """1. Fork 這個 repo
2. 寫你的解答到 `answers/chapterXX/`
3. 開 Pull Request
4. 社群 review + 討論
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
