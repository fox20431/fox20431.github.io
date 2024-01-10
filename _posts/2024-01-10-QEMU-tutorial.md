---
title: QEMU tutorial
date: 2024-01-10
---

# QEMU 教程

**QEMU 创建并启动虚拟机**

下载ubuntu镜像并重命名为 `ubuntu.iso` 。

有 `qemu` 已经足够让我们启动虚拟机：

```sh
# 创建存储的介质
qemu-img create -f qcow2 ubuntu.qcow2 20G

# 指定镜像去安装
qemu-system-x86_64 \
    -machine type=q35,accel=hvf \
    -smp 2 \
    -cpu host \
    -hda ubuntu.qcow2 \
    -cdrom ./ubuntu.iso \
    -m 4G

# 启动虚拟机
# 由于使用了MacOS的Hypervisor.framework
# 需要sudo命令
sudo qemu-system-x86_64 \
  -machine type=q35,accel=hvf \
  -M accel=hvf \
  -cpu host \
  -smp 6 \
  -m 16G \
  -hda ~/vm/ubuntu.qcow2 \
  -vga virtio \
  -usb \
  -device usb-tablet \
  -display default,show-cursor=on \
  -nic vmnet-bridged,ifname=en0
```

QEMU参考文档：

- [QEMU官方文档](https://www.qemu.org/docs/master/)
- [QEMU WiKi](https://wiki.qemu.org)：我建议作为官方文档的补充
- [QEMU - Arch WiKi](https://wiki.archlinux.org/title/QEMU)
- [Domain XML format](https://libvirt.org/formatdomain.html)
- [QEMU command-line passthrough](https://libvirt.org/kbase/qemu-passthrough-security.html)
- [Libvirt Hypervisor](https://libvirt.org/drvqemu.html)：众所周知 Hypervisor 是运行和管理多个虚拟机的程序
- [QEMU Switch To Libvirt](https://wiki.libvirt.org/page/QEMUSwitchToLibvirt)：将QEMU转换成Libvirt

**关于在macos上创建网络桥接**

[qemu在MacOS的桥接](https://taoshu.in/unix/qemu-bridge-on-macos.html)

如果想让外界直接访问虚拟机，最简单的办法是使用桥接。目前网上多数是利用tap模式。macos不支持tap设备需要依赖第三方tuntap，因为新的macos已经启用的内核拓展，tuntap不再继续开发。

macos 从 10.10 Yosemite 开始提供 Hypervisor.framework，这是 BSD 内核原生的虚拟化框架，有点类似 Linux 的 KVM 模块。Hypervisor.framework 支持为虚拟机创建桥接网络。qeum 大约在 2021 年年底开始支持 Hypervisor.framework。

```sh
sudo qemu-system-x86_64 path/to/disk \
    -M accel=hvf \
    -cpu host -smp cpus=8 -m 256 \
    -nic vmnet-bridged,ifname=en0
```

qemu在mac下体验不好，还是要linux下使用。

**存储**

有的磁盘是预先分配的，即分配多大就占用多少系统空间

有的磁盘是动态分配的，虽然有指定大小，但实际占用根据真正使用的大小来决定

前者省心但占用多，后者占用少但要考虑系统空间问题。


这好像叫做`sparse`，不太懂，顺便找到了一个命令可以将预先分配的转为动态分配的命令：

```sh
qemu-img convert -f qcow2 -O qcow2 -o preallocation=off vol.qcow2 newdisk.qcow2
```

**虚拟网络**

参考：https://linuxconfig.org/configuring-virtual-network-interfaces-in-linux