---
title: "1.7 流程控制"
---

<div class="lesson-header">
  <span class="chapter-tag">第 1 章 · 基礎語法</span>
  <h1>1.7 流程控制</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 入門</span>
  </div>
</div>

## 🎯 學習目標

- 學會 `if / elif / else` 條件判斷
- 理解 Python 的縮排規則（4 空格）
- 熟練巢狀條件
- 學會三元運算式


## 🔀 基礎 if

```python
age = 18

if age >= 18:
    print("你已成年")
else:
    print("你未成年")
```


## 🎯 if / elif / else

```python
score = 85

if score >= 90:
    print("A+ 優等")
elif score >= 80:
    print("B+ 良好")
elif score >= 70:
    print("C+ 中等")
elif score >= 60:
    print("D+ 及格")
else:
    print("F 不及格")
```


## 🔗 複合條件

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("可以開車")
elif age >= 18 and not has_license:
    print("需要先去考駕照")
else:
    print("年紀還沒到")
```


## ⚡ 三元運算式

```python
age = 20
status = "成年" if age >= 18 else "未成年"
print(status)    # 成年
```


## 🪆 巢狀 if

```python
score = 85
is_makeup = True

if score >= 60:
    if is_makeup:
        print("補考通過")
    else:
        print("正常通過")
else:
    print("未通過")
```


## ❗ 常見錯誤

1. **`==` 跟 `=` 搞混**
2. **忘記冒號 `:`**
3. **縮排不一致**：同一個 block 要用一樣的縮排（建議 4 空格）
4. **過度巢狀**：超過 3 層考慮用函式或早 return


## ✏️ 練習題

1. 寫一個 BMI 分類：< 18.5 過輕, 18.5-24 正常, 24-27 過重, > 27 肥胖
2. 判斷閏年：能被 4 整除且（不能被 100 整除 或 能被 400 整除）
3. 寫一個三元運算式判斷奇偶
4. 巢狀判斷：根據年齡 + 是否會員給不同折扣


