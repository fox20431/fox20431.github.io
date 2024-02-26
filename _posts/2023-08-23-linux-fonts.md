---
title: Linux Fonts
date: 2023-08-23
---

# Linux Fonts


## 安装字体

安装开源字体

- 思源汉（Source Han）
- Noto 以及 Noto emoji

```sh
# arch linux
sudo pacman -S adobe-source-han-sans-otc-fonts noto-fonts-cjk 
```

## 字体管理

查看字体

```sh
# 产看中文的的字体列表
fc-list :lang=zh
fc-list :file=/usr/share/fonts/adobe-source-han-sans/SourceHanSans.ttc
fc-list :family
```

更新字体缓存

```sh
# 更新系统字体缓存
sudo fc-cache -f -v
```

## 字体配置

*配置用户手册`/usr/share/doc/fontconfig/fontconfig-user.html`*

有两处配置字体的配置文件：

- 系统的配置，**不推荐修改**：`/etc/fonts/fonts.conf`
- 用户的配置：`~/.config/fontconfig/fonts.conf`

### 个人配置推荐

`~/.config/fontconfig/fonts.conf`

**确保下属字体存在或者名字正确，使用 `fc-lust` 查看**

```xml
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "urn:fontconfig:fonts.dtd">
<fontconfig>
  	<alias>
	    <family>sans-serif</family>
	    <prefer>
		    <family>Source Han Sans SC</family>
	    </prefer>
    </alias>
  	<alias>
	    <family>serif</family>
	    <prefer>
		    <family>Noto Serif CJK SC</family>
	    </prefer>
    </alias>
    <alias>
	    <family>sans</family>
	    <prefer>
		    <family>Source Han Sans SC</family>
	    </prefer>
     </alias>
    <alias>
	    <family>monospace</family>
	    <prefer>
		    <family>Noto Sans Mono CJK SC</family>
	    </prefer>
    </alias>
</fontconfig>
```

Chrome和electron会遵守 `sans-serif` 设置字体，所以这个是需要设置的。

## 安装字体

### 通过包安装

nerd-fonts

```sh
sudo pacman -S nerd-fonts
```

### 手动安装

1. 将字体文件放在指定目录：

   - 系统目录：`/usr/share/fonts`
   - 用户目录：`~/.fonts/`

2. 刷新字体缓存

    ```sh
    # 更新系统字体缓存
    sudo fc-cache -f -v
    ```

在 archlinux 中同时存在了 `source han` 和 `win11` 的字体为中文字体提供支持，Chrome 在无指定 `font-family` 样式时出现中文多种字体混用情况。

