# 从零搭建一个Android项目

首先创建一个文件夹并进入

```shell
mkdir gradle-project-demo && cd gradle-project-demo
```

执行gradle初始化命令

```shell
gradle init
```

提示你创建项目的类型

```
Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4] 2

Select implementation language:
  1: C++
  2: Groovy
  3: Java
  4: Kotlin
  5: Scala
  6: Swift
Enter selection (default: Java) [1..6] 4

Split functionality across multiple subprojects?:
  1: no - only one application project
  2: yes - application and library projects
Enter selection (default: no - only one application project) [1..2] 1

Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Kotlin) [1..2] 2

Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no] no 
Project name (default: viewmodel-demo): viewmodel-demo
Source package (default: viewmodel.demo): com.hihusky

> Task :init
Get more help with your project: https://docs.gradle.org/7.4.2/samples/sample_building_kotlin_applications_multi_project.html
```

选择kotlin语言作为项目实现语言、仅有一个应用项目（自动为你创建app子模块）、DSL为Kotlin（IDEA为kotlin提供了更好的语法支持）、项目名称、源码包（创建的app子模块会使用这个作为类路径加上app，比如com.hihusky.app.xxx.class），然后gradle自动执行init任务。

当然你也可以采用这种方式创建一个基础项目，方便你从头开始更深入了解

```shell
Select type of project to generate:
  1: basic
  2: application
  3: library
  4: Gradle plugin
Enter selection (default: basic) [1..4] 1

Select build script DSL:
  1: Groovy
  2: Kotlin
Enter selection (default: Groovy) [1..2] 2

Generate build using new APIs and behavior (some features may change in the next minor release)? (default: no) [yes, no] 
Project name (default: gradle-project-demo): gradle-project-demo

> Task :init
Get more help with your project: Learn more about Gradle by exploring our samples at https://docs.gradle.org/7.4.2/samples
```

基础项目的目录树

```
├── build.gradle.kts
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradlew
├── gradlew.bat
└── settings.gradle.kts
```

然后修改对应的文件

然后最终基本的android应用项目的目录树：

```
├── app
│   ├── build.gradle.kts
│   └── src
│       ├── main
│       │   ├── AndroidManifest.xml
│       │   ├── java
│       │   │   └── com
│       │   │       └── hihusky
│       │   │           └── app
│       │   │               └── MainActivity.kt
│       │   └── res
│       │       ├── drawable
│       │       │   ├── ic_launcher_background.xml
│       │       │   └── ic_launcher_foreground.xml
│       │       ├── layout
│       │       │   └── activity_main.xml
│       │       ├── mipmap
│       │       │   └── ic_launcher.xml
│       │       └── values
│       │           └── strings.xml
│       └── test
│           └── java
│               └── com
│                   └── hihusky
│                       └── viewmodeldemo
│                           └── app
│                               └── MessageUtilsTest.kt
├── build.gradle.kts
├── gradle
│   └── wrapper
│       ├── gradle-wrapper.jar
│       └── gradle-wrapper.properties
├── gradle.properties
├── gradlew
├── gradlew.bat
└── settings.gradle.kt
```

这里需要提示一下

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="com.hihusky.app">
    <application
            android:allowBackup="false"
            android:icon="@mipmap/ic_launcher"
            android:theme="@style/Theme.AppCompat"
    >
        <activity
                android:name="com.hihusky.app.MainActivity"
                android:exported="true"
        >
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
        </activity>
    </application>
</manifest>
```

你应该在这里声明出package所对应的目录，否则无法使用`R`进行资源引用。