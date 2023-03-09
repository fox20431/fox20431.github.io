# 布局方案

## 静态布局（static layout）

即传统Web设计，网页上的所有元素的尺寸一律使用px作为单位。

## Media媒体查询

按设备分辨率设计区间，每个区间有独自布局方案。

```html
html{font-size:10px}
@media screen and (min-width:320px) and (max-width:480px){html{font-size:12px}}
@media screen and (min-width:480px) and (max-width:640px){html{font-size:14px}}
@media screen and (min-width:640px){html{font-size:16px}}`
```

## 弹性布局（rem/em布局）

rem（font size of the root element）是指相对于根元素的字体大小的单位。 简单的说它就是一个相对单位。
em（font size of the element）是指相对于父元素的字体大小的单位。

## ViewPort

Viewport相关的单位有四个，分别为vw、vh、vmin和vmax。
vw：是Viewport's width的简写,1vw等于window.innerWidth的1%。
vh：和vw类似，是Viewport's height的简写，1vh等于window.innerHeihgt的1%。
vmin：vmin的值是当前vw和vh中较小的值。
vmax：vmax的值是当前vw和vh中较大的值。

在这个方案中，我们用vw来代替rem的缩放方案，就可以将页面做到任意环境下的同等自适应缩放。

