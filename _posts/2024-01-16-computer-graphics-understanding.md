---
title: computer graphics understanding
date: 2024-01-16
---

# 计算机图形学个人理解

显示器都遵守行业标准，相关关键字：VESA

当显示器接收到数据就会呈现该数据到显示器上，显示内容只和数据有关，和操作系统无关。

为了方便生成这些数据，在Linux平台上有工具包，比如GTK。

同时为了多应用协同工作就需要窗口管理器（桌面系统也包含窗口管理器的职责），比如Gnome。

Gnome使用GTK渲染图形，实现了Wayland协议，Wayland只是协议。

窗口管理器负责整体的图形渲染，但应用程序仍然需要自己负责创建和渲染自己的内容。应用程序通过监听窗口事件（大小等）来渲染Bitmap，交给管理器，管理器最终渲染整体的Bitmap，通过视频编码标准（压缩编码），比如H264、H265（HEVC）在HDMI上传递给显示器，显示器进行渲染。

因此应用程序可以拥有自己的渲染引擎，比如Chrome的Blink引擎。



所谓的Qt是图形框架，渲染引擎根据不同系统而不同：

1. **Windows：** 在 Windows 上，Qt 使用 Windows GDI 或者 Direct2D 作为底层图形系统。
2. **macOS：** 在 macOS 上，Qt 使用 Quartz 作为底层图形系统。
3. **Linux：** 在 Linux 上，Qt 可以使用 X11 或 Wayland，具体取决于系统的配置和支持。

比如Gnome下Qt使用GTK作为渲染引擎。



