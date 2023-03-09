与XML path规则相同
https://www.w3school.com.cn/svg/svg_path.asp


下面的命令可用于路径数据：
M = moveto
L = lineto
H = horizontal lineto
V = vertical lineto
C = curveto
S = smooth curveto
Q = quadratic Belzier curve
T = smooth quadratic Belzier curveto
A = elliptical Arc
Z = closepath

viewportWidth vs width in android vector:

The viewportWidth and viewPortHeight define the area of the document that the content of the VectorDrawable is drawn within. They are equivalent to the width and height fields of an SVG viewBox. Research how an SVG viewBox works if you need further explanation.

So imagine your shape is a rectangle that is 100 wide and 100 height. Your viewportWidth and viewPortHeightshould normally both be set to 100. So that Android knows the dimensions of the underlying shapes.

The width and height attributes tell Android what the default ("intrinsic") rendering size of the VectorDrawable should be. You can think of these like the width and height of a PNG or GIF (or SVG for that matter).

So the contents of your VectorDrawable could be defined over an area of 100x100. But if your width and height are 24x24, the contents will be scaled down from 100x100 to 24x24.

So that's why fiddling with the viewportWidth and viewPortHeight messes with the VectorDrawable. So for instance, if you change them to 50x50, you would end up with one corner of the shape scaled down to 24x24 - instead of the whole shape.

总结：
viewportWidth/viewportHeight 与 viewbox宽高类似，规定了画图的区域，路径信息都与此相关，是个相对画布宽高。
width/height则是决定具体显示多少的宽高，在基于viewportWidth/viewportHeight进行缩放。
