注重记录不容易记忆的运算。

## 位运算

Java 使用 `小端` 字节排序，及从左到右代表的位数越来越低。

Java 可以通过添加下面前缀来用指定进制表示数值：

- `0x`    表示16进制
- `0`     表示8进制
- `0b`    表示2进制

示例：

```java
public class Example {
    public static void main(String[] args) {
        int a = 0b0011;
        int b = 0b1100;
        int c = a | b;
        System.out.println(Integer.toBinaryString(c));
	}
}

// output
// 1111
```

位运算适用于 `long` ， `int` ， `short` ， `char` 以及 `byte` 。

但请注意进行位运算后的数据类型均为 `int` ，验证这一结论可以使用 `JDK 5` 增加的 `自动装箱/拆箱` 特性，如下：

```java
public class Example {
    public static String getType(Object obj){            
        return obj.getClass().toString();
    }
    public static void main(String[] args) {
        byte a = 0b0011;
        System.out.println(getType(~a));
	}
}

// output
// class java.lang.Integer
```

这里着重讲 `>>>` 和 `>>`，前者是无符号右移位后者是有符号右移位。

`>>>` 很简单粗暴的将位右移并在左端空缺的位置补零，很明显不适用于负数（负数最左端为符号位表示为 `1` ）

`>>` 会遵守符号的规则。如果为整数左端补零，如果为整数左端补一。

有个奇怪的现象，对于左移 `Java` 只有 `<<` 这唯一的运算符，这是为什么？

因为左移的时候需要补充的位是右边的低位（和符号位无关），因此没办法根据符号来判断补充的是一还是零，因此统一为零。

位运算同时可以应用到布尔类型。对于布尔类型还拓展了 `&&` （短路与）和 `||` （短路或）这些短路（short circuit）运算。

短路的操作可以缩短逻辑运算。当 `&&` 左逻辑值为为 `false` 则右逻辑则不再运算，因为无论右边逻辑真假结果均为 `false`； `||` 则是左逻辑结果为 `true` 则不运算右边逻辑，结果总为 `true` 。

运算也有优先级：

|  |  |

除了单目运算，其他的多元运算符都可以通过括号来优先运算，所以当你忘记优先级的时候可以使用这个方法。

比如 `&` 的优先级高于 `|` ：

```java
public class Example {
    public static String getType(Object obj){            
        return obj.getClass().toString();
    }
    public static void main(String[] args) {
        int a = 0b00110011;
        int b = 0b00110111;
        int c = 0b00000100;
        int d = a | b & c;
        System.out.println(Integer.toBinaryString(d));
	}
}

// output
// 110111
```