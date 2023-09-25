---
title: dual system bluetooth pairing conflict
date: 2023-09-25
---

# 双系统蓝牙配备冲突

在Linux&Windows双系统的情况下，如果蓝牙在Windows系统中配对后，那么进入Linux需要重新配对，同时在Linux系统中配对后，进入Windows也许要重新配对。这样的话在切换操作系统时配对操作就是复杂且费时，以下是Windows与Linux共享蓝牙的解决方案。

1. 在Windows建立蓝牙连接（配对）；

2. 切换到Linux操作系统，建立蓝牙连接（配对）；

3. 获取Ubuntu下的蓝牙配对的`linkkey`

   获取方式如下，首先进入到 `/var/lib/bluetooth` 目录，该目录下会显示你本机电脑所有蓝牙的MAC地址，选择已经建立好配置的MAC地址目录并进入；进入后会显示所有已经配对好的蓝牙设的MAC地址，同理选择与电脑配对的设备的MAC地址；该目录下会包含 `info` 文件，使用 `cat info` 获取设备的详细信息，其中包含 `[LinkKey]` 模块，将其中的 `key` 的值复制。

4. 切换到Windows操作系统，安装 [PSTools](https://technet.microsoft.com/en-us/sysinternals/bb897553) 用于修改受保护的注册表信息，然后执行 `PsExec.exe -s -i regedit` 打开注册表，找到 `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\BTHPORT\Parameters\Keys\`，里面包含了电脑蓝牙的MAC，找到配对蓝牙设备的蓝牙MAC在其中的连接的值改为LinkKey。