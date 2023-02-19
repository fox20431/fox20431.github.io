# 泛型

## 泛型约束 Generic Constraints

单个上界

```java
class Monster<T extends Animal> {
    // codes
}
```

```kotlin
class Monster<T : Animal> {
    // codes
}
```

多重上界

```java
class Monster<T extends Animal & Food> {
    // codes
}
```

```kotlin
class Monster<T> where T : Animal, T : Food {
    // codes
}
```

## 型变 Variance

通配符类型参数

### 协变

`out`生产者

### 逆变

`in`消费者


## 投影 Projections

### 星投影

用来表明"不知道关于泛型实参的任何信息"。

