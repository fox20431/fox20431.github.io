---
title: github connection closed exception
date: 2023-10-19
---

# Github 连接被关闭异常

异常表现：

```
Connection closed by *.*.*.* port 22
```

原因是连接方式不安全。

**解决方案：**

编辑 `~/.ssh/config` 添加如下内容：

```
Host github.com
	Hostname ssh.github.com
	Port 443
```

