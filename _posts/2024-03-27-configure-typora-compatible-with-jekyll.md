---
title: configure typora compatible with jekyll
date: 2024-03-27
typora-root-url: ../
typora-copy-images-to: ../assets/images/
---

# 配置 Typora 用于兼容 Jekyll

参考教程：[Typora and Jekyll](https://jay.gooby.org/2021/01/17/typora-and-jekyll)

`Typora` 支持 `Front Matter` ，详细请查看文档：[YAML Front Matter - Typora](https://support.typora.io/YAML/)。这是 Typora 兼容 Jekyll 重要桥梁。

## 通用 Front Matter 元数据

值得庆幸的是 `Typora` 支持的 `Front Matter` 与 `Jekyll` 规范的 `Font Matter` 在通用的元数据（meta data）上有很好的兼容。比如 `Jekyll` 支持 `title` 和 `date` 元数据有很好的支持，用于显示 `post` 的名称和时间，`typora` 也对 `title` 和 `date` 有很好的支持，用于在未命名的文件保存时自动生成文件名。

## Typora 特有 Front Matter 元数据

对于向帖子（博客）中引入资源文件（以下都以图片为例），Jekyll 引入方式与常规的相对/绝对路径引入方式不同（毕竟在服务器上）。

`jekyll` 的帖子位于 `<workspace_root>/_post` ，而图片资源一般放在 `<workspace_root>/assets/images` 中，如果想要向帖子中引入图片，必须使用绝对路径 `/assets/images/xxx` 。但是 Typora 默认查找 `/assets/images/xxx` 会从文件系统的根目录查找，当然无法找到。

这时候需要两个 `Front Matter` 使得 Typora 来兼容 Jekyll。

1. `typora-root-url` 元数据，用于配置 Typora 检索资源文件对应的位置。对于 `jekyll` 项目的目录，笔记位于 `<workspace_root>/_post` ，而图片资源一般放在 `<workspace_root>/asset/images` 中，因此我们只需要在每个文件的 `front_matter` 中设置 `typora-root-url: ../` 就能让typora正确的找到图片位置；
2. `typora-copy-images-to` 单独设置图片存放位置，对于兼容 jeykll 可以设置为 `typora-copy-images-to: ../assets/images/`。

对于图片位置我们也可以全局设置指定（但不推荐）：

![image-20240327181042472](/assets/images/typora-image-setting.png)
