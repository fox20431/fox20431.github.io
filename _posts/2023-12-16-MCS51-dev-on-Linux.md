---
title: 51 SCM dev on Linux
date: 2023-12-16
---

# 51单片机在Linux上的开发

## 识别

插入串口模块，显示USB设备确保被电脑识别：

```sh
lsusb
```

输入结果，识别出了我的CH340的串口模块：

```
Bus 003 Device 007: ID 1a86:7523 QinHeng Electronics CH340 serial converter
```

如果没有 `lsusb` 命令，安装如下包：

```sh
sudo pacman -S usbutils
```

查看设备文件：

```sh
ls /dev/ttyUSB*
```

如果没有则安装该驱动驱动：

- [CH340 沁恒官网Linux驱动下载](https://www.wch.cn/downloads/CH341PAR_LINUX_ZIP.html)

自己没编译成功，其次Arch高版本Linux内核自带ch341驱动。

```
lsmod | grep ch34
```

如果有`ch34x`或者`ch341`模块依旧没有`ls /dev/ttyUSB*`文件，尝试移除以下可能导致冲突的包：

```sh
yay -R orca
yay -R brltty
```



## 测试

设置波特率

```sh
sudo stty -F /dev/ttyUSB0 115200
```

screen使用相同的波特率，保证数据传输正确

```sh
screen /dev/ttyUSB0 115200
# 如果没screen，安装
sudo pacman -S screen
```

可以向 `/dev/ttyUSB0` 发送信号：

```sh
sudo echo "Hello111" > /dev/ttyUSB0
```

这样你可以在另外screen的tty中看到发送的信息，如果想退出screen，使用`ctrl+a k`快捷键。
