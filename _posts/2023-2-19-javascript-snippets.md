---
title: "JavaScript Snippets"
excerpt: "The Document will list the some JavaScript concepts."
---

# JavaScript Guidebook

The documentation will show some key knowledge points.

## The False Value

- false
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

## Module

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