---
title: Spring value
date: 2023-07-19
---

# Spring Value

`@Value` 注解支持两种常见的方式

1. SpEL(Spring Expression Language) - #{} 
2. Style property placeholder - ${}

讲一讲 `style property placeholder` 读取的优先级：

1. Spring 从系统属性（java运行时环境）查找该属性，即 Java 的  `System.getProperties()`，一般可以通过 `java -Dproperty=value` 传递参数
2. 环境变量
3. 配置文件
4. 默认值 比如${value: foo}中的foo