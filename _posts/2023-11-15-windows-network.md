---
title: windows network
date: 2023-11-15
---

# Windows Network



## 网卡

输入：

```
ipconfig
```

输出：

```
Windows IP Configuration

Ethernet adapter Ethernet:

   Media State . . . . . . . . . . . : Media disconnected
   Connection-specific DNS Suffix  . :

Wireless LAN adapter Wi-Fi:

   Connection-specific DNS Suffix  . : DHCP HOST
   Link-local IPv6 Address . . . . . : fe80::6262:15d6:82fe:943b%12
   IPv4 Address. . . . . . . . . . . : 192.168.0.101
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : 192.168.0.1
```

## 路由表

输入：

```powershell
route print
```

输出：

```
===========================================================================
Interface List
  4...98 8f e0 6b xx xx ......Intel(R) Ethernet Connection (16) I219-V
 12...10 b1 df 80 xx xx ......MediaTek Wi-Fi 6 MT7921 Wireless LAN Card
  1...........................Software Loopback Interface 1
 77...00 15 5d c5 xx xx ......Hyper-V Virtual Ethernet Adapter
===========================================================================

IPv4 Route Table
===========================================================================
Active Routes:
Network Destination        Netmask          Gateway       Interface  Metric
          0.0.0.0          0.0.0.0      192.168.0.1    192.168.0.101     30
        127.0.0.0        255.0.0.0         On-link         127.0.0.1    331
        127.0.0.1  255.255.255.255         On-link         127.0.0.1    331
===========================================================================
Persistent Routes:
  None
===========================================================================

IPv6 Route Table
===========================================================================
Active Routes:
 If Metric Network Destination      Gateway
  1    331 ::1/128                  On-link
 14    271 fe80::/64                On-link
 24    291 fe80::/64                On-link
===========================================================================
Persistent Routes:
  None
```

输出分为三部分：

1. Interface List

   第一列为接口MAC地址，第二列为接口描述

2. IPv4 路由表

   第一列为目的地网络地址，第二列为目标地址的子网掩码，第三列为通过的网关，第三列为使用的接口，第四个表示路由优先级（越小优先级越高）；

   `On-link` 表示数据包可以在本地链路上发送到目标地址，不需要通过路由器或网关；

   Persistent Routes表示持久路由，重启系统仍然有效的路由规则；

3. IPv6 路由表

   参考IPv4路由表