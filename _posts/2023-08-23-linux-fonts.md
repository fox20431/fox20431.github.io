---
title: linux fonts
date: 2023-08-23
---

# Linux fonts

Linux 系统的字体配置：/etc/fonts/fonts.conf

常见命令：

```sh
fc-cache -f -v

fc-list :lang=zh
fc-list :file=/usr/share/fonts/adobe-source-han-sans/SourceHanSans.ttc
fc-list :family
```

在 archlinux 中同时存在了 `source han` 和 `win11` 的字体为中文字体提供支持，Chrome 在无指定 `font-family` 样式时出现中文多种字体混用情况。

通过元素属性发现默认使用了 `Times New Roman` 字体，该字体库没中文字体，所以对于中文字体还会使用其他的字体库，所以通过询问ChatGPT得知 Chrome 默认使用无衬线字体，因此决定设置无衬线字体的 `font-family` ，考虑到一般情况用户配置的优先级会高于系统配置，所以就在 `~/.config/fontconfig/fonts.conf` 用户目录下添加了规则：


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
		    <family>Source Han Sans SC</family>
	    </prefer>
     </alias>
    <alias>
	    <family>monospace</family>
	    <prefer>
		    <family>FiraMono Nerd Font Mono</family>
	    </prefer>
    </alias>
</fontconfig>

```