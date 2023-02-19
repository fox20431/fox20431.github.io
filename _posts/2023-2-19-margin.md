上下相邻的块级元素margin重叠不相加

原因:

1、水平边距永远不会重合。

2、在规范文档中，2个或以上的块级盒模型相邻的垂直margin会重叠。最终的margin值计算方法如下：

a、全部都为正值，取最大者；

b、不全是正值，则都取绝对值，然后用正值减去最大值；

c、没有正值，则都取绝对值，然后用0减去最大值。


解决方案:

- float
- inline-block
- 父级overflow:hidden
- 父级padding 
- 父级border
- 父级position:absolute
