---
title: Read Spring Source Code
---



# Read Spring Source Code

Spring Framework

## Build Spring Framework

1. 首先克隆项目到本地：

    ```shell
    git clone https://github.com/spring-projects/spring-framework.git
    ```

2. 选择稳定的版本进行构建：

   - Spring 的 main 的不同版本都会被打赏 Tag ，同下属命令查看所有版本

     ```sh
     git tag
     ```

   - 选择合适的版本，创建分支并切换到当对应 Tag 的提交

     ```sh
     # craete the branch
     git checkout -b reading/v6.0.9
     # switch to the version
     git reset --hard v6.0.9
     ```

3. 配置合适的环境

    - Java 环境：查看 `Gradle` 配置中的 `sourceCompatibility/targetCompatibility`

4. 执行构建脚本

    ```sh
    ./gradlew build
    ```

5. 然后将项目安装到本地的Maven

   参考[官方文档](https://github.com/spring-projects/spring-framework/wiki/Build-from-Source) *（由于官方文档落后版本且未说明针对的具体版本，对于不同情况需作出调整）*

    ```sh
    ./gradlew publishToMavenLocal -x api -x javadoc -x dokkaHtmlMultiModule -x asciidoctor -x asciidoctorPdf
    ```

	编译的项目会被安装到：

    ```sh
    $HOME/.m2/repository/org/springframework
    ```

6. 引入上述手动构建的Spring库

   以下是子模块项目中的 `build.gradle`

    ```groovy
    plugins {
        id 'java'
    }
   
    group 'com.hihusky.hellobeanannotation'
    version '1.0'
   
    repositories {
            mavenLocal()
        // mavenCentral()
    }
   
    dependencies {
        implementation "org.springframework:spring-context:5.3.23"
   
        testImplementation 'org.junit.jupiter:junit-jupiter-api:5.8.1'
        testRuntimeOnly 'org.junit.jupiter:junit-jupiter-engine:5.8.1'
    }
   
    test {
        useJUnitPlatform()
    }
    ```

    在上述文件中我们添加 ` mavenLocal` 告知 Gradle 从本地寻找依赖，同时将 `mavenCentral` 注释以防止本地无法找到从云端寻找。依赖的引入和从Maven仓库引入的方法一致。

    由于 `gradle` 和 `maven` 会本地缓存之前安装的依赖，请确保你引入依赖正确，可以采用以下几种方式：

    - 根据现在IDE提供的功能，查看引入依赖的文件位置；
    - 在库中DIY一些输出信息，随后编译，在引用库后设法打印出该信息。

### Common Questions and Resolutions：

- 接口弃用导致的错误
  
    编译提示如下错误
    
    ```sh
    error: warnings found and -Werror specified
    ```
    
    该项目使用了弃用的接口，启用的接口会发出警告，然后`-Werror`参数认为警告为错误行为，然后构建终止。
    
    修复的方法很简答，在`buildSrc/src/main/java/org/springframework/build/compile/CompilerConventionsPlugin.java` 文件中将这个参数取消：
    
    ```java
    COMPILER_ARGS.addAll(Arrays.asList(
      // blah, blah...
      // , "-Werror"
    ));
    ```

## Thinking in Reading Spring Framework Source Code

完成上述步骤，我们就可以阅读源码了。

库的源码/源文件比较多，它们之间交叉引用，同时对外暴露多个接口。

相比较应用文件，应用的源码虽然也交叉引用，但最终只会暴露出一个接口（通常是`main`函数）

因此要读懂一个应用，从看`main`函数看起，根据程序的流程不断探索就可以。

但库没有约定的唯一入口，但为了提供某种特定的功能必定暴露接口，所以我们要找到这个接口，怎么找？

- 看说明文档（不是接口文档）。你见过哪个复杂的库没有说明文档的？没文档谁能看懂？人传人吗？推荐✅
- 遍历所有源码文档，Spring的源码都有文档，没准有线索（效率低，命不够长）。不推荐❌
- 我曾想着从单元测试找到相关线索，但源码还是有点多，就算找到了我估计耗时也够呛。未知❓



我们没必要去把源码全部读完（嫌命长以及性格耐挫败的可以试试），要明确自己要了解的功能。

再去探索这个功能通过哪些接口实现。

再接下来就有一些讨巧的方法了：

- 用接口写样例，使用DEBUG配合IDE查看调用栈

- 配合IDE进行源码跳转功能，帮助我们更好阅读源码

为什么还要写个样例再debug，看起来比直接从源码跳转复杂的多。

一般通用的接口虽然对外暴露只是简单的调用，但内部为了适合多种情况一般有多种分支，从暴露的接口不断跳转源码，就类似于主线任务进入多条支线任务，支线任务有进入多条子支线任务，指数爆炸知道吗，所以你清楚你最后应该去哪条支线任务吗，还是说命长把所有结果都遍历一遍。

同时DEBUG是具体的，相反直接看源码是抽象的，他的变量以及流程是不确定的。

所以，爱一个具体的人，也要爱一个具体的样例。



大局上掌握代码，你可以发现大多代码是调用的函数，函数又会调用其他函数。

如果将一行行代码作为节点的话，代码的执行其实就是树状结构，而被真正执行的都是没有子节点的节点。

## Skill Determines Speed

技巧在很大程度上决定你阅读源码的速度

这里的技巧主要是指

- IDE的使用，提供的功能特性和快捷键等

- 注释文档相关介绍

### IDE使用

在这里我使用的是`Visual Studio Code`

它的Palette特性很重要，简单介绍一下：

- `$filename`跳转到指定文件
- `>$task` 执行任务

- `#$file`跳转到库的文件
- `@function`跳转到方法

还有一些自定义的信息可以配置，比如

```json
{
	"editor.stickyScroll.enabled": true,
}
```



### 注释文档

类#方法

类$内部类

## Content about Reading Spring Framework Source Code

继续读前友情提示：

```java
if (急躁||不实践) {
	劝退();
}
```

在看源码时，你也应该留意包和类名。

通过对源码解读我发现有趣的现象，当源码使用`do`开头的方法，都是实现某种功能的具体代码，比如

```java
org.springframework.core.io.support.PathMatchingResourcePatternResolver#doFindAllClassPathResources(String)
```

### bean是如何被spring framework托管的？

以下面简单的示例作为开端：

```java
// file name: Application.java
package com.hihusky.hello_bean_annotation;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
public class Application {
    public static void main(String[] args) {
        Greeting greeting;
        SecondGreeting secondGreeting;
        ThirdGreeting thirdGreeting;
        try (AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext()) {
            context.scan("com.hihusky.hello_bean_annotation");
            context.refresh();
            greeting = context.getBean(Greeting.class);
            secondGreeting = context.getBean(SecondGreeting.class);
        }
        System.out.println(greeting);
        System.out.println(secondGreeting);
        System.out.println(thirdGreeting);
    }
}

// file name: Greeting.java
package com.hihusky.hello_bean_annotation;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
@Component
public class Greeting {
    private String message;
    public Greeting(@Value("Hello, Annotation!") String message) {
        this.message = message;
    }
    public String getMessage() {
        return this.message;
    }
    public void setMessage(String message) {
        this.message = message;
    }
    @Override
    public String toString() {
        return "Greeting{" +
                "message='" + message + '\'' +
                '}';
    }
}

// file name: SecondGreeting.java
package com.hihusky.hello_bean_annotation;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Component;
@Component
public class SecondGreeting {
	private String message;

	public SecondGreeting() {
	}
	public SecondGreeting(@Value("Hello again, Annotation!") String message) {
		this.message = message;
	}
	public String getMessage() {
		return this.message;
	}
	public void setMessage(String message) {
		this.message = message;
	}
	@Override
	public String toString() {
		return "SecondGreeting{" +
				"message='" + message + '\'' +
				'}';
	}
}
```

上述样例借助Spring的注解`AnnotationConfigApplicationContext`以及配合`@Component`完成将`Greeting`以及`SecondGreeting`实例化，并交给Spring管理。

接下来我们将以`Application.java`为中心分析代码

```java
AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext()
```

构造器创建默认的注解上下文

```java
context.scan("com.hihusky.hello_bean_annotation");
```

扫描这一步执行的步骤比较繁琐，请耐心看完。

首先是将`com.hihusky.hello_bean_annotation`这个包名处理成`classpath*:com/hihusky/hello_bean_annotation/**/.class`，用来检索该目录下的所有类文件，配合`ClassLoader`同时解析成元数据`org.springframework.core.type.classreading.SimpleAnnotationMetadata`，其中包含注解、类名等。

然后根据元数据做过滤，过滤的具体方法是`org.springframework.context.annotation.ClassPathScanningCandidateComponentProvider#isCandidateComponent(MetadataReader)`。该过滤方法会用到成员变量的两个过滤器，一个是`excludeFilters`，这个过滤器会排出该过滤器符合条件的类文件；一个是`includeFilters`，这个过滤器会添加符合条件的类文件。

由于我们使用的是以注解的方式添加bean，所以这里`includeFilter`为`org.springframework.core.type.filter.AnnotationTypeFilter`（`excludeFilters`为空），它会将包含`@Component`注解的类文件进行标记添加。

最终筛选出符合条件的类做成集合`Set<BeanDefinitionHolder>`

`Set<BeanDefinitionHolder>` 再经过层层处理成为

`org.springframework.beans.factory.support.DefaultListableBeanFactory`类中的成员变量：

```java
private volatile List<String> beanDefinitionNames = new ArrayList<>(256);
private final Map<String, BeanDefinition> beanDefinitionMap = new ConcurrentHashMap<>(256);
```

对这个转换有兴趣的小伙伴可以将断点打在`org.springframework.beans.factory.support.DefaultListableBeanFactory$registerBeanDefinition`方法上，通过上下文（调用栈附近的代码）来了解。

```java
context.refresh();
```

这一步以`beanDefinitionNames`为参考，将所有的bean以单例模式（默认）实例化。

这个参考依据可以查看`org.springframework.beans.factory.support.DefaultListableBeanFactory.preInstantiateSingletons`方法。

大家如果想了解如何被实例化的，我们可以逆向思维，要想实例化，Java就那几种方法：

- `T java.lang.Class#newInstance()`
- `T java.lang.reflect.Constructor#newInstance(Object ... initargs)`

第一种还被弃用了，如果想要实例化很大可能就是第二种方式进行实例化，先打个无声断点（Mute Break Point 就是灰色的断点）在第二个方法上，我们已知是在扫描开始后才进行初始化的，我们在扫描函数上打上断点，这样我们就可以缩小范围，避免`newInstance`断点停在非想要的位置（缩小范围）。随后开始调试，先停在扫描操作的断点上，然后将无声断点恢复，然后`continue`断点让其听到实例化的断点上，这时候我们需要不断的`continue`同时注意旁边的变量参数我们想要的实例化是否出现，出现后可以看看调用栈和代码之类的。

如果你用了上述操作你可以发现，调用栈中使用了为`org.springframework.beans.factory.support.DefaultSingletonBeanRegistry#instantiateBean(String, RootBeanDefinition)`方法。

```java
greeting = context.getBean(Greeting.class);
```

取数据就比较简单，直接从先前的`registery`中取单例。

综上就完成了Spring托管bean流程，不难看出主角还是`Registry`。
