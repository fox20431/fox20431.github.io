# 回调函数

## 定义

> A callback function is a function passed into another function as an argument, which is then invoked inside the outer function to complete some kind of routine or action.

摘录[MDN - Callback Function](https://developer.mozilla.org/en-US/docs/Glossary/Callback_function)

## 例子

```kotlin
fun greeting (name: String) {
    println("Hello, $name")
}
fun processUserInput(callback : (name : String) -> Unit) {
    println("Please enter your name.")
    val name = readLine()
    callback(name ?: "null")
}

fun main() {
    processUserInput(::greeting)
}
```

## 回调与调用的区别

调用：call
回调：callback

举例：我们两人打电话，称这个行为为`call`；我俩已经通过电话了，再次通电话叫做`callback`。我现在参数声明里给你“通电话”，告诉你我可以给你办公，等你觉得你需要我工作的时候“再给我通电话”，这就是回调。

谷歌翻译为：

an invitation to return for a second audition or interview.

邀请返回进行第二次试镜或面试。

这里可以理解为，函数不再是直接调用（call），而是传入被用作调用。

对比回调与调用：

```kotlin
fun hello(){
	println("hello")
}
fun hi() {
	println("hi")
}
fun say(callback : () -> Unit) {
	callback();
}

fun main() {
	say{ hello() }
	say{ hi() }
}
```

```kotlin
fun hello(){
	println("hello")
}
fun hi() {
	println("hi")
}
fun say() {
	hello()
	hi()
}

fun main() {
	say()
}
```

可以明显的发现回调函数的更加灵活，不必将要调用的函数预先固定写在代码中，而是在调用函数的过程中确定函数要回调的函数。
