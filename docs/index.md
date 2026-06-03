---
hide:
  - navigation
  - toc
---

<div class="hero">
  <h1>Python 學堂</h1>
  <p class="lead">從零基礎到數據分析，60+ 章節、4 個完整實戰專案。 用乾淨有創意的方式，學會 Python。</p>
  <div class="badges">
    <span class="badge python">🐍 Python 3.11+</span>
    <span class="badge orange">⚡ 60+ 章節</span>
    <span class="badge orange">🎯 4 個實戰</span>
    <span class="badge python">📊 pandas / NumPy</span>
    <span class="badge orange">🇹🇼 台灣在地化</span>
    <span class="badge python">🆓 永久免費</span>
  </div>
</div>

<div class="stats">
  <div class="stat"><span class="num">71</span><span class="label">內容檔案</span></div>
  <div class="stat"><span class="num">9</span><span class="label">主題章節</span></div>
  <div class="stat"><span class="num">4+</span><span class="label">實戰專案</span></div>
  <div class="stat"><span class="num">5</span><span class="label">附錄速查</span></div>
</div>

## 🎯 為什麼選這堂課？

這不是另一份「Python 入門教學」。**Python 學堂** 是為**完全沒寫過程式的學習者**設計的完整路徑，目標是「從零到能自己用 Python 分析真實世界的資料」。

<div class="cards">
  <a class="card" href="intro/">
    <span class="icon">🚀</span>
    <p class="title">零基礎友善</p>
    <p class="desc">從「Python 是什麼」開始，每一步都有完整解釋與可執行的範例。</p>
  </a>
  <a class="card" href="chapter05_pandas/01-intro/">
    <span class="icon">📊</span>
    <p class="title">真實資料驅動</p>
    <p class="desc">使用台灣政府公開資料（空污、實價登錄、Threads）做實戰，學會立刻能用。</p>
  </a>
  <a class="card" href="chapter07_stats/06-misuse/">
    <span class="icon">🧠</span>
    <p class="title">科學素養導向</p>
    <p class="desc">統計章節附「常見誤用警示」，訓練你看懂 p-hacking、辛普森悖論。</p>
  </a>
  <a class="card" href="chapter0X_setup/02-install/">
    <span class="icon">🛠️</span>
    <p class="title">環境最佳實踐</p>
    <p class="desc">從 venv 到 poetry，教你像專業工程師一樣管理 Python 環境。</p>
  </a>
  <a class="card" href="chapter08_projects_extra/05-air-vs-house/">
    <span class="icon">🏠</span>
    <p class="title">空汙 × 房價實戰</p>
    <p class="desc">獨家章節：用 twinkle-hub 整合環保署 AQI 與實價登錄，做完整分析。</p>
  </a>
  <a class="card" href="appendix/C-resources/">
    <span class="icon">📚</span>
    <p class="title">完整學習路徑</p>
    <p class="desc">9 章主軸 + 5 個附錄 + 100+ 練習題 + 30+ 程式碼範例。</p>
  </a>
</div>

## 🗺️ 學習路徑圖

```mermaid
graph LR
  A[0. 環境準備] --> B[1. 基礎語法]
  B --> C[2. 進階基礎]
  C --> D[4. NumPy]
  C --> E[5. pandas]
  D --> E
  E --> F[6. 視覺化]
  F --> G[7. 統計基礎]
  G --> H[8. 實戰專案]
  C --> H3[3. 環境管理]
  H3 --> H
  H --> I[9. 進階導讀]
  H --> J[空汙×房價 實戰]

  style A fill:#3776AB,color:#fff
  style B fill:#3776AB,color:#fff
  style C fill:#3776AB,color:#fff
  style D fill:#FF6B35,color:#fff
  style E fill:#FF6B35,color:#fff
  style F fill:#FF6B35,color:#fff
  style G fill:#FF6B35,color:#fff
  style H fill:#FFD43B,color:#0F172A
  style J fill:#FFD43B,color:#0F172A
  style I fill:#94A3B8,color:#fff
```

## 📖 章節總覽

| 章 | 主題 | 小節數 | 重點 |
|---|---|---|---|
| 0 | 環境準備 | 5 | 安裝、VS Code、第一支程式 |
| 1 | 基礎語法 | 10 | 變數、字串、list、dict、流程、函式 |
| 2 | 進階基礎 | 8 | 檔案、例外、模組、類別 |
| 3 | 環境管理 | 5 | venv / conda / poetry（專業工程師必備） |
| 4 | NumPy | 6 | ndarray、broadcasting、統計 |
| 5 | pandas | 10 | 讀寫、清洗、groupby、時間序列 |
| 6 | 視覺化 | 8 | matplotlib + seaborn + plotly |
| 7 | 統計基礎 | 6 | 檢定、迴歸、避免誤用 |
| 8 | 實戰專案 | 4 | 空氣品質 / 銷售 / Threads / 環境經濟 |
| **8.5** | **空汙 × 房價** | **1** | **🆕 twinkle-hub 整合實戰** |
| 9 | 進階導讀 | 3 | ML / 爬蟲 / 部署 |
| 附錄 | - | 5 | 速查 / FAQ / 資源 / 術語 / 答案 |

## 🚀 立即開始

<div class="cards">
  <a class="card" href="chapter0X_setup/01-why-python/">
    <span class="icon">📘</span>
    <p class="title">完全新手？</p>
    <p class="desc">從「為什麼學 Python」開始 →</p>
  </a>
  <a class="card" href="chapter01_basics/01-variables-types/">
    <span class="icon">⚡</span>
    <p class="title">有基礎想複習？</p>
    <p class="desc">直接進入第 1 章基礎語法 →</p>
  </a>
  <a class="card" href="chapter05_pandas/01-intro/">
    <span class="icon">🐼</span>
    <p class="title">想直接學資料分析？</p>
    <p class="desc">跳到第 5 章 pandas 開始 →</p>
  </a>
  <a class="card" href="chapter08_projects_extra/05-air-vs-house/">
    <span class="icon">🏠</span>
    <p class="title">想看實戰案例？</p>
    <p class="desc">空汙 × 房價實戰專案 →</p>
  </a>
</div>

---

**本站使用 [Open Design 0.9.0](https://github.com/nexu-io/open-design) 啟發的設計風格 · 本站內容採用 MIT 授權 · 程式碼範例皆可自由使用**
