# 为项目设置环境变量

官网参考：https://docs.spring.io/spring-boot/docs/current/reference/html/howto.html#howto.properties-and-configuration

## 原因

我曾经想过部署相关的问题：当我们项目打包后，application.properties/application.yml内的配置是写死的，这就要求我们在打包之前必须使配置文件与部署环境保持一致。比如数据库的账号密码，如果部署环境与本地不同，那么我们就需要再打包之前修改开发环境的配置文件再打包，打包后再改回部署环境，如果中间出现一些情况，来回调试十分不方便。

我就想到有没有一种方法，可以在产品打包后依旧可以修改配置文件，使其适应部署环境。

这种方法是存在的，就是通过命令行传递参数。

## 命令行传参

在spring配置文件写死的情况下，在Java/Gradle/Maven命令行使用`-Dargument=custom`参数将`custom`传递给配置文件的`arguments`，`-D`是**define**的意思。

但spring boot的配置文件字符较长，比如`spring.datasource.username=”root“`，这样传递参数的时候键入字符很消耗时间并且容易出错，可以通过`spring.datasource.username=${db.username:root}`，这样就可以使用`-Ddb.username=“root”`代替`-Dspring.datasource.username=”root“`。

这里`${db.username:root}`表示定义`spring.datasource.username`为 `db.username`，然后参数为`root`(可以不写)。

在开发环境中，项目的运行我们可以通过idea运行配置指定这些参数，但是单元测试使用的是maven/gradle，idea虽然可以为某个单元测试指定环境变量，但为所有单元测试指定环境变量是重复且无意义的事情。

那么我们可以在构建文件build.gradle.kts中这样配置：

```kt
tasks.withType<Test> {
    environment("db.username", "root")
    environment("db.password", "root")
    useJUnitPlatform()
}
```

当然，配置文件可以预先设置成与开发环境相同的，等到部署环境时候再指定参数。
