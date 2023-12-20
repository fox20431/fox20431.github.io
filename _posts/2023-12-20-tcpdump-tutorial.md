---
title: tcpdump tutorial
date: 2023-12-20
---

# TCPDUMP 教程

**DNS类型抓包**

下属是监听所有网卡源端口或目标端口的53端口的网络包，这里主要针对DNS（该协议使用53端口）：

```sh
sudo tcpdump -n -i any 'port 53'
# -n: Don't convert addresses (i.e., host addresses, port numbers, etc.) to names.
# -i: network interface => --interface=xxx
# `any` means capturing all interfaces
# 'port 53' is a filter condition.
```

当我们选择 `ping sss.s` ，未知域名的时候会从本地向上级路有发送的对53端口的查询。

输出如下

```log
16:56:55.337774 wlp44s0 Out IP 192.168.0.101.37635 > 192.168.1.1.53: 52538+ A? sss.s. (23)
```

**时间辍 网口名 出站/入站 地址类型(IP/IP6) 源地址 > 目标地质:  <包详情>**

`:`前面内容是IP/TCP协议通用的，后面内容根据不同的协议类型显示的不同。

`52538+`： 这表示 DNS 请求中的查询 ID。DNS 查询中的 ID 是一个16位的随机数，用于匹配 DNS 请求和响应。

`A?`：表示这是一个 DNS 查询，并且查询的类型是 A，即 IPv4 地址查询。

`sss.s.`：这是实际的 DNS 查询，表示正在查询的主机名或域名。

`(23)`：这是 DNS 查询的长度，即查询字段的字节数。

**TCP类型抓包**

首先在本次创建一个接受TCP的服务：

```sh
nc -l 12345
# listen port 12345
```

准备抓包：

```sh
sudo tcpdump -n -i any 'port 12345'
```

向端口发送内容：

```sh
echo "0101" | nc localhost 12345
```

这时候抓包内容如下，进行复位（RST）（第一行第二行），**三次握手（第三行到第五行）**，发送和响应信息（第六行和第七行）：

```
17:05:18.949975 lo    In  IP6 ::1.57762 > ::1.12345: Flags [S], seq 3733141808, win 33280, options [mss 65476,sackOK,TS val 2903481728 ecr 0,nop,wscale 7], length 0
17:05:18.949984 lo    In  IP6 ::1.12345 > ::1.57762: Flags [R.], seq 0, ack 3733141809, win 0, length 0
17:05:18.950022 lo    In  IP 127.0.0.1.38166 > 127.0.0.1.12345: Flags [S], seq 1465567219, win 33280, options [mss 65495,sackOK,TS val 2429543408 ecr 0,nop,wscale 7], length 0
17:05:18.950033 lo    In  IP 127.0.0.1.12345 > 127.0.0.1.38166: Flags [S.], seq 748706164, ack 1465567220, win 33280, options [mss 65495,sackOK,TS val 2429543408 ecr 2429543408,nop,wscale 7], length 0
17:05:18.950043 lo    In  IP 127.0.0.1.38166 > 127.0.0.1.12345: Flags [.], ack 1, win 260, options [nop,nop,TS val 2429543408 ecr 2429543408], length 0
17:05:18.950087 lo    In  IP 127.0.0.1.38166 > 127.0.0.1.12345: Flags [P.], seq 1:6, ack 1, win 260, options [nop,nop,TS val 2429543408 ecr 2429543408], length 5
17:05:18.950092 lo    In  IP 127.0.0.1.12345 > 127.0.0.1.38166: Flags [.], ack 6, win 260, options [nop,nop,TS val 2429543408 ecr 2429543408], length 0

```

上述Flags有很多

R：**RST (Reset the connection):** 重置连接。用于终止连接，表示连接出现严重问题。

S：**SYN (Synchronize Sequence Numbers):** 发起一个连接，用于建立连接。

.：**ACK (Acknowledgment):** 确认号字段（Acknowledgment Number）有效，表示确认号字段包含有效的确认序列号。

P：**PSH (Push Function):** 接收方应该尽快交付数据给应用层，而不是等待缓冲区满再交付。

F：**FIN (No more data from sender):** 发送方完成数据发送，用于关闭连接。

win表示窗口大小

下属是终止后的新增捕获：

