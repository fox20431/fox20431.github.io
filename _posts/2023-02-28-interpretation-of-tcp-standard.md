---
title: interpretation of tcp standard
date: 2023-2-28
---

# TCP标准解读

关于TCP（Transmission Control Protocol）IETF的RFC标准

https://datatracker.ietf.org/doc/html/rfc793

## 3-Way Handshake for Connection Synchronization

针对的连接同步的三次握手。

**步骤**

 Basic 3-Way Handshake for Connection Synchronization

```
      TCP A                                                TCP B

  1.  CLOSED                                               LISTEN

  2.  SYN-SENT    --> <SEQ=100><CTL=SYN>               --> SYN-RECEIVED

  3.  ESTABLISHED <-- <SEQ=300><ACK=101><CTL=SYN,ACK>  <-- SYN-RECEIVED

  4.  ESTABLISHED --> <SEQ=101><ACK=301><CTL=ACK>       --> ESTABLISHED

  5.  ESTABLISHED --> <SEQ=101><ACK=301><CTL=ACK><DATA> --> ESTABLISHED

```

`SEQ（Sequence Number）`：序列数，随机数，用于返回时确认字ACK；

`ACK（acknowledgment）`：序列数+1。

三次握手后，双方都知道了对方的序列号和确认号，就可以传输数据了。



断开和握手差不多，不要受到网上说的“四次挥手”的影响，实际也是三个包。
