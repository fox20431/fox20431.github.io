---
title: redirect obs to wemeet on linux 
---



# 转发OBS到腾讯会议



由于腾讯会与不支持wayland的屏幕共享协议，于是有了个曲线救国的方式，就是利用OBS将屏幕做虚拟摄像机。

**视频**

这个比较简单，打开 OBS 同时开启 `Virtual Camera`，自动创建名为 `OBS Vitrual Camera` 的虚拟摄像头。

**音频**

使用 `pipewire` ，与 `palseaudio` 会有冲突，需卸载后者：

```sh
sudo pacman -S pipewire pipewire-alsa pipewire-jack pipewire-pulse
```

创建名为 `wemeet` 的虚拟麦克风，将桌面音频作为麦克风的输入：

```sh
pactl load-module module-remap-source source_name=weemeet source_properties=device.description=wemeet master=$(pactl get-default-sink).monitor
```

不用的时候可以卸载：

```
pactl unload-module module-remap-source
```



