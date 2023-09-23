通过这么久长达快一年的断断续续的Android的学习，我想做个阶段性总结。

目前还是入门新手阶段。为什么我学了快一年还是入门阶段，首先问题有很多。

1. 太懒，我属于没有皮鞭抽着我，我就不动的那种；
2. 忙于其他事情：考研（没怎么学）、游戏（遇到几款好玩的单机游戏，包括但不限于英雄联盟手游、饥荒、原神）、个人焦虑（大创、考研、年初的失恋）、追剧（野良神、瑞克和莫蒂、脱口秀大会等等，为了逃避焦虑）、爱情（失恋后的大半年，新的爱情找上了我）等等，算是荒废的大半年；
3. 学习效率太低，这里展开来说一个是自傲导致的眼高手低、一个是弯路走的有点多。

所以综合我的经历，我觉得我可以提出一些少走弯路的方法。

不要想着打破砂锅问到底的

首先，就是构建工具。比如我用gradle工具，应为gradle的dsl使用的是groovy，我会想着去学习groovy，但是这个东西比较冷门，资料很少，再加上我眼高手低看别人敲的代码挺对，想着我只是来了解一下的，而且语言相通也没什么难的，结果就是看完之后过段时间全部忘完，而且这完完全全就是歪路，因为android开发gradle作为构建工具并不需要我们掌握很多内容，而且groovy语言的学习对于dsl帮助意义并没有想象中那么大，相反我们可以了解一下每个闭包和属性的意义，这个只需要记忆而且对项目开发很有帮助。

其次，我们学校也开设了关于android的课程，但使用的是java语言和view构建的。同期的时候，android项目kotlin早已经作为首选语言了，其次compose的beta版本也出来了。我对学校的课程嗤之以鼻，但其实我学的也就半斤八两。关于kotlin的学习，我是买了《第一行代码》作为我的android开发的启蒙书籍，内容涵盖比较全面，上面有介绍的kotlin的内容，但由于内容不够详尽，后面我是查看官方文档的。因为kotlin也是跑在JVM上的，所以一些概念可以对比JAVA来学习，对于一些晦涩难懂的概念，即使配合JAVA也很难懂，有时候你还会发现你JAVA学的也没想象中那么好。好在之前有学过弱类型语言比如js、ts（学过，但没实际项目开发用过）等等，kotlin的一些设计理念我也是能理解一二。如今我会想一下，当时确实眼高手低，虽然老师用的老一套API和JAVA语言，但一些内容还是值得听的，比如……我也找不出来，但自己着实有点五十步笑百步。

然后就是关于IDE的选择，开始我用Intellij，我想一个Intellij就可以完成Android的项目，为什么还要单独下载一个Android Studio，然后我就也折腾了一阵子，后面发现还是Android Studio好一些，它对Android开发的一些细节做了处理，用起来更顺手。

关于IDE的下载配置，我倒没花多长时间。因为用了科技魔法，所以404一些问题不存在。

我很耐心的把《第一行代码》前几章都看了，也一边看书一边敲代码很多，搞得我颈椎都有点毛病了，看到后面没耐心了，把大纲看了，知道有这个玩意，这个玩意的作用，就草草了之。再到后面，我本的项目先行，有了基础，边实践边补充学习，做了一个计算器，基本上就是无脑跟着敲代码，具体为什么我也不太清楚。好在最后实现了，而且后面复习了两遍（最后课设需要看了一遍，想学习代码内容看了一遍），也有一点点收获。

关于《第一行代码》好不好，我开始认为这个本书就是圣经啊，贯穿了整个android项目，最后还有一个天气的实战，太香了。最近我重启我的android开发学习，我也懒得翻这本书了，大致内容我都有点印象了，我才发现你现在让我写个Activity我都不记得怎么写了，每一行代码什么意思我也不记得了。他书中肯定会有大白话介绍，但他的介绍由于书本的原因限制了很多，他也只能介绍浅显的内容，像八股文一样。我最近看了Google的Android开发文档，我才发现你静下心来，不要觉得它话多，它可以从设计理念和原因原理都给你讲一遍，让你有更深的理解，这里建议阅读英语版本的，中文的翻译有偏差，对理解会有障碍。

上面就是我学习Android的经验之谈，如有其他，后续我会补充。

关于Android项目，你首先要理解Android的目录结构对应的作用。

对于文件：

1. 你要理解gradle相关文件，比如项目和模块的build.gradle文件等；
2. 你要理解AndroidMenifest.xml文件，由于Android没有main函数，由这个文件配置载入Activity来运行程序；

这里要讲的太多了，我也不一一赘述。

关于程序运行的逻辑我有必要声明：

AndroidMenifest.xml -> AndroidMenifest.xml配置主Activity -> 主Acitivy类 -> 主Activity选择xml布局文件实例化 -> xml布局文件

当一个activity跳转的另外一个activity时，通过类跳转

当一个activity寻找嵌套其中的fragment时，可以通过xml布局文件静态设置（'app:name'关联类），也可以在类文件中动态添加（用到FragmentManger）。

---10.27---

关于navigation，你需要引入：

