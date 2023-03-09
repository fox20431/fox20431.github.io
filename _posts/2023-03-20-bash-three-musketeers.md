# Bash 三剑客

bash 三剑客是指 grep、sed 和 awk 这三个常用的文本处理工具。

1. awk：是一种强大的文本处理工具，可以用于对文本进行格式化、计算、过滤等操作。awk 可以根据特定的规则对文本进行分割，然后对每个分割出来的部分进行处理。awk 常用于数据处理、报表生成等。

这三个工具都是基于命令行的，可以通过管道符号将它们的输出传递给其他命令进行处理。在 Linux 系统中，这三个工具被广泛应用于文本处理、日志分析、数据处理等方面。

## GREP

GREP 全称 Global Regular Expression Print，是一种强大的文本搜索工具，它可以在文件或者标准输入中查找匹配某个模式的行，并将其输出。grep 常用于查找关键字、过滤文本等。

常用命令：

```sh
# find files which contain the $(string)
grep -rl $(string)
# -r recursive
# -l files-with-matched
```

## SED

sed 全称 Stream Editor，是一个流编辑器，用于对文本进行编辑和转换。sed 可以根据正则表达式或其他规则对文本进行替换、删除、插入等操作。sed 常用于批量修改文件、文本过滤等。