---
title: Kotlin Lambda
date: 2023-07-21
---

# Kotlin Lambda 表达式

学习 Kotlin Lambda 是必要的，首先它常被用作KTS（gradle）作为脚本。

同时他也是面向对象语言通往高阶函数（将函数用作参数或返回值的函数）的方式。

Kotlin Lambda 表达式的形式：

```kotlin
{ 参数列表 -> 函数体 }
```

相比Kotlin的function：

```kotlin
fun foo (参数列表) {
    函数体
} 
```

本质上是个匿名函数。

## Lambda 表达式 起源

源自 $\lambda$演算 （Lambda calculus）。

### lambda 演算介绍

lambda演算用于研究函数抽象、递归和计算过程的形式化工具。

由以下三个基本元素组成：

1. 变量（Variables）：用来表示参数和函数的输入。
2. 抽象（Abstraction）：用λ（lambda）符号表示，用于创建函数。例如，λx.x 表示一个以变量 x 为参数并返回 x 的函数。
3. 应用（Application）：用空格表示，表示函数调用。例如，(λx.x) y 表示将参数 y 应用于函数 λx.x。

Lambda演算的基本原则是通过抽象和应用来定义和操作函数。在Lambda演算中，所有的计算都通过替换（substitution）进行。例如，应用表达式 (λx.x) y 中的 y 将替换抽象表达式 λx.x 中的 x，得到结果 y。

### lambda 演算实际操作

题目：在Lambda演算中定义一个函数，该函数接受两个参数并返回它们的和。

解决： 在Lambda演算中，我们可以使用λ（lambda）符号来表示函数抽象。函数抽象的一般形式为：λ参数.函数体。参数是函数的形式参数，函数体描述了函数的计算过程。

为了定义一个接受两个参数并返回它们的和的函数，我们可以使用以下Lambda演算表达式：

(λx.λy.(x + y))

其中，x和y分别表示函数的两个参数，(x + y)表示它们的和。

现在，让我们通过Lambda演算的替换规则来计算这个函数的应用：

(λx.λy.(x + y)) 2 3

首先，将x替换为2：

(λy.(2 + y)) 3

然后，将y替换为3：

2 + 3

最终结果为：

5

因此，定义的Lambda演算函数成功地将输入的两个参数相加并返回它们的和。

### lambda 演算与编程语言

比如计算平方的的函数 square 在 lisp 中可以表示如下的 lambda 表达式

```lisp
(lambda (x) (* x x))
```

## Kotlin Lambda 表示语法糖

### 为什么可以作为 KTS

```kotlin
// 高阶函数
fun foo(Any -> Any): Any
// 参数只有一个lambda表达式，调用可以写作
foo {
    // blah blah
    return any
}
```

