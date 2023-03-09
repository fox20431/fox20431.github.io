#　Android 用户界面多设备兼容

[Android 官方参考文档：Surrport different pixel densities](https://developer.android.com/training/multiscreen/screendensities)

## Android 单位

### 测量单位

Android用以下测量单位：

- **px (Pixels)** - Actual pixels or dots on the screen.
- **in (Inches)** - Physical size of the screen in inches.
- **mm (Millimeters)** - Physical size of the screen in millimeters.
- **pt (Points)** - 1/72 of an inch.
- **dp (Density-independent Pixels)** - An abstract unit that is based on the physical density of the screen. These units are relative to a 160 dpi screen, so one dp is one pixel on a 160 dpi screen. The ratio of dp-to-pixel will change with the screen density, but not necessarily in direct proportion. "dip" and "dp" are same.
- **sp (Scale-independent Pixels)** - Similar to dp unit, but also scaled by the user's font size preference.

注意**dpi**表示单位区域的像素数量，并不能直接表示长度，下面会提到。

### DPI

>  Configuration qualifiers for different pixel densities.

| Density qualifier | Description                                                  |
| :---------------- | :----------------------------------------------------------- |
| `ldpi`            | Resources for low-density (*ldpi*) screens (~120dpi).        |
| `mdpi`            | Resources for medium-density (*mdpi*) screens (~160dpi). (This is the baseline density.) |
| `hdpi`            | Resources for high-density (*hdpi*) screens (~240dpi).       |
| `xhdpi`           | Resources for extra-high-density (*xhdpi*) screens (~320dpi). |
| `xxhdpi`          | Resources for extra-extra-high-density (*xxhdpi*) screens (~480dpi). |
| `xxxhdpi`         | Resources for extra-extra-extra-high-density (*xxxhdpi*) uses (~640dpi). |
| `nodpi`           | Resources for all densities. These are density-independent resources. The system does not scale resources tagged with this qualifier, regardless of the current screen's density. |
| `tvdpi`           | Resources for screens somewhere between mdpi and hdpi; approximately 213dpi. This is not considered a "primary" density group. It is mostly intended for televisions and most apps shouldn't need it—providing mdpi and hdpi resources is sufficient for most apps and the system will scale them as appropriate. If you find it necessary to provide tvdpi resources, you should size them at a factor of 1.33*mdpi. For example, a 100px x 100px image for mdpi screens should be 133px x 133px for tvdpi. |

### px, dpi, dp 计算关系

**px**，**dpi** 和**dp**存在下列计算关系（官方）：
$$
px = dp \times (dpi \div 160)
$$
由于**px**和**dpi**是物理设备决定的，所以可以计算出相对测量单位**dp**；上式变形：
$$
dp = px \div dpi \times 160
$$

---

接下来实际计算**dp**：

已知设备 Nexus 7 参数为：1200x1920 px ，7.02" 。

计算对角线的像素，由勾股定理得：
$$
\begin{equation}
\begin{split}
px_{diagonal}
& = \sqrt[]{px_{width}^2 + px_{length}^2} \\
& = \sqrt[]{1200^2 + 1920^2} \\
& \approx 2264.2
\end{split}
\end{equation}
$$
已知对角线尺寸7.02英尺，则有：
$$
\begin{equation}
\begin{split}
dpi
& = \frac{px_{diagonal}}{in_{diagonal}} \\
& \approx \frac{2264.2}{7.02} \\
& \approx 322.5
\end{split}
\end{equation}
$$
根据Android定义的[density qualifier](###DPI)，**322.5**近似**320**的`xdpi`，故有：
$$
\begin{equation}
\begin{split}
dpi
&\approx 322.5 \\
&\approx 320 \\
\end{split}
\end{equation}
$$
根据定义 $px = dp \times (dpi \div 160)$ 计算宽度的dp：
$$
\begin{equation}
\begin{split}
dp_{width} 
&= px_{width} \div dpi \times 160 \\
&\approx 1200 \div 320 \times 160 \\
&= 600
\end{split}
\end{equation}
$$
得出dp的宽度为**600**。因为该手机官方给出的dp宽度为600，所以计算正确。

*Tips：假如手机官方未给出dp宽度，可以通过`安卓开发者模式`中`Smallest Width`来查看宽度dp。*

### px, density, dp 计算关系

$$
dp = px / density
$$

density表示像素密度，即1dp包含多个px。



## UI 适配

### 问题引出

通过上述计算我们得知**dp**是相对单位，相比绝对单位**px**，**dp**对适配支持更好，所以大多布局都选择这个**dp**作为测量单位。因为**dp**是相对单位，所以这个长度是可以自定义的（但该长度一般按照官方定义计算得出），最简单的自定义方式是在`安卓开发者模式`中修改`Smallest width`，还有一种自定义方式是在Android系统构建过程中提供虚假的物理参数（猜测），比如上段时间我三星手机刷第三方ROM会有不同的**dp**。但**dp**就能够完美适配所有机型了吗？各个设备有不同的参数，同时根据上述算法也会产生不同的**dp**，这也会产生适配的问题。那有没有一种简单的实现方式，就是无论什么情况下情况下我展示的是界面始终如一呢？

### 分析问题

用户界面适配问题其实简而言之就是不同型号手机在使用该应用过程中图形空间的利用是否合理问题。

让我说**dp**就是为了用户界面适配而存在的，因为目前主流手机的像素增长太快，而且分辨率参差不齐。假设手机像素远超平板，若使用**px**单位进行开发，你按照平板的布局来设计；当平板布局合理，那你将该应用放到手机上，你会发现一切界面都太小了！**px**带来的适配问题远不止于此，难不成每个型号都写个用户界面，不可能！

如使用相对长度**dp**，在理想情况下，各个厂商都按照Google的要求来，那么类型近似的设备会落在相同的区间下，比如目前主流大多数手机会在$[320,480)$这个区间，7寸平板在$[480,640)$，10寸平板在$[640~?)$。Android开发通过在layout上根据`smallest width`写多个样式文件可以支持上述UI兼容方式，如果为了适配更好，你也可以划分的更细致。但这个会出现一些问题，首先就是牵一发而动全身，比如你需要修改组件（包括添加、删除、修改样式等），那么你需要对每个都进行修改适配，再其次如果不是分发包（例如谷歌商店根据你手机型号来下载APK对应的资源）的话，包的体积大小也会增大。

### 解决方案

那有没有更好的解决方案能够解决**dp**的痛点，使用一套用户界面样式适配所有机型呢？

因为目前主流手机的长宽比例都是**4：3**、**16：9**、**16：10**等，长和宽的比例算不上差距很大。所以说就像图片一样，进行整体缩放将会是个很好的方案；但由于长宽比例不同，实际操作也会有影响。


所以就按照之前前辈告诉我的方式写一个`scale`缩放比例参数，来对样式进行一个缩放。其实归根结底就是确保组件的长宽在整个屏幕的的占比不变。

这个缩放必须是通用、遍历且递归的，不然这个缩放相比之前所写的适配难度只增不减，这个理论上可以实现，实际情况还需要根据Android的具体的View的数据结构来判断。

思路就是：

1. 计算要缩放的比例；
2. 缩放顶级组件；

3. 遍历子组件，并缩放子组件；

4. 子组件再遍历他的子组件，在缩放他的子组件；
5. 以此类推

整体缩放的计算方式如下：
$$
缩放比例 = \frac{要适配机型屏幕宽度（或长度）}{已适配机型屏幕宽度（或长度）} \\
要适配机型组件宽度（或长度） = 已适配机型组件宽度（或长度） \times 缩放比例
$$
这里要明白我们需要根据已适配机型的样式为基础来适配。

上述计算不能使用测量单位**dp**，因为他是相对的，但我们要选择绝对的，原因前面隐式提到。但是我们layout里面使用了**dp**，所以我们选择绝对的测量单位也必须和**dp**有关，根据上面计算公式不难猜到，我们需要使用**px**单位。

因此上述步骤就变成了这样：
$$
s = \frac{px_{要适配机型屏幕宽度（或长度）}}{px_{已适配机型屏幕宽度（或长度）的像素}} \\
dp_{要适配机型组件宽度（或长度）} = dp_{已适配机型组件宽度（或长度）} \times s
$$

2，3，4，5步骤可以抽出来，做遍历递归操作（后面会讲到）。

---

反射获取`ViewGroup`的`mChildren`行不通，因为字段上标注了`@UnsupportedAppUsage`注解（神秘力量）。



---

MeasureSpec 就用来封装 View 的 **size** 和 **mode** 这两个属性，它是 View 的一个静态内部类，用一个 int 类型的三十二位整数来表示这两个属性，前两位表示 mode，后三十位表示 size。通过单个整数来表示两个属性值并通过位运算来进行拆分可以更加节省内存空间。两个二进制位足够表示四种可能值，实际上 View 只用到了三种：UNSPECIFIED、EXACTLY、AT_MOST。`makeMeasureSpec` 方法就用于打包封装 size 和 mode 这两个属性值来生成 MeasureSpec