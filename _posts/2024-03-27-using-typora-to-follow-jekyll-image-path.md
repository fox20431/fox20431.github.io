---
title: using typora to follow jekyll image path
date: 2024-03-27
typora-root-url: ../
---

# 遵守Jekyll图片路径的Typora的使用方法

参考教程：

https://jay.gooby.org/2021/01/17/typora-and-jekyll

首先说明，Typora 对 Jekyll 的 Front Matter 有很好的支持，比如当我们设置Markdown文件的 `front matter` 的 `title` 与 `date` 后，Typora会自动帮我们生成文件名。

同时Typora支持在 `Front Matter` 中设置 `typora-root-url` 参数，用于检索资源文件对应的位置，常见资源文件指的是图片。

对于 `jekyll` 项目的目录，笔记位于 `<workspace_root>/_post` ，而图片资源一般放在 `<workspace_root>/asset/images` 中，因此我们只需要在每个文件的 `front_matter` 中设置 `typora-root-url: ../` 就能让typora正确的找到图片位置。

Typora对于图片也有很好的支持，你可以参考我下面的Typora关于图片的配置。

![image-20240327181042472](/assets/images/typora-image-setting.png)

在正确设置 `font matter` 的 `typora-root-url: ../` 与  Typora 图片设置后，Typora会将粘贴的照片按照绝对路径的方式进行存储，这也是Jykell所支持的网站图片展示方式。 
