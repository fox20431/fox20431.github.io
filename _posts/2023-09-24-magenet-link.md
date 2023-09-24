---
title: Magenet Link
date: 2023-09-24
---

# 磁力链接

磁力链接（Magnet Link），是对等网络中进行信息检索和下载文档的电脑程序。

和基于“位置”连接的统一资源定位符不同，磁力链接是基于元数据（metadata）文件内容，属于统一资源名称。

## Magnet URI Scheme

磁力链接包含了文件的元数据和Tracker服务器地址信息。下面是磁链的格式：

```
magnet:?xt=urn:btih:<hash>&dn=<name>&xl=<size>&tr=<tracker>&as=<source>
```

磁链以 magnet:? 开头，后面紧跟着参数列表。下面是参数的含义：

- xt：表示文件类型，一般都是固定值urn:btih。
- urn:btih：表示使用BitTorrent Info Hash作为标识。它是用于验证文件完整性的哈希值，通常使用SHA-1、SHA-256或其他哈希算法生成文件的唯一标识。这个参数是磁链中最重要的部分，指定了文件的哈希值。
- dn：表示文件名，一般与实际文件名相同。
- xl：表示文件大小，单位为字节。
- tr：表示Tracker服务器的地址。如果有多个Tracker服务器，则可以使用多个tr参数，每个参数对应一个Tracker地址。
- as: 表示源文件的网络地址，即文件的下载来源。

参数之间使用 `&` 符号分隔，参数名称和参数值之间使用 `=` 符号连接。

下面是一个示例磁链：

```
magnet:?xt=urn:btih:FEA025F1C2B5BA4543EBC9C50E0B4EA4D9E70F99&dn=myfile.zip&xl=21300&tr=http://tracker.example.com/announce
```

该磁链中包含了一个文件的元数据，文件名为"myfile.zip"，大小为21300字节，哈希值为"FEA025F1C2B5BA4543EBC9C50E0B4EA4D9E70F99"，使用了一个Tracker服务器地址"http://tracker.example.com/announce"。

总的来说，磁链是一种特殊的URL链接格式，包含了文件的元数据和Tracker服务器地址信息。参数之间使用 & 符号分隔，参数名称和参数值之间使用 = 符号连接。

## 类比BitTorrent

都是基于P2P（点对点）技术的文件共享协议，用户在下载文件的同时也扮演着上传方的角色。

## Tracker

Tracker服务器在这一过程中扮演着关键的角色。它的主要作用包括：

1. 协调Peers：Tracker服务器维护了一个记录所有正在下载或分享特定文件的Peers的列表。它追踪每个Peer的状态、可用性和下载进度。当用户连接到Tracker服务器时，它会向服务器注册自己的存在并获取Peers的地址列表。
2. 提供Peers的地址：Tracker服务器将Peers的地址列表提供给下载客户端，使其能够与其他用户建立连接并进行文件交换。通过这种方式，用户可以获取更多的下载源，并且当有新的用户加入时，Tracker服务器也会及时通知客户端。
3. 维护文件完整性：Tracker服务器还负责验证文件的完整性。它会跟踪每个Peer下载的文件块，并在需要时提供校验和验证，以确保文件被正确地下载和分享。

为了实现这些目的，Tracker服务器会记录并更新Peers的状态和提供可用性信息。当用户连接到Tracker服务器时，它会发送特定的请求，包括自己的标识和当前下载状态。Tracker服务器会根据这些信息更新Peers列表，并返回给用户其他Peers的地址列表。
