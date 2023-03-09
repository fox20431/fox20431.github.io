# 中缀表示法

* 它们必须是成员函数或扩展函数；
* 它们必须只有一个参数；
* 其参数不得接受可变数量的参数且不能有默认值。

下面两者等价
```kotlin
infix fun Int.add(x: Int): Int {
    return this+x
}

fun main() {
    println(1 add 2)
}
```

```kotlin
class Util(val number: Int) {
    infix fun add(x: Int): Int {
        return number + x
    }
}

fun main() {
    val u = Util(1)
    println(u add 2)
}
```