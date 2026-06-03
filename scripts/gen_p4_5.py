#!/usr/bin/env python3
"""生成第 4-9 章 + 第 8 章實戰 + 附錄"""
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
    # ========== 第 4 章 NumPy ==========
    ("chapter04_numpy/01-intro.md", "第 4 章 · NumPy", "4.1 NumPy 簡介", "15 分鐘", "資料分析", [
        ("🎯 學習目標", """- 知道 NumPy 是什麼
- 為什麼 list 不夠用
- 學會安裝跟 import
"""),
        ("⚡ NumPy = Numerical Python", """```python
import numpy as np

# Python list
list_a = [1, 2, 3, 4, 5]
list_b = [10, 20, 30, 40, 50]

# 想算 list_a + list_b 怎麼辦？
# 得寫 for 迴圈
result = [a + b for a, b in zip(list_a, list_b)]

# NumPy 一次搞定
arr_a = np.array(list_a)
arr_b = np.array(list_b)
result = arr_a + arr_b    # [11, 22, 33, 44, 55]
```
"""),
        ("🏃 速度差異", """NumPy 用 C 實作，比純 Python **快 10-100x**。

```python
import numpy as np
import time

n = 1_000_000
py_list = list(range(n))
np_arr = np.arange(n)

# 純 Python sum
t0 = time.time()
sum(py_list)
print(f"Python: {time.time() - t0:.3f}s")

# NumPy sum
t0 = time.time()
np.sum(np_arr)
print(f"NumPy:   {time.time() - t0:.3f}s")
```
"""),
        ("✏️ 練習題", """1. 比較 Python list 跟 NumPy 算 100 萬個元素加法的速度
2. 印出 np.__version__
"""),
    ]),

    ("chapter04_numpy/02-ndarray.md", "第 4 章 · NumPy", "4.2 ndarray 建立/索引/切片", "25 分鐘", "資料分析", [
        ("🎯 學習目標", """- 學會建立 ndarray
- 索引跟切片
- 常用屬性：shape / dtype / ndim
"""),
        ("🏗️ 建立 ndarray", """```python
import numpy as np

# 從 list
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])   # 2D

# 特殊陣列
np.zeros(5)          # [0, 0, 0, 0, 0]
np.ones((2, 3))      # 2x3 全 1
np.full((2, 2), 7)   # 2x2 全 7
np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
np.linspace(0, 1, 5) # [0, 0.25, 0.5, 0.75, 1]
np.eye(3)            # 3x3 單位矩陣
np.random.rand(3, 4) # 0-1 隨機
```
"""),
        ("🔪 索引切片", """```python
a = np.array([10, 20, 30, 40, 50])
print(a[0])     # 10
print(a[-1])    # 50
print(a[1:4])   # [20, 30, 40]
print(a[::2])   # [10, 30, 50]

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b[0, 1])     # 2
print(b[:, 0])     # 第一欄 [1, 4, 7]
print(b[1, :])     # 第二列 [4, 5, 6]
```
"""),
        ("🔍 屬性", """```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)    # (2, 3)
print(a.dtype)    # int64
print(a.ndim)     # 2
print(a.size)     # 6
```
"""),
        ("✏️ 練習題", """1. 建立 1D ndarray 含 1-10
2. 建立 3x3 全 0 陣列
3. 建立 2x5 identity matrix
4. 切片取出第 2 列第 3 欄
"""),
    ]),

    ("chapter04_numpy/03-shape.md", "第 4 章 · NumPy", "4.3 形狀操作", "20 分鐘", "資料分析", [
        ("🎯 學習目標", """- reshape / ravel / transpose
- 改陣列形狀
"""),
        ("🔄 reshape", """```python
import numpy as np

a = np.arange(12)        # [0, 1, ..., 11]
b = a.reshape(3, 4)      # 3x4 矩陣
c = a.reshape(2, 2, 3)   # 2x2x3 張量

# -1 自動算
d = a.reshape(2, -1)     # 2x6
e = a.reshape(-1, 4)     # 3x4
```
"""),
        ("↔️ ravel / flatten", """```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ravel())     # [1, 2, 3, 4, 5, 6]  # view
print(a.flatten())   # [1, 2, 3, 4, 5, 6]  # copy
```
"""),
        ("↕️ transpose", """```python
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.T)   # 轉置
# [[1, 4],
#  [2, 5],
#  [3, 6]]
```
"""),
        ("🔗 stack / split", """```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 合併
np.concatenate([a, b])          # [1, 2, 3, 4, 5, 6]
np.vstack([a, b])              # 垂直疊
np.hstack([a, b])              # 水平排

# 切割
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
np.split(c, 2, axis=1)          # 兩半
```
"""),
        ("✏️ 練習題", """1. 把 [1,12] reshape 成 3x4
2. 計算 3x4 矩陣的轉置
3. 合併兩個 1D array
"""),
    ]),

    ("chapter04_numpy/04-broadcasting.md", "第 4 章 · NumPy", "4.4 向量化與 broadcasting", "25 分鐘", "資料分析", [
        ("🎯 學習目標", """- 理解 broadcasting 規則
- 寫出高效的向量化運算
"""),
        ("🌊 什麼是 broadcasting", """不同形狀的陣列**自動擴展**做運算。

```python
import numpy as np

a = np.array([1, 2, 3])
b = 10                # 純量
print(a + b)          # [11, 12, 13]  ← 自動擴展

c = np.array([10, 20, 30])
print(a + c)          # [11, 22, 33]  ← 元素對元素
```
"""),
        ("📏 規則", """1. 如果兩個陣列維度數不同，小的補 1 在左邊
2. 如果形狀不相等，會在 size 1 的維度擴展
3. 如果還是不合，broadcasting 失敗

```python
# 範例 1: (3,) + (1,) → (3,)
a = np.array([1, 2, 3])
b = np.array([10])
print(a + b)    # [11, 12, 13]

# 範例 2: (3, 1) + (1, 4) → (3, 4)
a = np.array([[1], [2], [3]])      # 3x1
b = np.array([[10, 20, 30, 40]])   # 1x4
print(a + b)
# [[11, 21, 31, 41],
#  [12, 22, 32, 42],
#  [13, 23, 33, 43]]
```
"""),
        ("💡 為什麼好用", """```python
# 不用 for 迴圈
prices = np.array([100, 200, 300])
discounts = np.array([[0.9], [0.8], [0.7]])   # 3x1
final = prices * discounts                     # 3x3
```
"""),
        ("✏️ 練習題", """1. 算陣列 `[[1,2,3], [4,5,6]]` 加 10 的結果
2. (3,1) + (1,4) broadcasting 後形狀
3. 用 broadcasting 算 5 個產品 3 種稅率的價格
"""),
    ]),

    ("chapter04_numpy/05-stats.md", "第 4 章 · NumPy", "4.5 統計函式", "20 分鐘", "資料分析", [
        ("🎯 學習目標", """- 學會 sum / mean / std / median
- 沿軸計算（axis）
"""),
        ("📊 基本統計", """```python
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(a.sum())         # 55
print(a.mean())        # 5.5
print(a.std())         # 2.872
print(a.var())         # 8.25
print(a.min())         # 1
print(a.max())         # 10
print(np.median(a))    # 5.5
print(np.percentile(a, 75))  # 7.75
```
"""),
        ("↕️ 沿軸計算", """```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a.sum(axis=0))   # [5, 7, 9]   每欄加總
print(a.sum(axis=1))   # [6, 15]     每列加總
print(a.mean(axis=0))  # [2.5, 3.5, 4.5]
```
"""),
        ("🔍 argmax / where", """```python
a = np.array([3, 1, 4, 1, 5, 9, 2, 6])
print(a.argmax())     # 5（最大值的 index）
print(a.argmin())     # 1

print(np.where(a > 3))            # 回傳符合條件的 index
print(np.where(a > 3, a, 0))     # 條件為真留 a，否則 0
```
"""),
        ("✏️ 練習題", """1. 算 [1..100] 的 mean / std / median
2. 隨機 1000 個常態分佈樣本，算分位數
3. 沿 axis=0 算 2D 陣列的 mean
"""),
    ]),

    ("chapter04_numpy/06-random-linalg.md", "第 4 章 · NumPy", "4.6 隨機數與線代", "20 分鐘", "資料分析", [
        ("🎯 學習目標", """- 隨機數生成
- 線性代數基本運算
"""),
        ("🎲 隨機數", """```python
import numpy as np

np.random.seed(42)      # 設種子（讓結果可重現）

np.random.rand(5)       # 5 個 0-1 均勻
np.random.randn(5)      # 5 個標準常態
np.random.randint(1, 100, 10)  # 1-100 整數 10 個
np.random.choice([1,2,3,4,5], 3)  # 隨機抽 3 個

# 重要：攪亂順序
arr = np.arange(10)
np.random.shuffle(arr)
print(arr)

# 抽樣
np.random.choice(arr, 3, replace=False)
```
"""),
        ("📐 線性代數", """```python
from numpy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

# 解聯立方程組 Ax = b
x = linalg.solve(A, b)
print(x)    # [-4.  4.5]

# 反矩陣
A_inv = linalg.inv(A)

# 特徵值
eigvals, eigvecs = linalg.eig(A)

# 行列式
print(linalg.det(A))    # -2.0
```
"""),
        ("✏️ 練習題", """1. 模擬 1000 次丟 2 個骰子，畫分佈
2. 解 2x2 聯立方程組
3. 算 3x3 矩陣的特徵值
"""),
    ]),

    # ========== 第 5 章 pandas ==========
    ("chapter05_pandas/01-intro.md", "第 5 章 · pandas", "5.1 Series 與 DataFrame", "25 分鐘", "資料分析", [
        ("🎯 學習目標", """- 認識 Series 與 DataFrame
- 從 list / dict 建立
- 基本屬性與方法
"""),
        ("🐼 pandas 是什麼", """```python
import pandas as pd

# Series: 一維（像有 index 的 list）
s = pd.Series([10, 20, 30, 40], index=[\"a\", \"b\", \"c\", \"d\"])
print(s)
# a    10
# b    20
# c    30
# d    40

# DataFrame: 二維（像 Excel 表）
df = pd.DataFrame({
    \"name\": [\"Elvis\", \"Bob\", \"Carol\"],
    \"age\": [35, 28, 42],
    \"city\": [\"台中\", \"台北\", \"高雄\"]
})
print(df)
```
"""),
        ("🔍 探索 DataFrame", """```python
print(df.head())       # 前 5 筆
print(df.tail(3))      # 末 3 筆
print(df.shape)        # (3, 3) — 3 筆 3 欄
print(df.dtypes)       # 各欄型別
print(df.columns)      # 欄位名
print(df.index)        # index
print(df.describe())   # 數值統計摘要
print(df.info())       # 結構 + 型別 + 非空數
```
"""),
        ("✏️ 練習題", """1. 從 dict 建立一個 DataFrame
2. 印出 head / tail / describe
"""),
    ]),

    ("chapter05_pandas/02-io.md", "第 5 章 · pandas", "5.2 讀寫資料", "30 分鐘", "資料分析", [
        ("🎯 學習目標", """- 讀寫 CSV / Excel / JSON
- 設定 index / parse_dates
- 處理編碼問題
"""),
        ("📥 讀檔", """```python
import pandas as pd

# CSV
df = pd.read_csv(\"data.csv\")
df = pd.read_csv(\"data.csv\", encoding=\"utf-8\")
df = pd.read_csv(\"data.csv\", index_col=\"id\")
df = pd.read_csv(\"data.csv\", parse_dates=[\"date\"])

# Excel（要裝 openpyxl）
df = pd.read_excel(\"data.xlsx\", sheet_name=\"Sheet1\")

# JSON
df = pd.read_json(\"data.json\")

# 從 SQL
# df = pd.read_sql(\"SELECT * FROM users\", conn)
```
"""),
        ("📤 寫檔", """```python
df.to_csv(\"out.csv\", index=False, encoding=\"utf-8\")
df.to_excel(\"out.xlsx\", index=False, sheet_name=\"結果\")
df.to_json(\"out.json\", orient=\"records\", force_ascii=False)
```
"""),
        ("❗ 常見錯誤", """1. **編碼錯**：中文檔要 `encoding=\"utf-8\"` 或 `big5`
2. **index 被寫進去**：用 `index=False`
3. **Excel 引擎**：要裝 `openpyxl`
"""),
        ("✏️ 練習題", """1. 讀 `taiwan_aqi_latest.csv` 進 pandas
2. 過濾出 AQI > 50 的測站，存成新的 CSV
"""),
    ]),

    ("chapter05_pandas/03-selection.md", "第 5 章 · pandas", "5.3 選取資料", "30 分鐘", "資料分析", [
        ("🎯 學習目標", """- 熟練 loc / iloc
- 條件過濾
- 多條件
"""),
        ("🔪 選取欄", """```python
df[\"name\"]              # 一欄（Series）
df[[\"name\", \"age\"]]     # 多欄（DataFrame）
```
"""),
        ("📍 loc vs iloc", """```python
# loc: 用 label
df.loc[0]                 # 第一列
df.loc[0:3]               # 0 到 3
df.loc[0, \"name\"]       # 0 列的 name
df.loc[df[\"age\"] > 30]  # 條件

# iloc: 用位置
df.iloc[0]                # 第一列
df.iloc[0:3]              # 0, 1, 2
df.iloc[0, 1]             # 0 列 1 欄
```
"""),
        ("🔍 條件過濾", """```python
# 單條件
adult = df[df[\"age\"] >= 18]

# 多條件（注意括號）
tcc = df[(df[\"city\"] == \"台中\") & (df[\"age\"] > 30)]

# isin
big_city = df[df[\"city\"].isin([\"台北\", \"台中\", \"高雄\"])]

# str.contains
df[df[\"name\"].str.contains(\"明\")]
```
"""),
        ("✏️ 練習題", """1. 過濾出 AQI > 70 的測站
2. 找出特定縣市的所有測站
3. 用 iloc 取前 5 列
"""),
    ]),

    ("chapter05_pandas/04-cleaning.md", "第 5 章 · pandas", "5.4 資料清理", "35 分鐘", "資料分析", [
        ("🎯 學習目標", """- 處理缺失值
- 處理重複
- 型別轉換
"""),
        ("🕳️ 缺失值", """```python
df.isna()           # True/False 矩陣
df.isna().sum()     # 各欄缺失值數量

df.dropna()         # 丟掉有缺失的列
df.dropna(subset=[\"age\"])  # 只看 age

df.fillna(0)        # 填 0
df[\"age\"].fillna(df[\"age\"].mean())  # 填平均
```
"""),
        ("🔁 重複值", """```python
df.duplicated()            # 布林 mask
df.drop_duplicates()       # 丟重複
df.drop_duplicates(subset=[\"name\"])  # 只看 name
```
"""),
        ("🔄 型別轉換", """```python
df[\"age\"].astype(int)
df[\"date\"].astype(\"datetime64[ns]\")
df[\"price\"].astype(float)
pd.to_numeric(df[\"x\"], errors=\"coerce\")  # 轉不了變 NaN
```
"""),
        ("✏️ 練習題", """1. 找 AQI 資料的缺失值
2. 用平均值填 PM2.5 缺失
3. 移除重複測站
"""),
    ]),

    ("chapter05_pandas/05-transform.md", "第 5 章 · pandas", "5.5 轉換", "25 分鐘", "資料分析", [
        ("🎯 學習目標", """- apply / map / replace
- 新增衍生欄位
"""),
        ("🔧 apply", """```python
# 對 Series
df[\"age\"].apply(lambda x: x * 2)

# 對 DataFrame
df.apply(lambda row: row[\"a\"] + row[\"b\"], axis=1)
```
"""),
        ("🗺️ map / replace", """```python
df[\"city\"].map({\"台北\": \"北\", \"台中\": \"中\", \"高雄\": \"南\"})
df[\"status\"].replace({\"good\": \"好\", \"bad\": \"差\"})
```
"""),
        ("✏️ 練習題", """1. 算每個測站 PM2.5 的四分位距
2. 新增「嚴重程度」欄：>100 嚴重, 50-100 中等, <50 良好
"""),
    ]),

    ("chapter05_pandas/06-groupby.md", "第 5 章 · pandas", "5.6 groupby + agg", "30 分鐘", "資料分析", [
        ("🎯 學習目標", """- Split-Apply-Combine 觀念
- groupby + agg
"""),
        ("🔄 groupby 基礎", """```python
# 算每縣市平均 AQI
df.groupby(\"county\")[\"aqi\"].mean()

# 多個聚合
df.groupby(\"county\").agg(
    avg_aqi=(\"aqi\", \"mean\"),
    max_aqi=(\"aqi\", \"max\"),
    count=(\"aqi\", \"count\")
)
```
"""),
        ("📊 多重 groupby", """```python
df.groupby([\"county\", \"status\"])[\"aqi\"].mean()
```
"""),
        ("💡 transform", """```python
# 把每組的 mean 加到每一列
df[\"county_avg\"] = df.groupby(\"county\")[\"aqi\"].transform(\"mean\")
```
"""),
        ("✏️ 練習題", """1. 算每縣市 AQI 中位數並排序
2. 找 AQI 最高的 3 個測站（每縣市）
3. 用 transform 算每測站的 z-score
"""),
    ]),

    ("chapter05_pandas/07-merge.md", "第 5 章 · pandas", "5.7 合併", "25 分鐘", "資料分析", [
        ("🎯 學習目標", """- merge / join / concat
- 各種 join 方式
"""),
        ("🔗 merge", """```python
# inner join（預設）
result = df1.merge(df2, on=\"id\")

# left join
result = df1.merge(df2, on=\"id\", how=\"left\")

# 不同 key 名
result = df1.merge(df2, left_on=\"user_id\", right_on=\"id\")
```
"""),
        ("📚 concat", """```python
# 垂直合併（疊行）
all_df = pd.concat([df1, df2, df3], ignore_index=True)

# 水平合併（加欄）
wide = pd.concat([df1, df2], axis=1)
```
"""),
        ("✏️ 練習題", """1. 把空汙跟實價登錄 merge（用縣市）
2. concat 三個季度的資料
"""),
    ]),

    ("chapter05_pandas/08-pivot.md", "第 5 章 · pandas", "5.8 樞紐分析表", "25 分鐘", "資料分析", [
        ("🎯 學習目標", """- pivot / pivot_table
- melt（寬轉長）
"""),
        ("🔄 pivot_table", """```python
# 縣市 × 狀態 的平均 AQI
pivot = df.pivot_table(
    values=\"aqi\",
    index=\"county\",
    columns=\"status\",
    aggfunc=\"mean\"
)
```
"""),
        ("↔️ melt", """```python
# 寬轉長（適合 ggplot / seaborn）
long = wide.melt(
    id_vars=\"date\",
    value_vars=[\"A\", \"B\", \"C\"],
    var_name=\"category\",
    value_name=\"value\"
)
```
"""),
        ("✏️ 練習題", """1. 做縣市 × 月份的 AQI pivot
2. melt 回長格式
"""),
    ]),

    ("chapter05_pandas/09-time-series.md", "第 5 章 · pandas", "5.9 時間序列", "30 分鐘", "資料分析", [
        ("🎯 學習目標", """- to_datetime
- resample / rolling
- 時區處理
"""),
        ("📅 時間處理", """```python
df[\"date\"] = pd.to_datetime(df[\"date\"])
df[\"year\"] = df[\"date\"].dt.year
df[\"month\"] = df[\"date\"].dt.month
df[\"weekday\"] = df[\"date\"].dt.day_name()
```
"""),
        ("📊 resample", """```python
df.set_index(\"date\", inplace=True)

# 每日 → 每月
monthly = df.resample(\"M\").mean()

# 每日 → 每季
quarterly = df.resample(\"Q\").sum()
```
"""),
        ("📈 rolling", """```python
df[\"rolling_7\"] = df[\"aqi\"].rolling(7).mean()
df[\"rolling_30\"] = df[\"aqi\"].rolling(30).mean()
```
"""),
        ("✏️ 練習題", """1. 把 AQI 資料轉成時間序列
2. 算 7 日 / 30 日移動平均
3. 按月 groupby 看趨勢
"""),
    ]),

    ("chapter05_pandas/10-perf.md", "第 5 章 · pandas", "5.10 效能優化", "20 分鐘", "資料分析", [
        ("🎯 學習目標", """- vectorization
- query / eval
- 避免 Python 迴圈
"""),
        ("⚡ 向量化", """```python
# 慢：用 apply
df[\"price_x2\"] = df[\"price\"].apply(lambda x: x * 2)

# 快：向量化
df[\"price_x2\"] = df[\"price\"] * 2
```
"""),
        ("🔍 query / eval", """```python
# query（可讀性高）
adults = df.query(\"age >= 18 and city == '台中'\")

# eval（算術表達式）
df.eval(\"total = price * quantity\", inplace=True)
```
"""),
        ("✏️ 練習題", """1. 用向量化算 AQI 跟 PM2.5 的比值
2. 用 query 過濾 AQI > 100 的測站
"""),
    ]),

    ("chapter05_pandas/project.md", "第 5 章 · pandas", "小專案: 銷售資料分析", "90 分鐘", "資料分析", [
        ("🎯 專案目標", """用模擬的 1 萬筆電商銷售資料做完整分析：

- 讀 CSV → 清理 → groupby → 視覺化
"""),
        ("📥 模擬資料", """```python
import pandas as pd
import numpy as np

np.random.seed(42)
n = 10000
df = pd.DataFrame({
    \"order_id\": range(n),
    \"date\": pd.date_range(\"2025-01-01\", periods=n, freq=\"30min\"),
    \"product\": np.random.choice([\"筆電\", \"手機\", \"耳機\", \"平板\"], n),
    \"price\": np.random.randint(500, 50000, n),
    \"quantity\": np.random.randint(1, 5, n),
})
df[\"revenue\"] = df[\"price\"] * df[\"quantity\"]
df.to_csv(\"sales.csv\", index=False, encoding=\"utf-8\")
```
"""),
        ("📊 分析問題", """1. 各產品總營收？
2. 月營收趨勢？
3. 哪天賣最好？
4. 平均客單價？
5. 高單價產品分布？
"""),
        ("💻 完整分析", """```python
df = pd.read_csv(\"sales.csv\", parse_dates=[\"date\"])

# 1. 各產品營收
print(df.groupby(\"product\")[\"revenue\"].sum().sort_values(ascending=False))

# 2. 月營收
df[\"month\"] = df[\"date\"].dt.to_period(\"M\")
print(df.groupby(\"month\")[\"revenue\"].sum())

# 3. 哪一天賣最好
best_day = df.groupby(df[\"date\"].dt.date)[\"revenue\"].sum().idxmax()
print(f\"Best day: {best_day}\")

# 4. 平均客單價
print(f\"客單價平均: NT${df.groupby('order_id')['revenue'].sum().mean():.0f}\")

# 5. 高單價產品（> 30000）
print(df[df[\"price\"] > 30000][\"product\"].value_counts())
```
"""),
        ("📈 視覺化", """```python
import matplotlib.pyplot as plt

# 月營收趨勢
monthly = df.groupby(\"month\")[\"revenue\"].sum()
monthly.plot(kind=\"line\", marker=\"o\", figsize=(10, 5))
plt.title(\"月營收趨勢\")
plt.ylabel(\"NT$\")
plt.grid(True, alpha=0.3)
plt.show()

# 產品圓餅圖
df.groupby(\"product\")[\"revenue\"].sum().plot.pie(autopct=\"%1.1f%%\")
plt.title(\"產品營收占比\")
plt.show()
```
"""),
        ("🚀 挑戰版", """1. RFM 分析
2. 產品交叉銷售分析
3. 預測下月營收
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
