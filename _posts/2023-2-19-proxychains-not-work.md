proxychains 安装命令：

```shell
brew install proxychains-ng
```

原因：使用proxychains4 nmap的时候发现走的并非代理，而执行命令proxychains4 curl ifconfig.io 的时候，获取到的ip地址的确是本地的。无论怎么设置，都无法生效，流量就是不走设置好的socks5代理。
处理方法：关闭mac电脑System Integrity Protection (SIP)系统完整性保护，而在10.11 版本之前是没有的，所以需要关闭。

操作如下：

1. 关机
2. 开机的时候按住command+R 按钮，进入恢复模式，其实并不是去恢复系统，而是进入恢复界面，找到CMI命令行界面，这个类似windows进入了PE系统，这样子操作就可拥有对系统最大化的修改权，类似在windows下你删除system32 文件，显然是删不了的。但是在PE下就可以，这个进入恢复模式也是类似如此。
3. 执行命令：`csrutil disable`。这样子即可关闭，如果开启，执行如上操作，再次输入 csrutil enable 即可。
4. 检测命令：proxychains4 curl www.google.cn

Done