# 创建组件

```ts
// 创建实例
const app = Vue.createApp({ /* 选项 */ })
// 挂载组件
// 将app组件实例挂载到id为app的DOM元素上
const vm = app.mount('#app')
```

选项:
- data()
- method()
- computed()
- component
- props

# 注册组件

1. 全局注册

```ts
Vue.createApp({...}).component('my-component-name', {
  // ... 选项 ...
})
```

2. 局部注册

```ts
const ComponentA = {
  /* ... */
}
const ComponentB = {
  /* ... */
}
const ComponentC = {
  /* ... */
}

const app = Vue.createApp({
  components: {
    'component-a': ComponentA,
    'component-b': ComponentB
  }
})
```

# props

> 单向数据流: 父级 prop 的更新会向下流动到子组件中，但是反过来则不行。

1. 传递静态props
```html
<blog-post title="My journey with Vue"></blog-post>
```
2. 传递动态props
```html
<!-- 动态赋予一个变量的值 -->
<blog-post :title="post.title"></blog-post>
<!-- 动态赋予一个复杂表达式的值 -->
<blog-post :title="post.title + ' by ' + post.author.name"></blog-post>
```
3. props验证  
为props指定值类型
```ts
props: {
  title: String,
  likes: Number,
  isPublished: Boolean,
  commentIds: Array,
  author: Object,
  callback: Function,
  contactsPromise: Promise // 或任何其他构造函数
}
```
# props / $emit

1. 父组件可以使用 props 把数据传给子组件。
2. 子组件可以使用 $emit 触发父组件的自定义事件。

子组件
```html
<template>
  <div class="train-city">
    <h3>父组件传给子组件的toCity:{{sendData}}</h3> 
    <br/><button @click='select(`大连`)'>点击此处将‘大连’发射给父组件</button>
  </div>
</template>
<script>
  export default {
    name:'trainCity',
    props:['sendData'], // 用来接收父组件传给子组件的数据
    methods:{
      select(val) {
        let data = {
          cityname: val
        };
        this.$emit('showCityName',data);//select事件触发后，自动触发showCityName事件
      }
    }
  }
</script>
```

父组件
```html
<template>
    <div>
        <div>父组件的toCity{{toCity}}</div>
        <train-city @showCityName="updateCity" :sendData="toCity"></train-city>
    </div>
<template>
<script>
  import TrainCity from "./train-city";
  export default {
    name:'index',
    components: {TrainCity},
    data () {
      return {
        toCity:"北京"
      }
    },
    methods:{
      updateCity(data){//触发子组件城市选择-选择城市的事件
        this.toCity = data.cityname;//改变了父组件的值
        console.log('toCity:'+this.toCity)
      }
    }
  }
</script>
```



