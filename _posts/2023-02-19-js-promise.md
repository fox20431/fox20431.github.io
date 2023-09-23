---
title: JavaScript Promise
date: 2023-02-19
---



# JavaScript Promise

从两年前我得知Promise到如今，我终于体会到了Promise的魅力！

## 意义

更好的支持异步编程

## 状态

要了解Promise，首先要了解Promise它所具有的状态。

Promise共有三个状态:

- pending(待定)
- fulfilled(兑现)
- reject(拒绝)

Promise初始状态为`pending`，当变为`fulfilled`或者`reject`时，状态将会被冻结，无法再次改变。

## 链式调用API

Promise的链式调用API有以下两个：

- then( callback(x) )
- catch( callback(x) )

`callback`表示回调函数，`x`表示链式调用**上一个Promise回调函数的返回值**，如果返回值是Promise对象则表示Promise所包含的值。

### 用法

- 当上一个promise的状态为fulfilled时，将执行下一个then()；

- 当上一个promise的状态为reject时，将执行下一个catch()。

`then()`与`catch()`返回的仍为Promise，这也是能够链式调用的根本原因。

如何判断promise是fulfilled或者reject？以下是reject的情况，其余均是fulfilled：

1. 显式地使用 `reject()` 方法
2. 异常抛出

该返回的Promise会封装then()和catch()回调函数的返回值(如果无返值则封装undefined)

```js
let promise = new Promise(
    (resolve, reject) => {
        resolve('promise');
    }
)

let pt = promise.then((data) => {console.log(data);});

// 考虑到异步的执行顺序,这里使用setTimeout,保证then()异步先完成
setTimeout(() => console.log(pt), 0)
// output: Promise { undefined }
```

因此你可以`promiseObj.then(callback).then(callback).catch(callback).then(callback).catch(callback)...`then()与catch()方法交叉使用,这种链式调用被称作**复合(composition)**.

在then()与catch()组成的方法链中，当前方法的回调方法的参数为当前方法的Promise对象所封装的内容，所以就可以避免了臭名昭著的回调地狱。

## Promise如何优化调回调

```js
new Promise((resolve, reject) => {
  xxx
  resolve(xxx)
  xxx
})
```

promise 只有在 resolve 或者 reject 才会调用then()

但这并不意味着当resolve或reject被调用后，该同级代码块的后面的代码就不执行了，后面的代码依旧会被执行

如果出现多个resolve，后面调用链的参数以第一个为准

根据这个特性，我们可以了解调 resolve/reject 决定了下一步执行的时机和参数。