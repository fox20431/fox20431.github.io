---
title: Powershell tutorial
date: 2023-07-27
---



# Powershell tutorial

The following excerpt form [Microsoft Shell Documentation](https://learn.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.3):

> Excerpt from PowerShell is a cross-platform task automation solution made up of a command-line shell, a scripting language, and a configuration management framework. PowerShell runs on Windows, Linux, and macOS.

Powershell 是微软的跨平台任务自动化及解决方案。

## 安装

由于 Windows 自带 Powershell 的版本一般低于最新低，建议去 [Powershell Git 仓库](https://github.com/PowerShell/PowerShell) 下载最新版本，安装完成后配置到 Terminal 。

可以通过校验当前 Powershell 版本来确定 Terminal 是否配置正确：

```powershell
$PSVersionTable
```

## 快捷键

`Tab` 直接补全，`Ctrl` + `Space` 菜单补全。

## 美化

类似 Linux 下的 `zsh` 的 `oh-my-zsh` 美化， `PowerShell` 也存在 `oh-my-posh` 美化工具。

*温馨提示：oh-my-zsh 会拖慢启动速度，参考我的Powershell启动耗时：配置前700ms，配置后1000ms*

### 安装

**方式一**

`winget` 命令时 Windows 官方在 Win10 引入的包管理工具，可以通过 winget 快速安装 `on-my-posh`：

```
winget install JanDeDobbeleer.OhMyPosh
```

**方式二**

[oh-my-posh GitHub Release](https://github.com/JanDeDobbeleer/oh-my-posh/releases)

### 设置主题

通过下述命令查看可用主题：

```powershell
Get-PoshThemes
```

选择一个主题，并获取该主题配置文件的位置，配置 `profile`：

```powershell
notepad $PROFILE
```

预设如下启动命令，将 `/path/to/config` 修改为主题配置文件：

```
oh-my-posh init pwsh --config /path/to/config | Invoke-Expression
```

## 命令

Powershell 的内建命令格式统一为 `Verb-Noun` ，但对命令的大小写不敏感。

下述命令查看所有内建命令：

```powershell
Get-Command -CommandType Cmdlet
```

*cmd 查看内建指令的命令是 `help`*

### 常见命令

**查看命令位置**

```powershell
Get-Command <command>
```

cmd中的 `where` 在 powershell 中不可用，这是由于 powershell 默认 where 映射 `Where-Object` ，该方式配置的命令的优先级高于系统 `C:\Windows\System32\` 目录下的  `where` 命令。

**查看帮助文档**

```powershell
Get-Help <command>
```

