---
title: The Summary of Getting Java Resources
excerpt: 
---



# Java Resources

我们要明白，无论开发环境还是生产环境 Java 运行的程序都是编译后的，所以通过程序获取的相对路径都是相对于编译后程序的位置。

现在Maven还有Gradle项目的目录都包含了`src/main/java`和`src/main/resource`，这些目录下的内容都会被递归编译/拷贝到jar包的根目录中。

There are a lot of approaches to getting project resources that refer to files located in `src/main/resources` here. 

Why is it necessary to be recorded?

- Organize all the approaches;
- There are a lot of pitfalls;
- It confused me and take me a lot of time.



## Select Resources

Assume there is a path of the file called  `src/main/resources/filename`; let's figure out how many approaches to get it.

**Approach 1**

```java
getClass().getClassLoader().getResourceAsStream("filename")
//getClass().getClassLoader().getResource("filename")
```

**Approach 2**

```java
@Autowired
private ResourceLoader resourceLoader;
resourceLoader.getResource("classpath:filename");
```

What is the difference between them both?

`Approach 1` is provided by Java; `Approach 2` is provided by Spring.

I recommend `Approach 2` to get resources because the interface provides a lot of functions to convince us. 



## PITFALL

Java中的文件系统API不支持直接访问位于JAR文件内部的资源。如果您想访问JAR文件中的资源，应该使用Java的类加载器来获取资源的输入流，而不是通过文件系统路径。

```
Caused by: java.io.FileNotFoundException: class path resource [dicts/JMdict] cannot be resolved to absolute file path because it does not reside in the file system: jar:file:/C:/Users/ming/projects/omoidasu-api/build/libs/omoidasu-api-1.0-SNAPSHOT.jar!/BOOT-INF/classes!/dicts/JMdict
```

