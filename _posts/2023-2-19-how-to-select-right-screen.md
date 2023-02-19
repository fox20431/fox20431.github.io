就按照常规屏幕来说

1920*1080 px

15.6 inches

windows 缩放多少合适 1.25

假设人的位置不变，想在同一块位置看到大小一致的图像，只需要确保每英寸的相对像素数量不变就好。

拿宽度的相对像素1920/1.25

然后计算每英寸的1920/1.25/15.6约等于98.5

按照linux只能整数倍缩放，所以这里选择2整数，选择14英寸的设备（thinkpad x1 carbon），那么我们继续需要多大像素的屏幕

98.5x2x14 = 2758

所以需要2.8k屏幕。



下面使用python更准确的计算：

```py
import math
from sympy import *
import numpy as np

print("以下均以笔记本为参考标准：")

# 假设 15.6inch 1920x1080 x1.25 屏幕显示效果最为理想
# 根据这个数据求出不同尺寸的最理想想对像素

# 求对角线像素，平方根公式
diagonalPixel = math.sqrt(np.power(1920, 2) + np.power(1080, 2))
# 求相对像素
relativeDiagonalPixel = diagonalPixel / 1.25
# 设x为目标显示器理想像素
x = Symbol('x')
# symbolic mathematics
solutions_13 = solve((relativeDiagonalPixel / 15.6) * (13 / x) - 1, x)
print('13英寸理想对角线长度：', solutions_13[0]*2)
solutions_14 = solve((relativeDiagonalPixel / 15.6) * (14 / x) - 1, x)
print('14英寸理想对角线长度：', solutions_14[0]*2)
solutions_23_8 = solve((relativeDiagonalPixel / 15.6) * (23.8 / x) - 1, x)
print('23.8英寸理想对角线长度：', solutions_23_8[0])

p_1080 = math.sqrt(np.power(1920, 2) + np.power(1080, 2))
k_22 = math.sqrt(np.power(2240, 2) + np.power(1400, 2))
k_28 = math.sqrt(np.power(2880, 2) + np.power(1800, 2))
print("1080p 对角线像素：", p_1080)
print("2.2k 对角线像素：", k_22)
print("2.8k 对角线像素：", k_28)

"""
这里面对比过程中我参杂了一个23.8inch 1920*1080 x1的台式电脑显示器
发现以笔记本理想状态去衡量台式电脑显示器的分辨率有较大的误差

以笔记本标准计算出的23.8inch对角线像素高于实际对角线像素
同样大小尺寸的显示器，高像素就意味着能展示更多内容，也就意味着相同像素的图片在物理长度更小
最后得出实际上23.8inch的显示器像素低，相同像素展示比笔记本上的要大

为什么实际上23.8inch展示的图片比笔记本展示的较为明显的大
但人的感知依旧不明显呢？
原因很简到，近大远小

正常人眼到笔记本的距离短，大约40cm左右，而到台式显示器的距离可以有60cm，所以感知不明显

由于我个人有头前倾的倾向（不自觉地头前倾），所以我个人潜意识是认为呈现的内容较小的

所以我要选的就是比理想笔记本略大，但绝对要小于台式显示器
"""
```

