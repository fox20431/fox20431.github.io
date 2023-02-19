# Bean

Within the container itself, these bean definitions are represented as BeanDefinition objects, which contain (among other information) the following metadata:

- A package-qualified class name: typically, the actual implementation class of the bean being defined.

- Bean behavioral configuration elements, which state how the bean should behave in the container (scope, lifecycle callbacks, and so forth).

- References to other beans that are needed for the bean to do its work. These references are also called collaborators or dependencies.

- Other configuration settings to set in the newly created object — for example, the size limit of the pool or the number of connections to use in a bean that manages a connection pool.


# Inversion of Control (IoC)

> A bean is an object that is instantiated, assembled, and managed by a Spring IoC container.

> 翻译：bean是一个由Spring IoC容器实例化、组装和管理的对象。

与传统控制对象不同，对象由Spring IoC容器控制，而不由我们控制，所以称为控制反转。

# Dependency Injection (DI)

> Dependency injection (DI) is a process whereby objects define their dependencies (that is, the other objects with which they work) only through constructor arguments, arguments to a factory method, or properties that are set on the object instance after it is constructed or returned from a factory method.

翻译：

> 依赖注入（DI）是对象只能`通过构造器参数`、`工厂方法参数`或者`在属性已经被构造或工厂方法返回后在对象实例上设置的属性`来定义他的依赖（依赖是指与他一起运作的其它的对象）的过程



> DI exists in two major variants: Constructor-based dependency injection and Setter-based dependency injection.

翻译：

> DI存在于两个主要变体中：基于构造函数的依赖注入和基于Setter的依赖注入。 

通过官方文档原话我们可以得到以下有用的信息：
1. 依赖：与他一起运作的对象被称为依赖。  

# IoC与DI关系

> IoC is also known as dependency injection (DI).

> 翻译：IoC作为依赖注入（DI）所被熟知

# 为什么Spring能解偶

通过下面例子来讲解

这是Spring项目目录结构

```
src
├── main
│   ├── java
│   │   └── cn
│   │       └── arrayblog
│   │           └── pojo
│   │               └── Hello.java
│   └── resources
│       └── beans.xml
└── test
    ├── java
    │   └── HelloTest.java
    └── resources
```
共包含`Hello.java`、`beans.xml`和`HelloTest.java`三个文件

`Hello.java`:bean 
`beans.xml`:定义bean对象
`HelloTest.java`:创建bean对象

传统方式，仅`Hello.java`和`HelloTest.java`便能创建bean对象，属性赋值需要通过构造器、set方法或者工厂方法手动赋值。

如果使用Spring，那么你需要`beans.xml`来定义对象，`HelloTest.java`会根据`beans.xml`的内容所指定`Hello.java`来创建bean对象，并对其属性自动赋值。

# Q&A

Spring使得bean对象创建更复杂了吗？

- `beans.xml`文件的引入使项目结构变得复杂
- bean对象创建变得简单，因为属性自动赋值
- bean对象易于管理，因为都被存在`beans.xml`

Spring如何做到解偶？

Spring通过`beans.xml`来降低了`对象类`和`使用该对象类创建对象的类`的耦合度。

举个例子

不使用Spring，当我们手动创建一个`对象类`和`使用该对象类创建对象的类`，假设我们需要对`使用该对象类创建对象的类`进行关于`对象类`属性值的修改，那我们需要重新编译两个文件。

使用Spring，由于`beans.xml`不参与编译的原因，上述情况就可以通过修改`beans.xml`内容来解决。