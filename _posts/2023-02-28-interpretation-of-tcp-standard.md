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

序列号和确认号是TCP协议中用来保证数据传输可靠性和有序列的两个重要字段。序列号是用来标识从发送端向接收端发送的字节流的顺序，每发送一次数据，就累加一次该数据字节数的大小。确认号是用来表示接收端期望收到的下一个数据的序列号，发送端收到接收方发来的确认号后，就知道对方已经收到了哪些数据，可以继续发送后续的数据。通过序列号和确认号，TCP协议可以实现流量控制、拥塞控制、重传机制等功能，提高通信效率和质量。

注意，第二次握手的SYN+ACK是一次性发送的，不是分别发送了SYN和ACK包。这是因为TCP协议中有一个标志位字段，可以同时设置多个标志位。

**二次握手不能满足安全通信吗？**

假设信道不好，当第一次握手客户端请求连接的包超时未送达，为了尝试重新建立连接，客户端就会再次发送连接请求，然后超时的包后也送达后，服务端会认为是两次请求从而浪费资源，所以需要服务端发送请求（第二次握手）去确认是否是这个请求，以得到第三次握手客户端发来的确认。

## 四次挥手


**步骤**

1. 第一次挥手，客户端发送一个FIN包，表示关闭数据传输，进入FIN_WAIT_1状态。
2. 第二次挥手，服务器接收到FIN包后，回复ACK包，表示已经收到客户端关闭的请求，进入CLOSE_WAIT状态。客户端收到ACK包后，进入FIN_WAIT_2状态。
3. 第三次挥手，服务器发送一个FIN包，表示要关闭数据传输，进入LAST_ACK状态。
4. 第四次挥手，客户端收到FIN包，回复一个ACK包，表示统一断开连接，进入TIME_WAIT状态。服务器收到ACK包后，关闭连接，进入CLOSED状态。客户端等待一段时间后（2MSL），也关闭连接，进入CLOSED状态。

客户端要等待一段时间的原因是为了确保服务器收到了客户端的最后一个ACK包，以及防止网络中可能存在的旧的报文段对新的连接造成影响。
