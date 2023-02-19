# 位运算



```js
let a = 222 & (0xff >> 3) // 舍弃高三位
let b = 222 >> 3 // 舍弃低三位
console.log(a);
console.log(b);

// output
// 30
// 27
```

