---
title: troubles and solutions in linux
date: 2024-02-24
---

# Linux 平台遇到的问题以及解决方案

## Intel显卡

我之前一致认为intel显卡是最简单最不需要配置的显卡，直到入手了这台电脑。

阅读WiKi十分重要！！！https://wiki.archlinux.org/title/intel_graphics

我首先是将`i915`加入到`/etc/mkinitcpio.conf`的module中，然后还需要通过GRUB传参防止闪烁。

```
GRUB_CMDLINE_LINUX="i915.enable_psr=0"
```

关于intel的PSR：https://www.intel.com/content/www/us/en/support/articles/000057194/graphics.html

PSR is short for panel self refresh.

面板自动刷新，可以降低系统功耗。

## 输入法漂移的问题

在 Linux Wayland Gnome 上发现 gnome 绑定生态的应用都会出现 ibus 飘逸的问题。

多次解决无果，尝试询问群友，原来是因为我多加了 `GTK_IM_MODULE` 环境变量，将这个删除后生效。

## Xwayland在缩放情况下滚动速度问题

目前没发现的好的解决方案，但是chrome可以针对设置（**不推荐，会导致鼠标情况下滚轮速度非常慢**）

Chrome地址栏输入：chrome://flags/

搜索 `Windows Scrolling Personality` ，将其设置为Enable。

但对于VSCode这类的不提供设置的暂时没好的解决方案。

## 多模键盘Function按键失效问题

已知出现问题的键盘有：Keychon K2、腹灵MK870。

**在Linux上，Keychon K2不会将任何F1-F12功能键映射为实际的F键，而是默认将它们视为多媒体键。 Fn+F1-12的组合也不会起作用**

1. 将侧边模式转换键拨至Windows,（如果你习惯使用Mac模式那么应该不会遇到这个问题）
2. 长按Fn + X + L将F1-F12优先映射到功能键而不是媒体键
3. 在终端输入

```bash
echo 0 | sudo tee /sys/module/hid_apple/parameters/fnmode
```

**此时Keychron键盘应该已经可以正常使用了**

接下来可以将这项设置写入配置文件，否则每次重启你都要重新执行一遍

```bash
echo "options hid_apple fnmode=0" | sudo tee -a /etc/modprobe.d/hid_apple.conf
```

执行下面这条命令并重启

```bash
sudo update-initramfs -u    // Ubuntu
mkinitcpio -P               // ArchLinux
genkernel initramfs         // gentoo
dracut --hostonly -f --kver=<kernel-version> // 待测试，已知没有 '--hostonly' 参数不生效
```

原文链接：[KEYCHRON LINUX FUNCTION KEYS](https://mikeshade.com/posts/keychron-linux-function-keys/)

### Idea下ibus候选框错位问题

更新idea运行的JBR版本

### 字体不统一

一般是应用 `font-family` 设置中按照优先级选择到了指定字体，但是该字体包含的文字不全就导致了字体显示不统一。

解决方案删除那些包含不全面的字体，这里**不推荐在Linux下使用微软移植过来的字体**，因为不可信因素太多。