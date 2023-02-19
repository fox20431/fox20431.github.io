# 安卓样式

`src/main/resource/values`都是用`resources`标签包裹的。

resource可以包含color，string，dimen，bool，style，declare-styleable，item，attr。

color，string，dimen，bool都好理解，格式都差不多，一个name，标签包裹指定格式的参数：

```xml
<color name="emerald_green_50">#E1F2EA</color>
```

可以在别的地方引用，引用方式很简单`@color/<name>`，他们存在的目的就是为了创造参数（常量）。

既然有参数，肯定有需要用的地方，那你有想过在哪里引用吗？

这就需要涉及attr的标签了，常见的引用就是在写样式的xml的时候，像这样：

```xml
<com.google.android.material.button.MaterialButton
    ...                                             
	android:text="@string/select_picture"
    ... />
```

你有想过android:text哪里来的吗，当你通过idea点进去你会发现，他是：

```xml
<declare-styleable name="TextView">
    ...
	<attr name="text" format="string" localization="suggested" />
    ...
</declare-styleable>
```

declare-styleable表示一个翻译为声明可样式化的，他主要是提供给view组件来使用，你可以查看具体某个view的源码，他的注释会标明使用了什么declare-styleable，比如：

```java
/**
 ...
 * <b>XML attributes</b>
 * <p>
 * See {@link android.R.styleable#EditText EditText Attributes},
 * {@link android.R.styleable#TextView TextView Attributes},
 * {@link android.R.styleable#View View Attributes}
 */
public class EditText extends TextView {
    ...
}
```

declare-styleable含有多个attr，一个标准的attr包含两个部分，一个是name另一个是format。

name可以让别人通过这个来使用，比如在declare-styleable里声明的attr，可以直接在view组件的xml中把name作为参数；format选择格式，如果是color那就填写颜色格式（或者引用），如果是dimen就填写尺寸格式（或者引用），如果是string就填写字符串（或者引用），如果是reference，就填写style。

```xml
<attr name="layout_width" format="dimension"/>
```

attr可以包含enum，这是一个组件通用的`android:layout_height`，你可以选择enum的name，使其为选中的值。

```xml
<attr name="layout_height" format="dimension">
    <!-- The view should be as big as its parent (minus padding).
                 This constant is deprecated starting from API Level 8 and
                 is replaced by {@code match_parent}. -->
    <enum name="fill_parent" value="-1" />
    <!-- The view should be as big as its parent (minus padding).
                 Introduced in API Level 8. -->
    <enum name="match_parent" value="-1" />
    <!-- The view should be only big enough to enclose its content (plus padding). -->
    <enum name="wrap_content" value="-2" />
</attr>
```

像下面这样

```xml
<EditText
          ...
          android:layout_height="wrap_content"
          ... 
          />
```

有人会想，为view组件设置了这么多attr，但我们创建的时候好像并不需要全部指明样式要怎么写，那样式是怎么默认复制的呢？其实这个是和我们主题（theme）有关系的。

主题属于style标签的，他和其他style的区别就是他会被被`AndroidManifest.xml`加载，而且包含很多默认属性以及全局属性。但其他的style需要你在view组件的xml里面手动加载。

style我们主题继承了parent，paren有包含了许多item，item就可以指明哪些attr该是什么值。

这里提示一下，主题。

就比如简单的`themes.xml`文件：

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="Theme.GinkgoLeaves" parent="Theme.Material3.Light">
        <item name="windowNoTitle">true</item>
    </style>
</resources>
```

他的parent继承了很多属性，但我们还是重写了一个样式`<item name="windowNoTitle">true</item>`。

当你点开name的值的时候你就会发现，他指向的是以一个attr标签，他包含的参数类型也和attr的format格式相同。

```xml
<attr format="boolean" name="windowNoTitle"/>
```

这样你也就能够理解item存在的意义，其实item还能做更多。

当你发现item直接被resource这个顶级标签包围的item似乎格式不太一样（这可能就是见人说人话，见鬼说鬼话吧...），这时候的item就是常量了，比如他可以代替string，color，demin，bool等，如下：

```xml
<item format="float" name="m3_sys_state_dragged_state_layer_opacity" type="dimen">0.16</item>
```

但引用的时候，也是按照规则引用，比如这个就需要写`@dimen/m3_sys_state_dragged_state_layer_opacity`。



整理上面所述：

resource 是顶级目录

attr color demin string bool item style declare-styleable 是resource包裹的内容

color demin string bool item style都是可以通过@xxx拿来用的。

想要用attr的话，可以使用?attr/xxx，假如这个attr被赋值了，那么就引用这个attr的值。

declare-styleable是无法直接使用的。



个人见解：

declare-styleable会包含attr

style: 会包含item，item可能会引用color demin string bool。

也就是说declare-styleable我创造问题，style你来给我解决问题。



view组件的xml是使用declare-styleable来包裹attr的，theme的是直接使用resource包裹attr的。

declare-styleable：/Users/ming/Library/Android/sdk/platforms/android-31/data/res/values/attrs.xml

theme对应的文件：values material-1.5.0/res/values/values.xml





