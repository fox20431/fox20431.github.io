---
title: "WSL 挂载其他盘符"
excerpt: "Windows 能处理的文件系统有限，当遇到 `ext4` 、`btrfs` 等 Windows 系统无法处理的文件系统可以使用 WSL 进行挂载使用。"
---

# WSL Mount

Windows 无法处理 ext4 、 btrfs 等文件系统，但有时候有访问这样的文件系统的需求，WSL 作为子系统有着 Linux 的软件生态可以访问。

## Steps

1. 查看显示要挂载的设备ID

```ps1
wmic diskdrive list brief
```

输入:

```
Caption                     DeviceID            Model                       Partitions  Size
Samsung SSD 980 PRO 1TB     \\.\PHYSICALDRIVE0  Samsung SSD 980 PRO 1TB     2           1000202273280
SAMSUNG MZVL2512HCJQ-00BL2  \\.\PHYSICALDRIVE1  SAMSUNG MZVL2512HCJQ-00BL2  2           512105932800
```

2. 挂载硬盘到 WSL

管理员权限执行下述命令：

```ps1
wsl --mount \\.\PHYSICALDRIVE1 --partition 1
```

操作成功的输出：

```
The disk was successfully mounted as '/mnt/wsl/PHYSICALDRIVE1p1'.
```

不管你挂载的是哪个分区，最终 WSL 会识别到这块硬盘。

3. 挂载文件系统

定位要挂载的硬盘：

```sh
sudo parted -l
```

命令行挂载：

```sh
sudo mount /dev/device /mount/path
```

对于 LVM ，以 Ubuntu 的 WSL 为例：

安装 LVM 工具：

```sh
sudo apt-get install lvm2
```

扫描物理卷：

```sh
sudo pvscan
```

扫描卷组：

```sh
sudo vgscan
```

激活卷组：

```sh
sudo vgchange -ay
```

挂载：

```sh
mount /dev/mapper/vg-lvname /mount/path
```