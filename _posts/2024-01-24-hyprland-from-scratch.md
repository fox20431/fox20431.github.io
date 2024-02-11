---
title: hyprland from scratch
date: 2024-01-24
---

# Hyprland From Scratch



https://cascade.moe/posts/hyprland-configure/





https://dev.to/devhypercoder/login-without-username-in-tty-28n2

First, you need to edit the `getty@tty1.service` file.

`sudo vim /etc/systemd/system/getty.target.wants/getty@tty1.service` (if you do not know how to use vim, use nano or any other editor)

Check for the line which starts with `ExecStart=` and replace it with `ExecStart=-/sbin/agetty -n -o <username> %I`
Make sure to change `<username>` to which ever username you want as the default.