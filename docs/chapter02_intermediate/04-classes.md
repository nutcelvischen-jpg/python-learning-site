---
title: "2.4 類別與物件"
---

<div class="lesson-header">
  <span class="chapter-tag">第 2 章 · 進階基礎</span>
  <h1>2.4 類別與物件</h1>
  <div class="meta">
    <span>⏱️ 40 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 進階</span>
  </div>
</div>

## 🎯 學習目標

- 學會 class 語法
- 理解 `__init__` / self
- 認識繼承
- 知道 dunder methods


## 🏗️ 基本 class

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name}: 汪汪！"

    def __str__(self):
        return f"{self.name} ({self.breed})"

my_dog = Dog("小黑", "柴犬")
print(my_dog)             # 小黑 (柴犬)
print(my_dog.bark())      # 小黑: 汪汪！
```


## 🧬 繼承

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..." 

class Cat(Animal):
    def speak(self):
        return f"{self.name}: 喵喵！"

cat = Cat("小花")
print(cat.speak())    # 小花: 喵喵！
```


## ❗ 常見錯誤

1. **忘記 self**：方法第一個參數一定要 self
2. **過度設計**：簡單東西用 class 是 over-engineering


## ✏️ 練習題

1. 寫一個 `Student` class 有 name / scores
2. 加一個 `average()` 方法算平均分
3. 寫一個 `GraduateStudent` 繼承 `Student`


