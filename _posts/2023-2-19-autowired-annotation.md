# @Autowired注解

```java
@Autowired
private TestService service;
```

```java
private final TestService service;

@Autowired
public EnterpriseDbController(TestService service) {
   this.service = service;
}
```

上述两个案例，建议使用后者，因为@Autowired发生正构造器之后。

为什么使用final？

@Autowired本身就是单例模式，只会在程序启动时执行一次，即使不定义final也不会初始化第二次，所以这个final是没有意义的吧。