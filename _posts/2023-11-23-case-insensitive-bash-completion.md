---
title: case insensitive bash completion
date: 2023-11-23
---

# 大小写敏感的Bash补全

**创建 `inputrc` 文件：** 创建或编辑你的 `~/.inputrc` 文件，如果不存在的话。添加以下内容：

```sh
set completion-ignore-case on
```

`inputrc` 文件是用于配置 Readline 库的配置文件，而 Readline 是一个用于处理文本输入的库，它提供了命令行编辑和历史记录功能。Bash 是一个使用 Readline 库来处理用户输入的命令行解释器，因此 Bash 在交互模式下（非批处理模式）会使用 `inputrc` 文件中的配置来影响用户输入的行为。