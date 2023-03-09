# Gnome Desktop Shortcut

为Gnome创建应用桌面快捷方式图标。

系统默认路径`/usr/share/applications`；用户默认路径`~/.local/share/applications`。


格式

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