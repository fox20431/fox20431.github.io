# 接口

## 接口定义

- java接口可以是`public`，也可以是`friendly`，但一定是`abstracted`。
- java接口里的方法只能是`public`、`abstract`。
- java接口里的成员变量只能是`public`、`static`和`final`；并且必须赋初值，否则通不过编译。

```java
public abstract interface 接口名[extends 父接口名列表]{
	public static final 域类型 域名 = 常量值;
	public abstract 返回值类型 方法名(参数列表);
}
```

## 接口的特征
- 接口是由关键字interface定义的  
- 接口和方法默认为public abstract，变量默认是public static final类型的  
- 接口中的方法都是抽象方法，默认是public、abstract类型的  
- 接口没有构造方法，不能实例化，但可以定义接口的引用  
- 接口可以同时继承多个父接口  

## 接口使用

implement