---
title: xdg-standard
date: 2024-02-08
---

# XDG Standard

## `.desktop` file

- `/usr/share/applications/`
- `~/.local/share/applications/`

为Gnome创建应用桌面快捷方式图标。

系统默认路径`/usr/share/applications`；用户默认路径`~/.local/share/applications`。


格式：

```desktop
[Desktop Entry]
Name=My App
Exec=/path/to/myapp
Icon=/path/to/myapp/icon.png
Terminal=false
Type=Application
Categories=Utility;
```

对应的icon可以指定确定的位置，也可以选择`/usr/share/icons`，也可以选择用户的`~/.local/share/icons`。

或者 `/usr/share/pixmaps` 。

## autostart

- `/etc/xdg/autostart/`
- `~/.config/autostart`

## `mime`(Multipurpose Internet Mail Extensions)

- `/etc/mime.types`
- `~/.config/mimeapps.list`