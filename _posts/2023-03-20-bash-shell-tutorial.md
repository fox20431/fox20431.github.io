# Bash Shell 入门教程

在没有图形界面之前，Shell作为“外壳”与Linux内核交互。

在追求更好地使用体验的探索中，诞生了 “Linux哲学” 影响着工具的开发和用户的使用，所以Linux哲学是什么？

1. 简单而直接的接口：Linux Bash的命令行界面非常简单，用户可以通过键入命令来执行各种任务。
2. 每个程序只做一件事情：Linux Bash的每个命令都只完成一项任务，这使得命令更加简单、可靠和灵活。
3. 快速而灵活的输入输出：Linux Bash支持各种输入输出方式，包括标准输入输出、管道、重定向等，这使得用户可以轻松地将多个命令组合起来，完成复杂的任务。
4. 软件复用：Linux Bash可以使用其他命令的输出作为输入，这使得用户可以将多个命令组合起来，完成更复杂的任务。
5. 使用文本文件进行通信：Linux Bash使用文本文件作为命令和程序之间的通信方式，这使得数据交换更加简单和可靠。
6. 程序设计应该追求可靠性和稳定性：Linux Bash的命令都被设计为可靠、稳定和健壮，以确保系统的稳定性和可靠性。

### Pager

Pager 是一种用于显示大量文本数据的工具，它可以将文本数据分成一页一页进行显示。在 Unix/Linux 系统中，Pager 通常由两个工具来实现：more 和 less。

more 是最早的 Pager 工具，它只能向前翻页，不能向后翻页。使用 more 查看文本时，可以使用空格键翻页，使用 Enter 键向下滚动一行，使用 q 键退出。

### 输入/输出重定向：


```
> 输出重定向
>> 追加输出重定向
< here file 输入重定向 用于将一个文件的内容作为命令的输入
<< here document 用于将多行文本作为命令的输入
<<< here string 用于将一个字符串作为命令的输入
```

## Optism

### 大小写敏感的Bash补全

**创建 `inputrc` 文件：** 创建或编辑你的 `~/.inputrc` 文件，如果不存在的话。添加以下内容：

```sh
set completion-ignore-case on
```

`inputrc` 文件是用于配置 Readline 库的配置文件，而 Readline 是一个用于处理文本输入的库，它提供了命令行编辑和历史记录功能。Bash 是一个使用 Readline 库来处理用户输入的命令行解释器，因此 Bash 在交互模式下（非批处理模式）会使用 `inputrc` 文件中的配置来影响用户输入的行为。

### glob expansion

通配符拓展

```bash
# 1: Enable `show-all-if-ambiguous` in ~/.inputrc

set show-all-if-ambiguous on

# 2a: Check to ensure that `glob-complete-word` is bound.
$ bind -q "glob-complete-word"

glob-complete-word can be invoked via "\eg".

# 2b: If unbound, bind `glob-complete-word` to "\eg".
$ bind '"\eg":glob-complete-word'

# 3: Trigger the autocompletion with <META-g> or <ESC-g>

# META => alt      (Windows/Linux)
# META => option   (OSX)

$ ls *2.<META-g>     

# possible completions will be listed (show-all-if-ambiguous)   
mydoc2.pdf mydoc2.tex mydoc2.txt

# glob pathname completion will be performed (glob-complete-word)
$ ls mydoc2.  
```

上述情况在Gnome下 `alt` 可能被全局占用，请在 Setting -> Keyboard -> Special Character Entry 切换快捷键。