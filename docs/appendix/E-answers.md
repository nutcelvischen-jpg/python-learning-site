---
title: "E. 練習題答案"
---

<div class="lesson-header">
  <span class="chapter-tag">附錄 E</span>
  <h1>E. 練習題答案</h1>
  <div class="meta">
    <span>⏱️ 30 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 參考</span>
  </div>
</div>

## ⚠️ 使用說明

!!! warning "請先自己做再看"

    這裡的答案是給「卡關時參考」用的。 強烈建議**先自己寫 30 分鐘再來看**。

    練習題的價值在於**思考過程**，不是「答案長怎樣」。


## 📝 第 0 章 答案

#### 練習 1：自我介紹
```python
name = input("你叫什麼名字？ ")
age = input("你幾歲？ ")
hobby = input("興趣？ ")
print(f"我是 {name}，{age} 歲，興趣是 {hobby}")
```

#### 練習 2：計算機
```python
a = float(input("第一個數: "))
b = float(input("第二個數: "))
print(f"和: {a+b}")
print(f"差: {a-b}")
print(f"積: {a*b}")
print(f"商: {a/b}" if b != 0 else "除以 0")
```

#### 練習 3：溫度轉換
```python
c = float(input("攝氏: "))
f = c * 9/5 + 32
print(f"華氏: {f}")
```

#### 練習 4：BMI
```python
kg = float(input("體重 kg: "))
cm = float(input("身高 cm: "))
bmi = kg / (cm/100) ** 2
print(f"BMI: {bmi:.1f}")
```

#### 練習 5：Debug
```python
name = input("你叫什麼名字？")   # 補引號
age = int(input("你幾歲？ "))     # 補右括號
print(f"你是 {name}, {age} 歲")   # 改 Age → age
```


## 📚 各章答案

完整答案持續更新中。 各章練習題的標準答案放在 [GitHub Repo](https://github.com/nutcelvischen-jpg/python-learning-site/tree/main/answers) 的 `answers/` 目錄。

建議從 **pull request** 提交你的解答，跟社群互動學習！


## 💡 提交流程

1. Fork 這個 repo
2. 寫你的解答到 `answers/chapterXX/`
3. 開 Pull Request
4. 社群 review + 討論


