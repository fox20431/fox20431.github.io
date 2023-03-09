# Assertion

断言是jdk1.4加入的特性。

关键字为`assert`，其后boolean类型的。

## 现象

assert后跟false

```java
@Test
public void assertionTest() {
  assert false;
  System.out.println("Test");
}
```

报错

```
java.lang.AssertionError
```

assert后跟true

```java
@Test
public void assertionTest() {
  assert true;
  System.out.println("Test");
}
```

输出结果

```
true
```

## 结论

断言就是当你假设一个命题，当这个命题为真则执行正常，如果命题为假则抛出异常。

用于判断程序流程。