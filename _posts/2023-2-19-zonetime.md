# 时区

## 查看时间
`date`

## 时间类型

### UTC(Temps Universel Cordonné)
协调世界时

是世界上调节时钟和时间的主要时间标准，它与0度经线的平太阳时相差不超过1秒。

Arch Linux默认UTC时间为BIOS时间。

根据NTP(Network Time Protocol)可联网获取时间。

ArchLinux联网获取时间：  
1.安装openNTPD  
`sudo pacman -S openntpd`  
2.开启和启用该服务  
`systemctl start openntpd`  
`systemctl enable openntpd`  

### CST(China Standard Time)
当你执行这条命令之后：
`ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime`  
`date`中UTC变为CST
