---
title: "2.3 模組與套件"
---

<div class="lesson-header">
  <span class="chapter-tag">第 2 章 · 進階基礎</span>
  <h1>2.3 模組與套件</h1>
  <div class="meta">
    <span>⏱️ 25 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 學會 `import` 各種模組
- 理解 `from X import Y`
- 自己寫一個模組
- 知道什麼是 `__name__ == "__main__"`


## 📥 import 模組

```python
import math
print(math.sqrt(16))      # 4.0

from math import pi, sin
print(pi)                  # 3.14159...
print(sin(0))              # 0.0

import numpy as np         # 別名
arr = np.array([1, 2, 3])
```


## 📝 自訂模組

建立 `mymath.py`：

```python
# mymath.py
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

另一個檔案使用：

```python
import mymath
print(mymath.add(3, 4))       # 7
print(mymath.PI)              # 3.14159
```


## 🚪 `__name__` 魔術

```python
# myscript.py
def main():
    print("這是主程式")

if __name__ == "__main__":
    main()                # 只有直接執行才跑
```

`import myscript` 時不會跑 main()。


## ❗ 常見錯誤

1. **circular import**：A 引入 B，B 又引入 A
2. **路徑錯**：模組不在 PYTHONPATH


## ✏️ 練習題

1. 寫一個 `geometry.py` 模組含 circle_area / rectangle_area
2. 從另一個檔 import 它來用
3. 用 `if __name__ == "__main__"` 寫個測試


