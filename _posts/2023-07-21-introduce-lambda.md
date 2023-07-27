---
title: Introduce Lambda
date: 2023-07-21
---

# Introduce Lambda

很多开发语言会提到lambda表达式，本质上是个具有特别格式的匿名函数。

意义在于函数式编程（函数作为一等公民）。

## Lambda 表达式 起源

源自 $\lambda$演算 （Lambda calculus），由数学家阿隆佐·邱奇在20世纪30年代首次发表。

*图灵机（Turing Machine）由英国数学家艾伦·图灵在1936年提出的理论模型。*

*世界上第一台电子计算机 - ENIAC（Electronic Numerical Integrator and Computer）由美国的约翰·普雷斯班（John W. Mauchly）和约翰·艾克特（J. Presper Eckert）等人于1945年建造的。*

该思想最早被应用到LISP语言，因此也产生了函数的概念。LISP是由约翰·麦卡锡（John McCarthy）在1958年开发的。

### lambda 演算介绍

lambda演算用于研究函数抽象、递归和计算过程的形式化工具。

由以下三个基本元素组成：

1. 变量（Variables）：用来表示参数和函数的输入。
2. 抽象（Abstraction）：用 $\lambda$（lambda）符号表示，用于创建函数。例如，$\lambda x.x$ 表示一个以变量 $x$ 为参数并返回 $x$ 的函数。
3. 应用（Application）：用空格表示，表示函数调用。例如，(λx.x) y 表示将参数 y 应用于函数 λx.x。

Lambda演算的基本原则是通过抽象和应用来定义和操作函数。在Lambda演算中，所有的计算都通过替换（substitution）进行。例如，应用表达式 (λx.x) y 中的 y 将替换抽象表达式 λx.x 中的 x，得到结果 y。

### lambda 演算应用

Lambda演算表达式： $(\lambda x.\lambda y.(x + y))$。$x$ 和 $y$ 分别表示函数的两个参数，$(x + y)$ 表示它们的和。

通过Lambda演算的替换规则来计算这个函数的应用：
$$
(\lambda x.\lambda y.(x + y))\:2\:3
$$
首先，将 $x$ 替换为 $2$ ：

$$
(\lambda y.(2 + y))\:3
$$
然后，将 $y$ 替换为 $3$：

$$
2 + 3 = 5
$$

### lambda 演算与编程语言

**LISP**

可以在 Linux 环境下通过 `sudo apt install sbcl sbcl-doc sbcl-source slime` ，执行 `sbcl` 进入到交互界面。

```lisp
; normal function，受到lambda表达式的“抽象”的影响
(defun function-name (parameters...)
  body)

; lambda，计算平方
(lambda (x) (* x x))

; assign
(setq add (lambda (x y)
            (+ x y)))
```

**Kotlin**

现代化编程语言：

```kotlin
// normal function
fun add(x: Int, y: Int): Int {
    return x + y
}

// lambda
{ x: Int, y: Int -> x + y }
```

