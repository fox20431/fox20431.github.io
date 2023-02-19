# 闭包

## 概念

闭包的英文是 closure，翻译成闭包我觉得挺“信、雅、达”的。英文的意思大概是：a function which **closes over** the **environment(scope)** in which it was defined。

所以闭包就是：在一个封**闭**的词法作用域中，将某些自由变量**包**在定义它的函数中。

第一，闭包是一个函数，而且存在于另一个函数当中

第二，闭包可以访问到父级函数的变量，且该变量不会销毁

## 闭包与函数的区别

摘录[Apple Developer Forums](https://developer.apple.com/forums/thread/43606)

> Roughly, a closure is a block of code that may capture variable values from its surrounding scope.
>
> Roughly, a function is a statically defined block of code that may use variable values from its surrounding scope.

摘录[维基百科](https://zh.wikipedia.org/wiki/闭包_(计算机科学))

> 闭包跟函数最大的不同在于，当捕捉闭包的时候，它的自由变量会在捕捉时被确定，这样即便脱离了捕捉时的上下文，它也能照常运行。捕捉时对于值的处理可以是值拷贝，也可以是名称引用，这通常由语言设计者决定，也可能由用户自行指定（如C++）。

闭包是`capture`环境变量，函数是`use`环境变量。`capture`会使得环境变量无法释放，`use`则使得环境变量可以释放。

当你需要环境变量一直存在内存中不被释放时，则需要闭包。

## 应用

普通函数

```js
function add() {
  var x = 1;
  console.log(++x);
}

add(); //执行输出2

add(); //执行还是输出2
```

闭包函数


```js
function add() {
  var x = 1;
  return function() {
    console.log(++x);
  };
}
var num = add();

num(); //输出2

num(); //输出3

num(); //输出4
```

## 结论

个人见解：由于闭包函数为其他函数的返回值，所以形成一种封闭结构，导致其包含的变量无法释放，所以称为闭包。