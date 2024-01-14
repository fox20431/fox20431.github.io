---
title: linux DNS operating mechanism
date: 2024-01-13
---

# Linux DNS 运行机制



## Linux 默认情况下 DNS 解析流程


在Linux系统上，DNS解析通常是由用户空间的应用程序或系统库（如glibc）完成的。下面是Linux系统中DNS解析的一般步骤：

1. **应用程序发起DNS查询：** 当用户空间的应用程序需要进行DNS查询时，它通常会使用系统提供的解析库（如glibc中的`getaddrinfo`函数）或者使用专门的DNS客户端库（如`resolv`库）。
2. **查询本地缓存：** 解析库首先检查本地的DNS缓存，看是否已经解析过这个域名。如果有缓存，它会直接返回缓存的IP地址，避免了对DNS服务器的实际查询。
3. **向系统配置的DNS服务器发起查询：** 如果本地缓存中没有找到相应的记录，解析库将向系统配置的DNS服务器发起查询。系统配置的DNS服务器通常在 `/etc/resolv.conf` 文件中配置。
4. **递归解析：** DNS服务器可能会进行递归解析，即它会在自己的缓存中查找，如果找不到则向根DNS服务器查询，接着向顶级域（TLD）服务器查询，然后向权威DNS服务器查询，直到找到目标域名对应的IP地址。中间的DNS服务器可能会将查询结果缓存，以加速未来的查询。
5. **解析结果返回给应用程序：** 一旦DNS服务器找到了目标域名的IP地址，它将结果返回给解析库，解析库再将结果返回给应用程序。应用程序现在可以使用该IP地址与目标服务器建立连接。

## systemd-resolved

启用 `systemd-resolved` 服务

```sh
systemctl enable --now systemd-resolved.service
```

关于 `systemd-resolved` 描述可见

```
man systemd-resolved
```

总结：

1. 支持 DNS 缓存；
2. 作为验证 DNS/DNSSEC 的轻量级解析器；
3. 支持 LLMNR（Link-Local Multicast Name Resolution）和 MulticastDNS（mDNS）解析和响应。

### resolvectl

`resolvectl` 是 `systemd-resolved` 下的工具。

查看状态

```sh
sudo resolvectl status
```

清理缓存

```sh
sudo systemd-resolve --flush-caches
```



