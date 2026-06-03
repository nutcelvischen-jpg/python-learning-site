# Python 學堂 · 從零到數據分析 🐍

> 一個完整的 Python 教學網站，從零基礎到數據分析實戰。
> 使用 [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) + 自訂設計系統建置。

🌐 **Live Site**: https://nutcelvischen-jpg.github.io/python-learning-site/

## ✨ 特色

- 🎨 **Open Design 風格** — 乾淨、有創意感的設計系統
- 🐍 **60+ 章節內容** — 涵蓋基礎語法到數據分析
- 🎯 **4+ 個實戰專案** — 含獨家「空汙 × 房價」案例
- 🇹🇼 **台灣在地化** — 用台灣政府開放資料
- 📊 **真實 Python 圖表** — 13 張由 Python 跑出的高品質圖
- 🤖 **整合 twinkle-hub MCP** — 真實 AQI + 實價登錄資料
- 📚 **完整 IMRaD 結構** — 適合教學 / 自學

## 📚 章節架構

| 章 | 主題 | 小節 |
|---|---|---|
| 0 | 環境準備 | 5 |
| 1 | 基礎語法 | 10 + 小專案 |
| 2 | 進階基礎 | 8 + 小專案 |
| 3 | 環境管理 | 5 |
| 4 | NumPy | 6 |
| 5 | pandas | 10 + 小專案 |
| 6 | 視覺化 | 8 |
| 7 | 統計基礎 | 6 |
| 8 | 實戰專案 | 4 + 🆕 空汙房價 |
| 9 | 進階導讀 | 3 |
| 附錄 | - | 5 |

## 🛠️ 技術棧

- **內容格式**: Markdown (MyST 擴充)
- **建置工具**: MkDocs + Material 主題
- **部署**: GitHub Pages + GitHub Actions
- **Python**: 3.11+
- **資料來源**:
  - [環境部 AQI 監測](https://airtw.moenv.gov.tw/) (透過 twinkle-hub MCP)
  - [內政部實價登錄](https://plvr.land.moi.gov.tw/) (透過 twinkle-hub MCP)
  - [twinkle-hub 開放資料 MCP](https://hub.twinkleai.tw)

## 🚀 本地開發

```bash
# 1. Clone
git clone https://github.com/nutcelvischen-jpg/python-learning-site.git
cd python-learning-site

# 2. 安裝依賴
python3 -m venv .venv
source .venv/bin/activate
pip install -r scripts/requirements-build.txt

# 3. 重新生成所有圖表
python scripts/fetch_real_data.py
python scripts/render_charts.py

# 4. 本地預覽
mkdocs serve
# 開 http://localhost:8000
```

## 📦 部署

每當 push 到 `main` branch，GitHub Actions 自動：

1. 安裝 Python 依賴
2. 跑 `render_charts.py` 重新生成所有圖
3. 用 MkDocs build 靜態網站
4. Deploy 到 GitHub Pages

## 🎨 設計系統

本站設計啟發自 [Open Design 0.9.0](https://github.com/nexu-io/open-design)：

- **主色**: Python 藍 `#3776AB`
- **亮點**: 創意橘 `#FF6B35`
- **背景**: 純白 `#FFFFFF` / 深色 `#0F172A`
- **字型**: Noto Sans TC（中文）+ JetBrains Mono（code）
- **特色**: 漸層 hero、卡片化設計、admonition 客製

## 📜 授權

- 內容: [MIT License](LICENSE)
- 程式碼範例: MIT
- 圖表: MIT
- 資料: 政府資料開放授權條款第 1 版

## 🤝 致謝

- 設計靈感：[Open Design](https://github.com/nexu-io/open-design)
- 內容來源：Python 官方文件 + K-Dense-AI/scientific-agent-skills
- 資料來源：環境部 + 內政部地政司（透過 twinkle-hub）
- 建置工具：[MkDocs Material](https://squidfunk.github.io/mkdocs-material/)

---

**作者**: Elvis Chen（赫哥） · 國立臺中科技大學
