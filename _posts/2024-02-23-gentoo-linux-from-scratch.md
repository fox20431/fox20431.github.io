---
title: gentoo linux from scratch
date: 2024-02-23
---

# Gentoo 安装指南

在拥有 Arch Linux 安装经验后，其中很多部分比较容易理解。

[官方文档](https://wiki.gentoo.org/wiki/Handbook:AMD64)有很详尽的操作，这个教程作为概述以及补充。

## 烧录镜像

## 内核编译

### 手动编译

编译安装：

```sh
# config
make menuconfig
make -j12 && make modules_install
make install
```

引导安装：

```sh
cp ./arch/x86/boot/bzImage /efi/EFI/gentoo/bzImage.efi
# initramfs
dracut /efi/EFI/gentoo/initrd.cpio.gz --kver <kernel_version>
# 注册 efi （仅需第一次）
efibootmgr --create --disk /dev/nvme1n1 --label "Gentoo" --loader "\EFI\gentoo\bzImage.efi" -u 'root=UUID=97ffc05a-6098-4af9-9d61-a40f403fffca initrd=\EFI\gentoo\initrd.cpio.gz'
```

### install-kernel 安装（OpenRC）

需要依赖 `install-kernel` ，如果使用 OpenRC 请选择 [debian的内和安装方式](https://wiki.gentoo.org/wiki/Installkernel#Debian.27s_installkernel)，而不是 systemd 的方式。

关于配置，首先是 `/etc/kernel/install.conf` 中编辑：

```conf
layout=grub
initrd_generator=dracut
uki_generator=dracut
```

改配置针对 grub 配置。


同时修改对于 `installkernel` 的 `use` 关键字，删除 `systemd` ：

file: /etc/portage/package.use/installkernel

```use
sys-kernel/installkernel    -systemd dracut grub
```

这时候运行内核安装 `make install` 就能正确生成我们需要的 `vmlinuz`、`config`、`system.map` 等文件。

## Trouble

**MT7921蓝牙在Gentoo下不工作**

https://linux-hardware.org/?id=pci:14c3-7961-1a3b-4680

硬件问题
