# Gentoo 遇到的问题以及解决方案

## 触摸板

参考：https://wiki.gentoo.org/wiki/Synaptics

## obs无法录屏

obs没有开启 pipewire use 标记

## ibus输入法连续触发的问题

安装 `app-i18n/im-chooser`

## VSCode 无法输入中文

删除 vscode desktop 文件`Exec`后面的参数：

```sh
sudo nvim /usr/share/applications/code.desktop
```

保留最后像这样：

```desktop
Exec=/usr/bin/vscode %F
```

