# 日志等级
这里的日志是指内核信息的日志  
## 功能作用
日志等级拥有过滤功能，等级越高过滤的内容越多  
日志等级可为`0-7`，`0`是为处理过的日志文件  
## 查看日志等级
`cat /proc/sys/kernel/printk`  
## 修改日志等级
```
nvim /etc/sysctl.d/20-quiet-printk.conf
kernel.printk = 7 4 1 7
```

[等级参考](https://en.wikipedia.org/wiki/Printk)

四个等级从做到右分别对应：  
- console_loglevel
- default_message_loglevel
- minimum_console_loglevel
- default_console_loglevel


