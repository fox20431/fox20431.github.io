---
title: default application of linux
date: 2024-01-26
---

# Linux的默认打开方式

Think about a question: why can a browser launch the system file manager?

becasue it uses the `xdg-open` command.

`xdg` is short for `X Desktop Group`, the group make the standard.

besides, i have to know `MIME` (Multipurpose Internet Mail Extensions)

MIME determine which application is able to be executed the `xdg-open`.

If you editor the `.desktop` ext file(which is in /usr/share/applications/), you will find they have the properties is about mine.



to change the default application, you need change the mime list, you can use the following command:

```
xdg-mime default ranger.desktop inode/directory
```

it let the ranger.desktop open inode/directory type.