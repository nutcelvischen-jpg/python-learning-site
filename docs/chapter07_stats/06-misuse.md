---
title: "7.6 統計誤用警示"
---

<div class="lesson-header">
  <span class="chapter-tag">第 7 章 · 統計基礎</span>
  <h1>7.6 統計誤用警示</h1>
  <div class="meta">
    <span>⏱️ 20 分鐘</span>
    <span>📖 互動式</span>
    <span>🎯 統計</span>
  </div>
</div>

## 🎯 學習目標

- p-hacking
- 辛普森悖論
- 相關 vs 因果


## ⚠️ p-hacking

一直做統計檢定直到 p < 0.05，**一定會找到顯著結果**。 這就是 p-hacking。

!!! warning "修正"

    1. 先註冊研究設計
    2. 多重比較用 Bonferroni 修正
    3. 報告效應量不只是 p-value


## 🌀 辛普森悖論

分組看 vs 整體看會得到**相反**的結論。

!!! example "範例"

    治療 A 對男性有效、對女性也有效。 但把男女加總後，「A 反而比 B 差」！

    原因：**分組比例不同**。


## 🔗 相關 ≠ 因果

X 跟 Y 相關不代表 X 引起 Y。

- 可能是巧合
- 可能 Z 引起 X 跟 Y
- 可能反向因果


## ✏️ 練習題

1. 找一個 p-hacking 的真實案例
2. 解釋一個辛普森悖論例子


