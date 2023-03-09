# Linux远程桌面

远程一般有两种方式VNC和RDP（MS-RD）

前者通用，后者时微软创建的协议，有压缩功能可以降低带宽压力。


## Gnome

安装 Gnome Remote Desktop

```sh
sudo pacman -S gnome-remote-desktop
```

在 settings > sharing > 开启 remote-desktop

主要是设置帐号密码，你可以看到其使用 `ms-rd` 连接方式，该方式默认使用 `3389` 端口。

所以选择支持RDP(ms-rd)的程序，在可访问的网络情况下，进行访问远程连接。

Android 可以使用 `RD Client` 应用，但显示效果不好，能能显示一部分而且会花屏。

你可以通过内网穿透，将该宽口暴露到公网上，通过公网就可以访问该主机了。

内网穿透可以选择 `ngrok` ，该服务提供公网和服务器，只需要注册即可。`frp` 需要自己有公网和服务器。

值得说的是，在进行设置的时候，请去掉代理，可以使用 `env -i command` 让命令忽略环境变量代理。