---
title: "Understanding Time Zones"
excerpt: "Different regions have different times, understanding time zones can help us understand the rules of time in different regions."
---

# Time Zones

有没有想过，当我们是白天的时候，美国正是午夜，当我们时间为 `13:00` 的时候，美国正是 `01:00` 。有没有考虑过在同一时刻为什么时间不同，是什么规定了这些时间。

## UTC(Coordinated Universal Time)

[**协调世界时（UTC）**](https://zh.wikipedia.org/zh-hans/%E5%8D%8F%E8%B0%83%E4%B8%96%E7%95%8C%E6%97%B6)，是世界上调节时钟和时间的主要时间标准，时间上尽量接近**[格林威治标准时间（GMT）](https://zh.wikipedia.org/wiki/格林威治标准时间)**。

时区和经度有着紧密关系，**以本初子午线（0度经线）为基准，向东和向西每隔15度或30度划分一个时区**，向东的时区标准时间比本初子午线的时间提前，向西的时区标准时间则比本初子午线的时间落后。例如，北京位于东经116.4度左右，与本初子午线相差约116.4/15=7.76个时区，因此北京时间比UTC（协调世界时，即本初子午线的时间）提前8小时，也称 UTF+8 。

### Other

时间标准除了UTC，还有[夏令营](https://zh.wikipedia.org/zh-hans/%E5%A4%8F%E6%97%B6%E5%88%B6)等等，但都不常用或者渐渐被废弃。

## Time Zones Setting

Understanding the timezone can set it for our OS.

## Change The Time Zones

设置中国时区：

```shell
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

*中国时间为什么不是北京而是上海？因为上海的经度靠近经度120°，更接近UTC+8。*

查看当前时间：

```shell
date
```

输出：

```
Sun Feb 19 22:12:56 CST 2023
```

`CST` is the abbreviation for `China Standard Time`.

## Sync Time

下面以 ArchLinux 为参考同步系统时间，同步时间常用协议是 NTP(Network Time Protocal) 。

**systemd**

```ssh
sudo systemctl enable systemd-timesynced
sudo systemctl start systemd-timesynced
```

**openntpd**

1. 安装openNTPD  

```
sudo pacman -S openntpd
```

2. 开启和启用该服务 

```
systemctl start openntpd
systemctl enable openntpd
```





