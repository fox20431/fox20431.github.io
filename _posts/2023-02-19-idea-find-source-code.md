你有没有考虑过idea如何定位到第三方库的源码的。

像maven、gradle等，一般下载第三方库的时候，在下载xxx.jar的同时还会下载xxx-source.jar。前者是编译后的压缩包，用于开发使用；后者是对应的源码，用于查看代码。

idea通过指定的路径规则来定位源码。比如gradle对应的位置都在~/.gradle，maven对应的位置都在.m2。idea作为构建工具的调用者，并不会改变这些位置，所以也不用猜测是idea在别的位置重新帮你下载了源码，他只是帮你找到源码位置，下载工作还是构建工具（maven、gradle）来完成的。

在构建android项目时，使用gradle wrapper出现了一个问题，我并不能查看build.gralde的源码，只能通过反编译来构建源码，比如android必包，idea并不能识别方法和里面字段，后来我才发现是我没有下载源码。

gradle wrapper的下载的源码，如果你留心观察过，它并没有压缩成gradle-xxx-source.jar的形式，而是以目录结构的形式展现，idea也能很好的识别。

在项目的`/gradle/wrapper/gradle-wrapper.properties`文件中：

```
#Fri Oct 22 16:36:02 CST 2021
# GRADLE_USER_HOME is `$USER_HOME/.gradle`
distributionBase=GRADLE_USER_HOME
distributionUrl=https\://services.gradle.org/distributions/gradle-7.0.2-all.zip
distributionPath=wrapper/dists
zipStorePath=wrapper/dists
zipStoreBase=GRADLE_USER_HOME
```

distributionUrl可以两种：

https\://services.gradle.org/distributions/gradle-xxx-all.zip

https\://services.gradle.org/distributions/gradle-xxx-bin.zip

xxx为版本，all包含源码，bin不包含源码。

所以你要下载all的版本。

同时如果你要开发android项目，直接使用android studio，相比idea，定制的android studio会有更好的开发体验。