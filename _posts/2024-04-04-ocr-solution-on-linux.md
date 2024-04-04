---
title: ocr solution on linux
date: 2024-04-04
---

# Linux 平台下 OCR 解决方案

## 软件要求

- flameshot（截图工具）
- tesseract（OCR工具）
- wl-clipboard（wayland的剪贴板工具）*如果桌面运行在x环境，选择`xsel`*

## 编写脚本

```sh
#!/bin/bash

# prerequiste thoes app: `flameshot`, `tesseract`, `wl-clipboard`.

# Create a temporary directory
TMPDIR=$(mktemp -d)

# Take a screenshot of a selected area and save it as screenshot.png in the temporary directory
flameshot gui -p $TMPDIR/screenshot.png

# Process the screenshot with Tesseract and save the result to a text file in the temporary directory
tesseract $TMPDIR/screenshot.png $TMPDIR/output

# Copy the result to the clipboard (Wayland)
# ignore all non-ASCII characters
cat $TMPDIR/output.txt |
    tr -cd '\11\12\15\40-\176' | grep . | perl -pe 'chomp if eof' |
    wl-copy

# Optionally, remove the temporary directory when done
rm -r $TMPDIR
```

## 设置快捷键

根据使用的桌面发行版来绑定快捷键运行脚本。