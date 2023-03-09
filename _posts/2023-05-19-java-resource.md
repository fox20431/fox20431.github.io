---
title: The Summary of Getting Java Resources
excerpt: 
---



# Java Resources

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

Now, I have to say an **important** pitfall.

As we all know, the project should be packed in a `jar` package when the project is deployed on the server. There is no doubt the project resources are packed in `jar` package.

THIS IS IMPORTANT!!!

YOU CAN'T USE ANY FILE INTERFACE.

OR IT WILL REPORT:

```
Caused by: java.io.FileNotFoundException: class path resource [dicts/JMdict] cannot be resolved to absolute file path because it does not reside in the file system: jar:file:/C:/Users/ming/projects/omoidasu-api/build/libs/omoidasu-api-1.0-SNAPSHOT.jar!/BOOT-INF/classes!/dicts/JMdict
```

This is because the `jar` is just a file, not its own file system so that file packed in it is not a file now.

