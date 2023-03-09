# component-scan

## 如何使用

```xml
<context:component-scan base-package="org.example.xxx"/>
```

## 作用

扫描有`component`注解的包，批量注册成bean

## 条件

需要`component`注解，例如`@Controller`、`Service`和`@Repository`

既然需要注解，那肯定需要注解驱动：

```xml
<mvc:annotation-driven/>
```

## 优缺点

### 优点

- 批量注册，简单省力快速
- 方便源码阅读

### 缺点

- 由于是自动注册成Bean，如果有依赖需要注入，只能通过`@Autowired`，手动设置Bean则注解和配置都可以完成依赖注入
- 不便与解偶
- 不能集中管理