---
title: from transistor to CPU analog design
date: 2023-12-11
---

# From Transistor to CPU Analog Design

这个文章将讲述“逻辑电路设计”与“晶体管（Transistor）”的关系，以帮助工作在“逻辑电路设计”的朋友了解该工作对计算机（CPU设计）的意义，避免抽象的设计方式导致的学科断层。

## Introductory Common Sense

晶体管具有**开关功能**，这个是实现数字逻辑功能的关键，具体原理会在[晶体管结构章节](##Structure of Transistors)进行解释。

**CPU上存在着大量的晶体管**（P型或者N型），具体的数量和排列方式取决于设计。一般是使用光刻机将将图案投影到硅片上，制造芯片的各种结构。

## History

要讲晶体管（Transistor）首先要讲到真空管（Vaccum Tube，AKA. 电子管）。

两者都用放大信号、开关功能。早期的

## Structure of Transistors

晶体管包括：

- 场效应管（FET，Feild Effect Transistor），有栅极（Gate）、漏极（Drain）和源极（Source）
- 双极晶体管（BJT，Bipolar Junction Transistor），有发射极（Emitter）、基极（Base）和集电极（Collector）

真空管 -> BJT -> FET

### FET

MOSFET（Metal Oxide Metal Oxide Semiconductor FET）是常见的FET，常用于CPU。

The following is a simplified structure of an n-type **MOS (NMOS)** device.

![structure-of-a-mos-device](assets/structure-of-a-mos-device.png)

MOS (NMOS) Transistor symbols and switch-level models

![image-20231211224208292](assets/transisor-symbols-and-switch-level.png)

### BJT

下面是N型BJT

![NPN_BJT_basic_operation](assets/NPN_BJT_basic_operation.png)

Symbols


![Transistors - Practical EE](assets/symbols_bjts.jpg)



## Transistor for Logic Gates

The following image is excerpted from [GateRL](https://www.mdpi.com/2079-9292/10/9/1032?type=check_update&version=1).

![image-20231213145140539](assets/mos-for-logic-gates.png)

这样就能构成我们的逻辑电路库
