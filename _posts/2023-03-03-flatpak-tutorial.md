---
title: flatpak tutorial
date: 2023-03-03
---

# flatpak 教程



`Flatpak` 安装的应用运行在 runtime 中，字体路径如下：

`/var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/23.08/active/files/share/fonts/`

使用如下命令可以让 `typora ` 应用遵守系统字体设置：

```sh
sudo flatpak override --filesystem=xdg-config/fontconfig
```

但是对 spotify ，考虑是 spotify 不适配 wayland 的原因。



## flatseal

安装 `flatseal` 可以查看应用的权限。
