---
title: gentoo package management tool tutorial
date: 2024-02-23
---


## emerge 教程

同步安装包信息：

```sh
emerge --sync
```

搜索

```sh
emerge -s <package_name>
emerge --search <package_name>
emerge --searchdesc <package_description>

# for example: 
# emerge -s '%^python$' # search using a regex
# emerge -s '@net-ftp' # search catagory
```

安装

```sh
emerge <pkg_name>
# with ask
emerge -a <pkg_name>
emerge --ask <pkg_name>
```

卸载：

```sh
emerge -C <pkg_name>
emerge --unmerge <pkg_name>
```

清理已安装软件包的构建残留物：

```sh
emerge -c
emerge --depclean
```

清理配置文件

```sh
sudo emerge --config sys-apps/portage  
```

全局更新：

```sh
emerge --ask --verbose --update --deep --newuse @world
# --deep: forces  emerge to consider the entire dependency tree of packages, instead of checking only the immediate dependencies of the packages.
# --newuse: tells emerge to include installed packages where USE flags have changed since compilation.

emerge -avuDN @world
```

## equery

查看安装的包：

```sh
equery list '*'
```

查看包的 `use` 选项和介绍：

```sh
equery uses <pkg_name>
```

查看包安装文件路径：

```sh
equery files <package_name>
```

查看文件归属的包：

```sh
equery belongs <file_path>
# for example
equery belongs /usr/share/applications/wpa_gui.desktop
```


## 相关配置文件

/etc/portage/make.conf

下载、编译、安装相关配置

/etc/portage/package.use/*

用于设置包的use选项，文件格式为

```
<pkg> <use_list>
```

/etc/portage/package.accept_keywords/*

有些包不适用于全平台，使用改配置文件可以接受制定关键字的包

文件格式为：

```
<pkg> <keywords>
```

