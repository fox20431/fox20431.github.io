# export


a.js
```js
export var name="李四";
```

b.js
```js
import { name } from "/.a.js"
export default {
  data () {
    return { }
  },
  created:function(){
    alert(name)
  }
 }

```

`export`与`export default`
1. export与export default均可用于导出常量、函数、文件、模块等
2. 你可以在其它文件或模块中通过import+(常量 | 函数 | 文件 | 模块)名的方式，将其导入，以便能够对其进行使用
3. 在一个文件或模块中，export、import可以有多个，export default仅有一个
4. 通过export方式导出，在导入时要加{ }，export default则不需要

# import

输入模块