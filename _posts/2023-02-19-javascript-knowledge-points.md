---
title: JavaScript knowledge points
excerpt: "The Document will list some JavaScript concepts."
---

# JavaScript Guidebook

## false values:

The following values are thought false

- The following values are thought falsefalse
- null 
- undefined
- 0
- '' (empty string)
- NaN

## Date

Get current time:

```js
let timestamp=new Date().getTime()；
// 获取的数字为 1658201369045
// 应该从后往前看 1658201369.045s
```

Date 所能解析的时间戳

1. new Date("month dd,yyyy hh:mm:ss");
2. new Date("month dd,yyyy");
3. new Date("yyyy/MM/dd hh:mm:ss");
4. new Date("yyyy/MM/dd");
5. new Date(yyyy,mth,dd,hh,mm,ss);
6. new Date(yyyy,mth,dd);
7. new Date(ms);

## Gabage Collection

内存分配 -> 内存使用 -> 内存回收

全局变量一般不会被回收（关闭页面会被回收）

局部变量不用时被回收

Module

Node引入了JS模块化的概念

现在已经支持ECMAScript的引入模

```json
{
  ...
	"type": "module",
  ...
}
```

目前模块化的不同方案：

- CJS Common JavaScript
- AMD Asynchronous Module Definition
- UMD Universal Module Definition
- ESM es6

## Immediately Invoked Function Expression

IIFE 立即执行函数表达式，也称作包围函数。

```js
(function() { /* code */ })();
```

作用：可以用它创建命名空间，只要把自己所有的代码都写在这个特殊的函数包装内，那么外部就不能访问，除非你允许(变量前加上window，这样该函数或变量就成为全局)。各JavaScript库的代码也基本是这种组织形式。

```js
// 如果你不在意返回值，或者不怕难以阅读
// 你甚至可以在function前面加一元操作符号

!function () { /* code */ } ();
~function () { /* code */ } ();
-function () { /* code */ } ();
+function () { /* code */ } ();
```

都是跟`(function(){})();`这个函数是一个意思，都是告诉浏览器自动运行这个匿名函数的，因为!+()这些符号的运算符是最高的，所以会先运行它们后面的函数。