# 方法引用(method reference)

`::`双冒号操作符(double colon operator)

如果函数式接口需要传入的方法已经定义，那么使用lambda匿名函数调用方法就会造成代码冗余，可以通过方法引用的方法，指定方法名，无需外套可lambda表达式。

以下是Java 8中方法引用的一些语法：

1. 静态方法引用（static method）语法：classname::methodname 例如：Person::getAge
2. 对象的实例方法引用语法：instancename::methodname 例如：System.out::println
3. 对象的超类方法引用语法： super::methodname
4. 类构造器引用语法： classname::new 例如：ArrayList::new
5. 数组构造器引用语法： typename[]::new 例如： String[]:new

## 示例

```java
@Test
public void doubleColonWithOneParamTest() {
  String a = "a";
  String b = "b";
  String c = "c";
  // double colon operation
  Arrays.asList(a, b, c).forEach(System.out::println);
  // 等价lambda
  // Arrays.asList(a, b, c).forEach((var) -> System.out.println(var));
}
```

### 解析

声明三个成员变量，使用`Arrays.asList(a, b, c)`将其加入数组中；然后遍历。

