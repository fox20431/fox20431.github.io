Collection 继承树🌲(Collection inheritance tree)

![Collection Hierarchy in Java | Collection Interface - Scientech Easy](assets/java-collection-hierarchy.png)

## 解读

### Collection

List是`有序的`

Queue是具有`队列(先进先出)的`特性的

Set是`不能有重复元素的`的

### Arrays

是定长的数组。

创建方法

```java
int[] a = {1, 2, 3};
// or
int[] a = new int[3];
a = {1, 2, 3};
```

相比Collection，Collection有`add()`和`remove()`方法修改长度。

### Map

不定长的数组，但是存储的结构为键值对。