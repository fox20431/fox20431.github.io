---
title: MCU getting started tutorial
date: 2023-11-06
---

# MCU Getting Started Tutorial

MCU 入门教程

## Prerequisite

首先购买硬件：

- STC89C52RC-40I-PDIP40（单片机学习的主角） + 最小系统板（用于将DIP阵脚引出，也可以选择集成电子模块的系统板类似YL-39）
- USB to TTL电子模块（本人使用搭载CH340芯片的硬件，W11默认有驱动）
- 面包板 + 杜邦线（颜色、公母连接方式都买些，毕竟便宜）

注释：

> 1. DIP（Daul Inline Package ）为上述MCU使用的封装手段，但由于这种分装引出的阵脚不方便接线，所以需要再买个最小系统板
> 2. 杜邦线为美国杜邦公司生产的排线，英文称作Jumper Line

其次了解软件：

- keil uVersion5 C51
- STC-ISP

## 硬件

### STC89C52RC

由于采用DIP，共计40个引脚

放置单片机使其脚延伸方向远离你，缺口方向在左端，其引脚从坐下逆时针顺序分别为1-40

Transmit Data (TxD or TD)

Receive Data (RxD or RD)

### USB to TTL 与 STC89C52RC 接线

USB to TTL 的5V接最小系统板5V，GND接GND

TXD接RXD，RXD接TXD

## 软件使用

STC-ISP 在 `下载/编程` 的时候需要先按用鼠标点击 `下载/编程` 再接电源线，否则会无法识别单片机。

## 硬件排错

### CH340排除

将USB to TTL插入，将 RXD 和 TXD 短接，用 `Vofa+` 等软件测试串口是否可用，至于5V和GND可以接灯泡测试。

## Reference

- [USB to TTL 文档](https://www.cnblogs.com/ppqppl/articles/16758861.html)
- [STC-ISP 与 Keil vVersion5 C51 创建项目](https://zhuanlan.zhihu.com/p/477491382)