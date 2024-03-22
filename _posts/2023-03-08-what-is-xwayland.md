# XWayland

现在大趋势是 XOrg —> Wayland。

而Wayland为了能兼容Xorg进行过度，实现了XWayland在Wayland平台上的的XOrg服务，用于适配基于X开发的应用。

如果判断当前应用是原生运行在Wayland还是运行在XWayland上的？

方法一：

`xwininfo` 命令选择窗口，看打印信息；

方法二：

`xeyes` 将鼠标移动到要判断的窗口，如果 `xeyes` 有反应就是运行在 XWayland ，没反应就是原生。

方法三：

`xlsclients` list client applications running on a display