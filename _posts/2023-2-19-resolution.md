# 分辨率

## Pixel

像素（pixel），为影像显示的基本单位。

pix是英语单词picture的常用简写，加上英语单词“元素”element。

参考文献：[像素](https://zh.wikipedia.org/zh-cn/%E5%83%8F%E7%B4%A0)

## Inch

英寸（inch），长度单位。

$$
1 inch = 2.54 cm
$$

## PPI（DPI）

Dots Per Inch（Pixels Per Inch）

### 等式

$$
ppi = \frac{pixel}{inch}
$$

计算公式：
$$
dpi = \frac{\sqrt{height^2+width^2}}{size}
$$

### 参考意义

$$
a = 2 \arctan(\frac{h}{2d})
$$

其中$a$代表人眼视角，$h$代表像素间距，$d$代表肉眼与屏幕的距离。

将通常使用距离及正常眼能区分屏幕上两点的最小视角约为1’代入上公式可知：移动电话显示器的像素密度达到或高于300ppi就不会再出现颗粒感；手持平板类电器显示器的像素密度达到或高于260ppi就不会再出现颗粒感，而苹果笔记本电脑的Retina显示器像素密度只要超过200ppi就无法区分出单独的像素。

参考文献：[Retina显示屏](
https://zh.wikipedia.org/wiki/Retina%E6%98%BE%E7%A4%BA%E5%B1%8F)

## HiDPI

HiDPI High Dots Per Inch

*Retina显示器应用了HiDPI技术，但不能说Retina就是HiDPI*

常见共同出场词语：高分屏。

### 目的

为了更好的视觉展示效果。


### 特点

整数倍缩放。

### 原理

如果你修改过电脑桌面分辨率，或者说游戏内的分辨率，你会发现一个有趣的情况，当你调低分辨率的情况下，图形反而变大了。这种情况不难解释，在屏幕尺寸不变的情况下，调低分辨率相当于增大了单个像素的大小，因此像素数不变图形自然也会跟着变大。

猜测缩放背后发生了什么？现在我将1920x1080分辨率修改为1600x1200，图形虽然变大了，但显示很模糊。会不会是像素减少的原因呢？你又去尝试修改为640x480，你想这样就能看到像素锯齿了吧，但你依旧看不到明显效果。这是因为，在你减小分辨率的过程中，原分辨率会多出一些像素无处安放，这时候显卡就会采用**插值**算法，来猜测这些像素应该变现出什么颜色，这种猜测不是准确的，所以看起来很模糊。

*引申：因为没见过分辨率放大的应用，所以上述都是讲述分辨率缩小的情况。但图片缩小会遇到分辨率增大的情况，这时候设备的物理像素无法表现出的细节，将被丢弃。*

那有没有一种方法可以完美解决上述问题，既放大又不模糊？解决方案就是分辨率缩小的情况下避免插值算法。

分辨率缩小的情况下避免插值算法，可以通过整数倍缩小来实现。我目前电脑分辨率为2560x1600，将它长宽像素各缩小两倍（Pixel Ratio = 2），即面积放大四倍，得到分辨率为1280x800，那么2560x1600的四个像素对应1280x800的一个像素，只要2560x1600的四个一组的像素显示同一个颜色与1280x800的对应像素的颜色保持一致，这样就不需要插值算法来猜测，也就避免了插值算法。

如果你继续思考，你会觉得如果四个像素来表示一个像素，岂不是暴殄天物，还不如直接买个低分辨率的显示器。如果HiDPI只是做到这种地步，毫无疑问是个反智行为。HiDPI并非真的将四个像素当作一个来用，比如字体、位图、矢量图等可以使用更高的分辨率，HiDPI自然而然将四个像素独立工作，这些内容也不会涉及插值算法。

综上就可以达到放大切清晰的图像了。

### 应用

苹果电脑的Retina显示器。

Gnome的2倍缩放可以清晰显示，而xorg进行的分数缩放会模糊。因为前者是HiDPI，后者通过插值算法实现。分数倍缩放字体不模糊是因为字体是矢量图形，无论如何缩放都不会失真。

Windows二倍缩放不存在模糊问题，分数倍缩放存在模糊问题。


### 参考文献

[mbp2018规格](https://yesviz.com/devices/macbookpro-2018-13/)

[Retina和分辨率](https://www.paintcodeapp.com/news/ultimate-guide-to-iphone-resolutions)

[Retina详细解释](https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/Explained/Explained.html)

## DP、SP

- 微软：device-independent pixel
- 谷歌：density-independent pixel

A device-independent pixel (also: density-independent pixel, dip, dp) 

手机自定义DP

[查询css pixel](https://bestfirms.com/what-is-my-screen-resolution/)



## 像素在浏览器的应用

ddpx.innerText = devicePixelRatio;
sw.innerText = screen.width;
sh.innerText = screen.height;



## Q&A

Mac上分辨率的问题

我的Mac电脑是Macbook 13inch 2560x1600，但是我查看网页的分辨率为1400*900，我很好奇为什么是这个数值，因为从倍数上基本找不到关系，反而和16inch的2800x1800有着倍数关系。我刚开始猜测是因为是浏览器识别电脑型号导致的问题，后来才发现是Mac操作系统对外暴露的信息的问题，它向外传达的就是我是一台1400x900分辨率的显示器。这点我通过neofetch命令也验证了，他返回的结果也是1400x900，所以这只能说明不是浏览器的问题，而是操作系统的问题。

因为mac显示采用retina方案，就是多个物理像素点表示一个抽象像素的。后面我在Perfermances&rarr;Displays&rarr;Scaled里通过调节缩放，再通过neofetch获取分辨率信息，分辨率确实改变了，把分辨率改成1280x800后感觉好多了，不用整天把头埋在电脑面前了。显示字体大就是爽！！！