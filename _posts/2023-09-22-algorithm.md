---
title: algorithm
date: 2023-09-22
---

# 算法

 	

## 算法简介

### 起源

[Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace)曾受委托将[Charles Babbage](https://en.wikipedia.org/wiki/Charles_Babbage)的论文翻译成英文，她在自己的翻译批注中描述了一种用于分析引擎计算伯努利数的算法。

其中她在批注中这样写到：

> [The Analytical Engine] might act upon other things besides *number*, were objects found whose mutual fundamental relations could be expressed by those of the abstract science of operations, and which should be also susceptible of adaptations to the action of the operating notation and mechanism of the engine...

这个便是对算法的最初的描述。

### 常见算法及用途

我们在后面接触到很多算法，比如：

- 可以用来计算两点间最短路径的**图算法**；
- 可以解决资源分配、生产调度问题的**动态规划算法**；
- 可以用来编写推荐系统的**K-最近邻算法**。

### 算法优劣

评价算法的优劣一般会从**时间复杂度**和**空间复杂度**判断。

时间复杂度和空间复杂度一般可以表示为 $O(n)$ 、$O(n^2)$等，这里的 $O$ 表示最糟糕情况，在坐标轴中表现为上界。

关于复杂度表示方法这里做个汇总：

- $O$表示上界（实际复杂度<=）
- $\Omega$表示下界（实际复杂度>=）
- $\Theta$表示确界（实际复杂度=）
- $o$松上界（实际复杂度<）
- $\omega$松下界（实际复杂度>）