---
title: Introduce Lambda
date: 2023-07-21
---

# Introduce Lambda

很多开发语言会提到lambda表达式，本质上是个具有特别格式的匿名函数。

意义在于函数式编程（函数作为一等公民）。

## Lambda 表达式起源

源自 $\lambda$演算 （Lambda calculus），由数学家阿隆佐·邱奇（Alonzo Church）在20世纪30年代首次发表。它被认为是计算机科学的理论基础之一，并对函数式编程语言的设计产生了深远影响。

该思想最早被应用到LISP语言，因此也产生了函数的概念。LISP是在1958年由约翰·麦卡锡（John McCarthy）开发。

### lambda 演算介绍

lambda演算用于研究函数抽象、递归和计算过程的形式化工具。

由以下三个基本元素组成：

1. 变量（Variables）：表示一个标识符，如 x、y、z 等。
2. 抽象（Abstraction）：使用$\lambda$符号表示，后跟一个变量和一个点，然后是一个表达式。它表示一个匿名函数的定义，例如 $\lambda x.x$ 表示一个接受一个参数 x 并返回 x 的函数。
3. 应用（Application）：将一个表达式应用到另一个表达式上，用空格分隔。例如 (λx.x) y 表示将函数 λx.x 应用到参数 y 上。

Lambda演算可以使用这些基本形式来表示和计算复杂的函数和表达式。它具有很强的表达能力，可以表示任何可计算的函数，并且通过一系列规约操作可以进行计算。

### lambda 演算应用

Lambda演算表达式：$(\lambda x.\lambda y.(x + y))$。$x$ 和 $y$ 分别表示函数的两个参数，$(x + y)$ 表示它们的和。

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

