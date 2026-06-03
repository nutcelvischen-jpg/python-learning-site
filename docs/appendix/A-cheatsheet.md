---
title: "A. 速查表"
---

<div class="lesson-header">
  <span class="chapter-tag">附錄 A</span>
  <h1>A. 速查表</h1>
  <div class="meta">
    <span>⏱️ 5 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 速查</span>
  </div>
</div>

## 📚 內建函式

```python
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


## 📦 串列方法

```python
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


## 📖 字典方法

```python
d[k] = v             # 設
d.get(k, default)    # 取
d.keys() / values() / items()
d.update(other)
d.pop(k)
d.setdefault(k, v)
```


## 🐼 pandas 速查

```python
df = pd.read_csv("f.csv")
df.head() / tail() / describe() / info()
df["col"] / df[["c1", "c2"]]
df.loc[i] / df.iloc[i]
df.query("cond")
df.groupby("col").agg(...)
df.merge(other, on="key")
df.pivot_table(...)
df.fillna(0) / dropna()
df.apply(fn)
```


