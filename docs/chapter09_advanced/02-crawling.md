---
title: "9.2 進階爬蟲"
---

<div class="lesson-header">
  <span class="chapter-tag">第 9 章 · 進階導讀</span>
  <h1>9.2 進階爬蟲</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- requests / BeautifulSoup
- 處理動態網頁
- 反爬蟲對策


## 🌐 requests

```python
import requests

r = requests.get("https://example.com")
print(r.status_code)
print(r.text)
```


## 🥣 BeautifulSoup

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, "html.parser")
titles = soup.find_all("h2")
```


## 🎭 Selenium（動態）

```python
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://example.com")
```


## ⚠️ 注意事項

- 尊重 robots.txt
- 加 delay
- 不要商業濫用


