# 函数式接口

## 创建函数式接口

```java
@FunctionalInterface //添加此注解后，接口中只能有一个抽象方法。
public interface A<T, R> {
	R call(T t);
	// 可以包含其他default方法
}
```

函数式接口满足条件：

- 注解`@FunctionalInterface`
- 是接口
- 有且仅有一个抽象方法
- 可以包含多个default方法

不同函数式接口最大的区别就是**抽象方法的参数和返回值**，以及default方法。

java常见的内置函数式接口：Function、Consumer、Predicate、Supplier。

## 函数式接口使用

将函数式接口作为另一个方法的参数，并在方法中对函数式接口做修饰。

*这里的修饰是指，指定传出的参数以及对返回值的处理等。*

当调用该方法时，对应函数式接口参数就可以替换成lambda表达式。