---
title: Android CA Certifications
---

# Android CA Certifications

近日由于个人学习需求搭建了网络代理，用于中转流量。

为了确保安全，采用了TLS的加密方式，电脑能够测得延迟，但是手机不行。

后续了解到是因为TLS验证证书问题，原因是我服务器使用的ZeroSSL CA签发的免费内证书其根证书并不在Android系统中，所以系统无法建立TLS连接。

我尝试通过 `Settings` 里为安装 CA，却无济于事，其原因我也在[掘金文章](https://juejin.cn/post/7149098344445378568)上找到答案：

**Android 7.0以后，用户安装的证书不被系统认可。**

```
系统的证书目录：/system/etc/security/cacerts
用户证书目录：/data/misc/user/0/cacerts-added
```

当我使用Root权限配合Magisk的机制，将申请到的CA根证书转移到系统的证书目录中，之前无法连通连接就生效了！YYDS！