```log
17:29:07.231823 lo    In  IP 127.0.0.1.38166 > 127.0.0.1.12345: Flags [F.], seq 6, ack 1, win 260, options [nop,nop,TS val 2430971689 ecr 2429543408], length 0
17:29:07.232048 lo    In  IP 127.0.0.1.12345 > 127.0.0.1.38166: Flags [F.], seq 1, ack 7, win 260, options [nop,nop,TS val 2430971690 ecr 2430971689], length 0
17:29:07.232086 lo    In  IP 127.0.0.1.38166 > 127.0.0.1.12345: Flags [.], ack 2, win 260, options [nop,nop,TS val 2430971690 ecr 2430971690], length 0
```

客户端发起终止（第一行），服务器收到终止后也发起请求终止（第二行），客户端承认服务器的终止（第三航）。

关于为什么四次挥手也是三个报文，这个解答我非常满意。[原文链接](https://www.quora.com/Why-is-the-TCP-connection-terminated-in-a-4-way-handshake)

> Four things need to happen for a TCP connection to **start**, and four things need to happen for a TCP connection to **end**.
>
> - **Starting:** A TCP connection has fully started when:
>   - each node has received a SYN flag from its peer (that’s two things, one SYN in each direction)
>   - and each node has received an acknowledgment of its own SYN flag from its peer (that’s two more things, for a total of four things that have to happen)
> - **Ending:** A TCP connection has essentially ended when:
>   - each node has received a FIN flag from its peer with no gaps in the sequence space (that’s two things)
>   - and each node has received an acknowledgment of its own FIN flag from the peer (that’s two more things, for a total of four things that have to happen)
>
> So **both starting and ending** a TCP connection involve a “four-way” handshake, for a pretty sensible reason: both sides have to do something, and then both sides have to acknowledge that the other side did that thing.
>
> The subtlety is that just because four things are happening, that doesn’t mean these four-way handshakes require four **segments** (i.e. packets).
>
> When establishing a TCP connection, it’s extremely common (not universal, but extremely common) that the non-initiating node will put its SYN flag and its acknowledgment of the peer’s SYN flag in the same segment (this is called a “SYN-ACK segment”). So the “four-way” establishment can use four segments, but generally packs everything into three (SYN, SYN-ACK, ACK).
>
> This is common because if a “server” has decided to accept a TCP connection that’s triggered because a “client” is trying to connect, the server’s TCP implementation must acknowledge the other side’s SYN flag, and to do that it has to send its own outgoing SYN. So it may as well do those two things in the same segment. (It doesn’t have to combine them into the same segment, but why not? It has to do both of them anyway.)
>
> When shutting down a TCP connection, it’s also possible for a node to combine two of the four things into one segment, i.e. a node can send a FIN flag and an acknowledgment of the other side’s FIN flag in the same segment. So it also is possible for TCP to do the “four-way” shut down using only three segments (FIN, FIN-ACK, ACK).
>
> But this is a lot less common. The reason is that upon receiving an incoming in-order FIN (indicating the end of the incoming byte stream), the receiving TCP implementation is not **required** to end its own outgoing byte stream. In other words, it’s not mandatory to send a FIN in reply to an incoming FIN — the question about when to end the outgoing byte stream is decided by the application, not by the TCP implementation. So when a TCP implementation receives an incoming in-order FIN (end of the incoming byte stream), it tells the application about it (e.g. with an EOF), and then the application has the choice about whether to end its own byte stream (e.g. with a shutdown() or close()). Unless the application makes that decision very quickly, the TCP implementation has probably already sent out an acknowledgement of the incoming FIN. So when the application shuts down or closes the socket, the TCP implementation will have to send a second segment with an outgoing FIN. Hence why it’s less common to combine FIN-ACK into one segment.
>
> But fundamentally: both starting and ending a TCP connection involve a “four-way” exchange, and both of these exchanges can use four segments or can be packed into three. It’s just a heck of a lot more common that the establishing handshake will be packed into three segments than the shutdown sequence.

其核心思想是建立和断开都是是4-way，Client.SYN - Server.ACK - Server.SYN - Client.ACK，这个步骤可以省略成 Client.SYN - Server.ACK&SYNC - Client.ACK

同理，挥手也是，RFC并没有挥手这一说法，所以挥手的说法也不标准，其核心思想就是 Client.FIN -  Server.ACK - Server.FIN - Client.ACK，实际上抓包也是这样，Client.FIN -  Server.ACK&FIN - Client.ACK



## Adanced

用 `-xx` 以16进制显示。