---
title: gradle tutorial
---





# Gradle

## Create a gradle project

1. create and get into the directory

    ```
    mkdir my-wrapper-project && cd my-wrapper-project
    ```

2. Execute the init:

    ```
    gradle init
    ```

## CMD

upgrade gradlew

```cmd
 .\gradlew wrapper --gradle-version=7.6 --distribution-type all 
```

## Build

Gradle 引入依赖的三种方式

```groovy
dependencies {
    implementation project(':projectABC')
    implementation fileTree(dir: 'libs', include: ['*.jar'])
    implementation 'androidx.appcompat:appcompat:1.0.2'
}
```

gradle 刷新依赖

```sh
gradle --refresh-dependencies
```

Intellij IDEA 先入为主的观点，让我们以为 build.gradle 的每次更改都需要我们刷新。

而实际上这个刷新仅仅用作 Intellij IDEA 解析 build.gradle 的任务、依赖等，本质上 gradle 本身并不需要做什么，然而这个问题困扰了我很久，我因此上网查询这个浪费了很多时间，我认为，build.gradle 作为配置文件，是每次 gradle 执行都回去读取的文件。



用下列命令看看gradle更多信息

Gradle 命令之 --stacktrace ， --info ， --debug
