# 单例

##  什么是单例

保证一个类仅有一个实例，并提供一个访问它的全局访问点。

## 为什么单例在多线程中不安全

单例代码：
```java
class Singleton {
    private Singleton() {};
    private Singleton instance;
    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
    }
}
```

当单例未创建实例，多个并发的线程同时执行到`install == null`都将创建对象。