```groovy
// navigation
implementation "androidx.navigation:navigation-fragment-ktx:$nav_version"
implementation "androidx.navigation:navigation-ui-ktx:$nav_version"
// Testing Navigation
androidTestImplementation "androidx.navigation:navigation-testing:$nav_version"
```

其实还有一些库，但具体作用不详，我也没用到，就暂时不引入了，具体哪几个库可以见官方文档：https://developer.android.com/guide/navigation/navigation-getting-started

navigation的逻辑是这样的，activity中绑定layout。

MainActivity.kt

```kotlin
package com.example.onesentence

import androidx.appcompat.app.AppCompatActivity

class MainActivity :
    AppCompatActivity(R.layout.activity_main) { // pass view id to constructor, and you can omit 'setContentView(R.layout.activity_main)' code in 'onCreate' method.
}
```

activity_main.xml

```xml
<androidx.constraintlayout.widget.ConstraintLayout
	xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:fitsSystemWindows="true"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    tools:context=".MainActivity">

        <androidx.fragment.app.FragmentContainerView
            android:id="@+id/nav_host"
            android:name="androidx.navigation.fragment.NavHostFragment"
            android:layout_width="match_parent"
            android:layout_height="match_parent"
            app:layout_constraintTop_toTopOf="parent"
            app:layout_constraintBottom_toBottomOf="parent"
            app:layout_constraintLeft_toLeftOf="parent"
            app:layout_constraintRight_toRightOf="parent"

            app:defaultNavHost="true"
            app:navGraph="@navigation/nav_graph"/>

</androidx.constraintlayout.widget.ConstraintLayout>
```

这里添加`FragmentContainerView`控件，并且绑定`NavHostFragment`第三方类。

最后这个控件通过`app:navGraph="@navigation/nav_graph"`找到`res/navigation/nav_graph.xml`文件。

nav_graph.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<navigation
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/nav_graph"
    app:startDestination="@id/home_fragment">

    <fragment
        android:id="@+id/home_fragment"
        android:name="com.example.onesentence.fragments.HomeFragment"
        android:label="fragment_blank"
        tools:layout="@layout/fragment_home" >
        <action
            android:id="@+id/action_home_fragment_to_second_fragment"
            app:destination="@id/second_fragment" />
    </fragment>
    <fragment
        android:id="@+id/second_fragment"
        android:name="com.example.onesentence.fragments.SecondFragment"
        android:label="fragment_blank"
        tools:layout="@layout/fragment_second" />
</navigation>
```

nav_graph.xml可以添加多个fragment，这里我们添加两个fragment，分别为home fragment和second fragment。

这里需要设定`app:startDestination="@id/home_fragment"`起始的fragment，关于两个fragment的跳转可以采用`action`来进行跳转，这里我们设置从home fragment跳转到second fragment，但这个动作需要被触发。

引入了navigation框架，关于fragment的跳转我们只需要将其委托给框架，我们需要做的就是写fragment。

fragment_home.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <TextView
        android:id="@+id/text"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="Home Fragment"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        />

    <Button
        android:id="@+id/button"
        android:text="Jump to second fragment"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:layout_constraintTop_toBottomOf="@id/text"
        app:layout_constraintStart_toStartOf="parent"/>


</androidx.constraintlayout.widget.ConstraintLayout>
```

HomeFragment.kt

```kotlin
package com.example.onesentence.fragments

import android.os.Bundle
import android.view.View
import android.widget.Button
import androidx.fragment.app.Fragment
import androidx.navigation.findNavController
import com.example.onesentence.R

class HomeFragment : Fragment(R.layout.fragment_home) {

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        val button = view.findViewById<Button>(R.id.button)

        button.setOnClickListener {
            it.findNavController().navigate(R.id.action_home_fragment_to_second_fragment)
        }
    }
}
```

这里我们写了一个按钮用来触发指定id的action，这里需要注意，findNavController可以为Fragment也可以为View，两者都必须是属于`NavHostFragment`容器下，`NavHostFragment`在`activity_main.xml`中已经提到。

fragment_second.xml:

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    xmlns:app="http://schemas.android.com/apk/res-auto">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginStart="20dp"
        android:layout_marginEnd="20dp"
        android:text="Second Fragment"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        />

</androidx.constraintlayout.widget.ConstraintLayout>
```
SecondFragment.kt:

```kotlin
package com.example.onesentence.fragments

import androidx.fragment.app.Fragment
import com.example.onesentence.R

class SecondFragment : Fragment(R.layout.fragment_second) {

}
```

上述两个fragment都做了最简单的绑定。

这样运行程序，就可以得到最简单的navigation的demo。

访问内网接口

```
Instead of localhost/127.0.0.1 use 10.0.2.2 IP address.
```

## Q&A

对于`@+id/some_value`: 如果R.java中没有some_value这个值, 则在R.java中生成一个some_value值; 如果有则直接使用已经存在的值.

对于`@id/some_value`: 如果R.java中存在some_value这个值, 则使用此值; 否则会造成编译错误.

---

debug的时候源码对不上的原因？

你需要确保Android Emulator Image版本与当前的源码版本保持一致。
