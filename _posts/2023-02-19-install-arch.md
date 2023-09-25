# ArchLinux Installation

## 准备阶段

1. 准备一个U盘

2. 下载镜像

   下载地址： 

   - [清华镜像站](https://mirrors.tuna.tsinghua.edu.cn/) 
   - [科大镜像站][http://mirrors.ustc.edu.cn/ ]

3. 下载烧录工具

   - Windows环境推荐使用**USBWriter**应用

   - Linux环境推荐使用**dd**命令

   - Mac环境也推荐使用**dd**命令


4. 使用烧录工具将镜像烧入到U盘

5. 重启电脑并选择U盘作为开机启动项

## 安装基本系统

### 硬盘处理

Forwords:

由于硬件类型和分区方式的多样性，非通用命令不在本文记录

*常用分区命令：parted、fdisk、cfdisk*

#### 1.引导系统与硬盘分区表的关系

MBR (Master Boot Record) 和 GPT (GUID Partition Table) 是用于存储磁盘分区信息的两种不同的格式。

- MBR是老式的磁盘分区格式，每个磁盘最多只能有4个分区，并且每个分区的最大大小为2 TB。
- GPT是新型的磁盘分区格式，可以有超过4个分区，并且每个分区的大小没有限制。此外，GPT还具有更强的容错性，因为它在磁盘上有多份备份。

在启动系统时，BIOS 或 UEFI 用于加载操作系统。

- 如果系统使用BIOS，则MBR是首选的磁盘分区格式。
- 如果系统使用UEFI，则GPT是首选的磁盘分区格式，因为UEFI支持大于2 TB的磁盘分区。

因此，MBR和GPT是磁盘分区格式，而BIOS和UEFI是用于加载操作系统的引导系统。系统的硬件类型决定了应该使用哪种引导系统，而磁盘分区格式则取决于系统的引导系统。

下面将以UEFI举例，UEFI要求引导的分区格式为vfat，普通的BIOS没有这个要求。

#### 2.选择硬盘分区方式

两种方式：  

1. 普通分区  
2. 逻辑卷分区

普通分区确定大小后不能拉伸缩小容量，逻辑卷可以 ；普通分区操作简单，逻辑卷相反

#### 3.规划硬盘分区方案

|分区类型|分区大小|是否必要|
|-|-|-|
|efi分区|推荐300M|必要|
|swap分区|推荐内存的1-2倍|非必要|
|家目录分区|不定|非必要|
|根分区|不定|必要|

efi分区：用于安装引导程序来引导电脑进入系统。

swap分区：与windows虚拟内存原理类似，当内存的使用超出实际内存大小的时候swap分区用来充当内存。此外，在休眠状态下内存里的内容转移到swap分区中，继而内存停止工作，从而节省电量；当解除休眠时，内存就会从swap分区中读取数据，从而使电脑正常运行。

家目录分区：非root用户在平时活动根据地，用来保存用户的各种信息，比如各个应用的配置文件，下载内容，创建内容等等。

根目录分区：储存除挂载(主要指efi分区和swap分区)和swap分区外所有数据。

> Tips: 如果你是双硬盘可以选择一整张硬盘作为家目录分区，避免由于物理或者软件原因导致自己家目录受到牵连。目前市面上笔记本多为一固态一机械，由于机械的读写慢寿命长，所以推荐机械硬盘作为家目录分区，这样就可以在不影响系统速度的情况下将个人数据保存的更长久，同理固态的读写快寿命短，推荐用来安装系统。

#### 4.格式化分区

efi分区文件系统：exfat

swap分区文件系统：swap

家目录/根目录分区文件系统：ext4

> efi格式化建议选择exfat，也可以选择fat16和fat32。fat16容量最大支持2GB，fat32最大只能拷贝4GB，exfat没有他们的缺点。

```sh
mkfs.vfat /dev/efi分区
mkswap /dev/swap分区
# 开启swap分区
swapon /dev/swap分区
mkfs.ext4 /dev/根目录分区
mkfs.ext4 /dev/家目录分区
```

### 挂载处理

挂载是对分区内容进行操作

```sh
mount /dev/根目录分区 /mnt
mkdir -p /mnt/boot/efi
mount /dev/efi分区 /mnt/boot/efi
# 如果有家目录再执行下列命令
mkdir /mnt/home
mount /dev/家目录分区 /mnt/home
```

### 链接网络

通过下述命令进入 `iw` 交互界面：

```sh
iwctl
```

在交互终端中执行下述操作连接网络：

```sh
# use the 
station <net_intface_name> get-networks
station <net_interface_name> connect <ap_name>
```

#### 修改镜像源

包管理获取软件的镜像站地址全部储存在`/etc/pacman.d/mirrorlist`  
包管理会按照文件内镜像站的顺序作为优先级获取软件  
当最前的镜像站连接超时后自动跳转第二个，以此递推

为了确保网络畅通，通过编辑方式将中国的镜像站放到最前面

*推荐的镜像站：163、stinghua*

```
# 编辑文件
vim /etc/pacman.d/mirrorlist
# 具体操作略
```

### 安装系统

通过pacstrap给挂载的分区安装系统

```sh
# 安装系统
pacstrap /mnt base base-devel linux linux-headers linux-docs linux-firmware

# 微码（微码也不一定需要安装，我的电脑安装完后反而G302无限鼠标不能用了）
# 如果CPU是intel，执行下载操作
pacstrap /mnt intel-ucode
# 如果CPU是AMD，执行下载操作
pacstrap /mnt amd-ucode
```

微码是嵌入在中央处理器（CPU）内部的一种固件，它可以对 CPU 的操作进行微小的修改，以修复硬件错误、提供新的功能、改进性能或者增强安全性。

当 Intel 发现 CPU 中存在一些问题、漏洞或者需要改进的地方时，他们可以通过更新微码来解决这些问题，而无需对硬件进行物理更改。这可以通过操作系统或主板固件的更新来实现。

- base：包含最基础工具
- base-devel：包含最基础的开发工具
- linux：linux内核，长期支持版本的为linux-lts
- linux-headers：linux内核的头文件，长期支持版本的为linux-lts-headers
- linux-docs：linux的说明文档，长期支持版本的为linux-lts-docs
- linux-firmware：对一些硬件的支持

### 创建fstab

fstab作用：开机的时候告诉系统挂载的分区、挂载点、挂载格式、挂载选项等

```sh
# 在已安装内的系统内创建fstab
genfstab /mnt >> /mnt/etc/fstab
# 根据内容检查fstab正误
cat /mnt/etc/fstab
```

### 进入系统并执行必要操作

```sh
# 进入新装的系统
arch-chroot /mnt
# 设置root密码
passwd
# 安装编辑器
pacman -S vim
```

如果你采用lvm分区需要执行额外操作

- 安装lvm2
- 编辑`mkinitpio.conf`，在`HOOKS`所在行加入`lvm2`
- 使修改配置文件生效

当grub安装在lvm中，默认的grub配置开机无影响，当手动修改`/etc/default/grub`配置使grub记住选项会无法生效并输出错误（Error: diskfilter writes are not supported）。

```sh
# 安装lvm2
pacman -S lvm2
# 修改mkinipio.conf
# HOOKS所在行添加 `lvm2`
vim /etc/mkinitcpio.conf
# 是配置文件生效
mkinitpio -p linux
```

### 语言设置

1. 生成locale

   locale作用：

   显示本地化的文字、货币、时间、日期、特殊字符等包含地域属性的内容

    ```
    # 修改语言的配置文件
    # 取消`en_US.UTF-8`的注释
    vim /etc/locale.gen
    # 生成locale
    locale-gen
    ```

2. 设置locale.conf

    locale.conf作用:设置系统语言

    locale.conf会在系统启动的早期被`systemd`读取

    ```sh
    # 编辑locale.conf
    vim /etc/locale.conf:
    # 设置英文需添加：LANG=en_US.UTF-8
    # 设置中文需添加：LANG=zh_CN.UTF-8
    # 其他语言以类似
    ```

3. 安装字体

    缺失对应字体会出现方块字情况，需要安装相应的语言字体。

    对于中文字体目前我只推荐Adobe公司开发的 `adobe-source-han-sans-otc-fonts`。

    Google 公司开发的 `noto` 中文系列的字体中的某些字体形状怪异或者缺失，不推荐；但是非中文系列的 `noto-fonts` 还是值得安装的，此外 `nerd` 系列拥有更全面的字体，因此安装 `ttf-noto-nerd` ；以及 `noto-fonts-emoji` 是为了提供 emoji 支持需要安装的。
    
    综上，安装如下字体：
    
    ```sh
    sudo pacman -S adobe-source-han-sans-otc-fonts noto-fonts-emoji ttf-noto-nerd
    ```

### 时间设置

Arch Linux以BIOS的时间为世界统一时间（UTC）。

中国在东八区，即UTC时间加8个小时，将对应配置文件链接到对应位置即可将时间设置成东八区。

```
# 设置时区为东八区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
```

### 网络设置

若想配合图形界面，建议安装 `NetworkManager`。

```sh
# 方案一
# 安装网络组件
pacman -S networkmanager dhcpcd
# 启动无线网络
systemctl enable NetworkManager
# 启动有线网络
systemctl enable dhcpcd
```

非图形界面安装 `iwd` 占用更小。

```sh
# 最小化安装
pacman -S iwd dhcpcd
# 启动无线网络
systemctl enable iwd
# 启动有线网络
systemctl enable dhcpcd
```

### 安装引导

```sh
# 安装引导所需包
pacman -S grub efibootmgr
# 安装grub
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch
# 使配置文件生效
grub-mkconfig -o /boot/grub/grub.cfg
```

Tips:

`/etc/default/grub` 为 grub 配置文件  

修改配置文件后，执行下述命令进行更新：

```sh
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

### 新建用户

root作为超级用户，在平时使用会存在风险

需要新建用户，然后赋予root的权限

```sh
# 创建test用户生成家目录并加入wheel组
useradd -m -G wheel test
# 设置test的密码
passwd test
# 允许wheel组获取权限
vim /etc/sudoers
# 取消wheel的其中一个注释
```


### 退出系统并结束所有流程

```sh
# 退出系统
exit
# 解除挂载
umount -R /mnt
# 重启电脑
reboot
```

*恭喜你完成所有操作，记得拔出U盘*

## 安装图形界面

在安装图形界面之前，我们应该了解图形界面的窗口协议目前主流为Xorg与Wayland。

Xorg由于设计原因逐渐被Wayland替代，目前KDE和GTK等都默认选择Wayland。

下述均以Gnome为例讲述，KDE也是很好的图形界面，但Gnome更受其他厂商推崇。

### 安装 Gnome

```sh
sudo pacman -S gnome gnome-tweaks
systemctl enable gdm
```

### 组件配置

**网络**

确保 `networkmanager` 包安装并且被 `systemd` 启用并运行。

**音量**

安装声音相关的固件，如果不安装可能导致无法正常播放音频。


```sh
sudo pacman -S sof-firmware alsa-firmware alsa-utils pulseaudio pulseaudio-alsa pulseaudio-bluetooth
# sof is short for "sound open firmware
```

**蓝牙**

```sh
# 安装蓝牙组件
sudo pacman -S bluez
# 启用蓝牙服务
systemctl enable bluetooth
```

### 配置

`Tweaks` 中可以配置字体

- Interface Text：表示系统界面字体，选择 Source Han Sans SC Regular
- Documentation Text：选择 Source Han Sans SC Regular
- Monospace Text：等宽字体，一般会影响终端字体，选择 FiraMono Nerd Font Regular（任何等宽字体）
- Legency Window Titles：选择 Source Han Sans SC Regular

### 注意事项

- GNOME的三指操作需要在Wayland下才能做到

  终端输入`echo $XDG_SESSION_TYPE`查看当前使用的桌面协议。

  `x11`为xorg，`wayland`为wayland。

- 开机无法检索到wayland，必须注销重新登录才能有wayland选项，但gnome默认使用的是wayland。

  原因是显卡驱动加载满，userspace速度太快导致的。修改`/etc/mkinitio.conf`中的`MODULES=(xxx)`，我的是intel核显所以改为`MODUDLES=(i915)`。

  参考：https://bbs.archlinuxcn.org/viewtopic.php?id=11275 & https://wiki.archlinux.org/title/Kernel_mode_setting#Early_KMS_start

## 更多



### YAY

`yay` 涵盖 `pacman` 仓库缺少的AUR（Arch User Repo，里面有闭源的软件）。

我把这一项放在最前面考虑到有些包需要借助 `yay` 安装。

安装

```sh
pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
```

详情见[yay仓库主页](https://github.com/Jguer/yay)

### emoji

安装 emoji picker

```sh
yay -S emote
```

### 输入法

如果你安装 `Gnome` 的话，由于 `Gnome` 集成了 `ibus` ，所以推荐使用 `ibus` 输入法。

具体 ibus 的什么输入法，这里我推荐 `ibus-rime`，因为好用。

如何安装：

```sh
sudo pacman -S ibus-rime
```

默认是繁体字，可以使用 `ctrl - \`` 设置简体中文。

同时可以使用修改 `~/.config/ibus/rime/build/ibus_rime.yaml`

```yaml
style:
  horizontal: true
```

将输入法设置横向。

Rime 输入法快捷键 `ctrl - grave`   与 Visual Studio Code 冲突，在 ``~/.config/ibus/rime/build/default.yaml``  文件中注释该快捷键：

```yaml
switcher:
  abbreviate_options: true
  caption: "〔方案選單〕"
  fold_options: true
  hotkeys:
  	# - "Control+grave"
```

### 增加软件库

```sh
sudo vim /etc/pacman.conf
```
文件尾添加下面两行
```sh
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch
```

[multilib]为32位软件库，取消注释

```sh
sudo pacman -Syu
sudo pacman -S archlinuxcn-keyring
```

### 双系统

Windows & Linux

#### GRUB引导

```sh
sudo pacman -S os-prober
# 检测有无Windows EFI引导
$ sudo os-prober
/dev/nvme0n1p1@/EFI/Microsoft/Boot/bootmgfw.efi:Windows Boot Manager:Windows:efi
```

```sh
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=arch
grub-mkconfig -o /boot/grub/grub.cfg
```

#### 时区

Windows 以硬件时间为时间，Linux以硬件时间为UTC时间。

建议以Linux方案为主，修改Windows的注册表，将硬件时间设为UTC时间。

修改 Windows 的注册表的命令

```sh
Reg add HKLM\SYSTEM\CurrentControlSet\Control\TimeZoneInformation /v RealTimeIsUniversal /t REG_DWORD /d 1
```

### plocate

```sh
sudo pacman -S plocation
sudo updatedb
```

### Logitech Micr

罗技鼠标采用lightspeed传输技术，若想让Linux支持该功能需要安装：

```sh
sudo pacman -S libratbag
sudo systemctl enable ratbagd
sudo systemctl restart ratbagd
```

更多关于libratbag可见：https://github.com/libratbag/libratbag

更多可见：https://wiki.archlinux.org/title/Logitech_Unifying_Receiver

### Intel显卡

我之前一致认为intel显卡是最简单最不需要配置的显卡，直到入手了这台电脑。

阅读WiKi十分重要！！！https://wiki.archlinux.org/title/intel_graphics

我首先是将`i915`加入到`/etc/mkinitcpio.conf`的module中，然后还需要通过GRUB传参防止闪烁。

```
GRUB_CMDLINE_LINUX="i915.enable_psr=0"
```

关于intel的PSR：https://www.intel.com/content/www/us/en/support/articles/000057194/graphics.html

PSR is short for panel self refresh.

面板自动刷新，可以降低系统功耗。

### Docker

```sh
pacman -S docker
systemctl enable docker
systemctl start docker
usermod -a -G docker <username>
reboot
```

### OBS

OBS在x11上表现并没有太大问题，但在wayland上又有一些问题。

首先安装包：

```sh
sudo pacman -S gst-plugin-pipewire
sudo pacman -S obs-studio
```

首先obs通过`PipeWire`捕获屏幕，所以需要安装pipewire。

然后OBS是基于QT开发的软件，如果要让其支持wayland需要安装qt相关的包。

最后配置环境变量。

### Fonts

当对应编码的字体不存在时，会出现“方块字”的现象。

解决这个问题的方法就是安装上对应确实的字体。

可以选择 `wqy-zenhei` 自发开源组织的字体（貌似不再维护），推荐使用选 google 的开源字体 `noto-fonts` 系列的字体（有大厂背书），同时 Adobe 也开源了 `souce-han` 系列字体。关于代码相关的字体，我推荐 `fira` 字体。

在不安装 `noto-fonts` 包会出现很多特殊字符缺失，所以这个算是必装的吧。

```sh
sudo pacman -S noto-fonts
# 其他的通过关键字搜索
```

### PDF阅读器

Pdf阅读器我推荐两个：okular、evince。

这两个都是开源的，但okular是KDE平台的，evince是gnome平台的。

evince涵盖在gnome集合包中，安装gnome时自动安装evince。

```sh
sudo pacman -S evince
```

### 多屏幕显示问题及暂时解决方案

When you use multiple monitors in wayland gnome environment with different scale, you will find scaling problems which make you have to use single monitor.

The problem:

- The cursor scales abnormally in some applications, for example `telegram`
- The application scaling is not adapt the other minotor scale, for example `chrome`, `visual studio code`, other `electron application`, and `firefox`
- Even the gnome has the second problem

Althought the single monitors also has the part of problems, but it not effect the daily use.

To solve the problem to use the idle monitor, we should enable the experimental fractional scaling feature:

```sh
gsettings set org.gnome.mutter experimental-features "['scale-monitor-framebuffer']"
```

ref: https://wiki.archlinux.org/title/HiDPI#Wayland

Now you will find the almost old application which run on x11 well run well on wayland.

But it still have some problems, such as `chrome`, `visual studio code` and so on is blur...

Luckily, we know the `chrome` and `visual studio code` can pass the parameter:

```sh
--ozone-platform=wayland
```

So, we just need add the `alias` into `~/.bashrc` and add options into `xxx.desktop`.

But i will find the ibus chinese not working when open it.

Unluckily, I just know the `chrome` which allow `--gtk-version=4` parameter to make ibus chinese well.

`visual studio code` cannot do it, so I use the English to write the part.

I will wait update and it's fine.

==== update ====

我仍然选择单个屏幕，因为多个屏幕很多软件显示很模糊。

然后我整理了下思绪...

下面是对适配 `gtk` 的应用的缩放：

```sh
gsettings set org.gnome.desktop.interface scaling-factor 2
```

下面是针对 `x11` 的应用的缩放，比如 `Visual Studio Code` 等：

```sh
gsettings set org.gnome.settings-daemon.plugins.xsettings overrides "[{'Gdk/WindowScalingFactor', <2>}]"
```

目前属于 `x11` 到 `wayland` 过渡的镇痛期。

### 安装pipewire

https://blog.ryey.icu/replace-pulseaudio-with-pipewire.html


```sh
pacman -S pipewire pipewire-pulse wireplumber
```

```sh
systemctl --user enable pipewire pipewire-pulse wireplumber
systemctl --user start pipewire pipewire-pulse wireplumber
```

安装 `pipewire` 会导致 `MPV` 没声音，似乎是 `MPV` 对其不兼容，但还是选择这个作为播放音频接口。

解决方案：https://wiki.archlinux.org/title/mpv#Unable_to_play_audio_if_PipeWire_is_masked

将 `--ao=alsa` 写入 `mpv.conf` 。

### 耳机有电流声（bazzing）

测试同一耳机同台电脑Windows平台没有电流声，猜测是驱动问题。

顺便钻研了下 `alsa` 详细配置：

```sh
alsamixer
```

`F6` 将 `Mic Boos（Microphone Boost）` 是将麦克风的声音增强。

### 输入法漂移的问题

在 Linux Wayland Gnome 上发现 gnome 绑定生态的应用都会出现 ibus 飘逸的问题。

多次解决无果，尝试询问群友，原来是因为我多加了 `GTK_IM_MODULE` 环境变量，将这个删除后生效。

下面是群友原话：

> 这个东西是这样 你设置的话会走 ibus 的 gtk im module

> 不设置就是 gtk 的 wayland text input v3

> 我也不知道 gtk 上游在搞些啥。。。

> 但我知道 fedora 默认是不用 gtk im module 的（默认就走 text input v3

> 我测试的结果是 gtk4 确实比较适合 text input v3

> 虽然用 fcitx5 的话 不会错位

### 触摸板滚动速度问题

一般都是使用libinput，对于这种情况可以使用(libinput-config)[https://gitlab.com/warningnonpotablewater/libinput-config]，修改对应配置文件`/etc/libinput.conf`。

```sh
# 0.4倍速度
scroll-factor=0.4
```

### Office 安装

可以安装 `LibreOffice` 和 `WPS`，推荐 `LibreOffice` 。

安装微软相关的字体 `yay -S ttf-ms-fonts`。这个字体不是很全，像楷体、仿宋之类的字体依旧不存在。

解决方案也很简单粗暴，如 Windows 系统去`C:\Windows\Fonts`将所有字体下载下载，再将该目录完全拷贝下来，根据Linux中的`/etc/fonts/fonts.conf`的配置，默认用户`~/.fonts/`目录可以用于存放字体文件。将Windows的所有字体都拖入到这里。

利用 fontsconfig 工具刷新下缓存即可。

```sh
fc-cache -fv
```

### Gnome 插件推荐

- Hibernate Status Button
- Tray Icons: Reloaded