---
title: 51 SCM study note
date: 2023-12-14
---

# 51 SCM Study Note



```c
sfr P1 = 0x90
// 本质上是
volatile unsigned char *P1 = (unsigned char *)0x90;

// 访问 P1 寄存器的方式
// P1访问的是第一个位置的值
// P1^0 = 0x91
// P2^1 = 0x92
// ...
// 以此类推
   
// 所以P1本质上是个值
```



电平只有两种状态，1高电平，0低电平。

51SCM默认P引脚都与GND的电势差是5V（高电平），未接通的情况下是高阻抗。51是低电平导通。

