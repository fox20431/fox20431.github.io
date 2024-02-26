---
title: gentoo linux from scratch
date: 2024-02-23
---

# Gentoo 安装指南

在拥有 Arch Linux 安装经验后，其中很多部分比较容易理解。

[官方文档](https://wiki.gentoo.org/wiki/Handbook:AMD64)有很详尽的操作，这个教程作为概述以及补充。

## 烧录镜像



## 关于手动编译内核

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

