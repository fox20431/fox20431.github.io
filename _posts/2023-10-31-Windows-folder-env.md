---
title: Windows Folder Env
date: 2023-10-31
---

# WIndows文件夹环境变量

`%USERPROFILE%` 用户目录

`%SystemRoot%`: 表示Windows系统的安装目录。默认情况下，它指向 `C:\Windows`。

1. **%ProgramFiles%**: 指向Windows程序文件目录，默认为 `C:\Program Files`。
2. **%ProgramFiles(x86)%**: 对于64位系统，这个变量指向64位程序文件目录，默认为 `C:\Program Files (x86)`。
3. **%UserProfile%** 或 **%HomeDrive%%HomePath%**: 表示当前用户的主文件夹（通常是 `C:\Users\YourUsername`）。
4. **%Temp%** 或 **%Tmp%**: 表示用于存储临时文件的目录，默认情况下为 `%SystemRoot%\Temp` 或 `%SystemDrive%\Temp`。
5. **%AppData%**: 指向当前用户的应用程序数据目录，通常为 `C:\Users\YourUsername\AppData\Roaming`。
6. **%LocalAppData%**: 指向当前用户的本地应用程序数据目录，通常为 `C:\Users\YourUsername\AppData\Local`。
7. **%Public%**: 指向公共文件夹，通常为 `C:\Users\Public`。
8. **%SystemDrive%**: 表示Windows系统所在的驱动器，通常为 `C:`。
9. **%WinDir%**: 指向Windows系统目录，通常为 `%SystemDrive%\Windows`。