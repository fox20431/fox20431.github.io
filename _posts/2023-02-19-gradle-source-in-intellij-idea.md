# Gradle Source In Intellij Idea

在 `Intellij Idea` 中查看 `Gradle` 的源码。

gradle支持groovy和kts，按照平常使用经验groovy只能看到反编译的源码，而kts可以看到真实的源码。

通过对比可以发现，在使用kts作为gradle的dls时idea会自动为项目添加额外的库以供跳转到真实的源码。对比使用kts前后 `External Libraries > Gradle Script dependencies` 中的库的变化能判断idea增加了那些库，也是增加的这些库为kts提供了源码跳转支持。

本来对这个事情习以为常了，但最近我发现只要项目中存在一个kts作为gradle的构建文件，那么其他的用groovy语法的项目也能够跳转到真实源码，也就是说只要增加了上述所说的库无论是kts还是groovy都能够跳转到真实源码而非反编译的源码！这真的太离谱了，故意为难不适用kts的开发者吗，不愧是kotlin的亲爹...

但我又发现了，spring的项目在idea中打开后，虽然点击后跳转的依然是反编译的源码，单上面增加了 `download source` 的选项，然后 `attach downloaded source` 就可以让groovy的dsl跳转真实源码，我反复确实这个是spring特有的，普通项目不存在。

我自然又是查看`External Libraries`，对比发现多了很多个`library root`的库，这个标签标识这个库来自该项目，右击其中一个点击`Open Library Setting`发现他们都来自`buildScr`项目中，我判断应该是这个项目为项目增加了库，值得一提的是`buildScr`是一个Gradle构建系统的特殊文件夹，它在构建过程中用于编写自定义代码。

我就复制粘贴了`buildScr`到其他普通的gradle项目下，发现其他项目也拥有这个特性，也能查看源码，不得不说十分好用！

最终检测是`build.gradle`的这行代码生效：

```gradle
plugins {
	id 'java-gradle-plugin'
}
```

到此总结两个在intellij idea查看groovy源码的方案：

- 添加一个kts的构建文件，让intellij自动引入
- 使用`buildScr`，让gradle引入，再让idea识别gradle引入的
