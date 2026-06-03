---
title: "9.3 部署與分享"
---

<div class="lesson-header">
  <span class="chapter-tag">第 9 章 · 進階導讀</span>
  <h1>9.3 部署與分享</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- Streamlit / Flask
- Docker
- 雲端部署


## 🚀 Streamlit

```python
import streamlit as st
st.title("我的第一個 App")
st.line_chart([1, 2, 3, 4])
```


## 🌐 Flask

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```


## 🐳 Docker

```dockerfile
FROM python:3.11
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```


