---
title: "时间复杂度"
excerpt: "评判算法的优劣，时间复杂度是一个重要指标。"
---

# 时间复杂度

## 类型

- O(1)：常数时间复杂度
- O(log n)：对数时间复杂度
- O(n)：线性时间复杂度
- O(n log n)：线性对数时间复杂度
- O(n^2)：平方时间复杂度
- O(n^3)：立方时间复杂度
- O(2^n)：指数时间复杂度
- O(n!)：阶乘时间复杂度

## 排序

下述为我使用 Python Matplotlib 创建线图：

![time complexity line plot](https://raw.githubusercontent.com/fox20431/pic-hub/master/img/202302261628368.png)

当数据量大的时候，我们可以得出结论：

O(log n) < O(N) < O(nlog n) < O(n^2) < O(n^k) < O(2^n) < O(n!)