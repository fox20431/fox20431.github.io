# macbook使用指引

## 关于限制

关闭**SIP(System Integrity Protection)系统完整性**，该功能会限制我们root功能，详情见[关于 Mac 上的系统完整性保护](https://support.apple.com/zh-cn/HT204899)，关闭方法：

1. 关机
2. 开机的时候按住command+R 按钮，进入恢复模式，其实并不是去恢复系统，而是进入恢复界面，找到CMI命令行界面，这个类似windows进入了PE系统，这样子操作就可拥有对系统最大化的修改权，类似在windows下你删除system32 文件，显然是删不了的。但是在PE下就可以，这个进入恢复模式也是类似如此。
3. 执行命令：`csrutil disable`。这样子即可关闭，如果开启，执行如上操作，再次输入`csrutil enable` 即可。

未知开发者的安装包无法安装解决方案

```shell
sudo spctl --master-disable
```

## 关于安装

App Store

HomeBrew，HomeBrew的`brew services`用于服务管理，目的是为了简化MacOS的launchd的操作。

`sudo spctl --master-disable`设置之后允许来自任何来源的安装，且不会提示。

## 关于代理

v2ray privoxy proxychains-ng

MacOS系统代理：System Preferences > Network > Advanced > Proxies

这里将http和https都设置上，如果不设置https会导致类似git网络传输速度慢。

## 关闭Splotlight

1. From the finder, select “**Go**” > “**Utilities**” > “**Terminal**“.

2. Type one of the following commands, then press “

   Enter:

   - Enable Indexing – **`sudo launchctl load -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist`**
- Disable Indexing – **`sudo launchctl unload -w /System/Library/LaunchDaemons/com.apple.metadata.mds.plist`**





sudo mdutil -a -i off

## 关于