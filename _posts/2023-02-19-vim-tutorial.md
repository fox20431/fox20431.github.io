# Vim指南

## 简介

Vim是Vi的增强版。

Vim相比其他编辑器提供了多种模式进行切换。

详细信息，请启动Vim使用`:help`获取更多帮助。

默认leader键 `\`

## 操作

以下快捷键均在命令模式。

### 方向键

- h: &larr;.
- j: &uarr;.
- k: &darr;.
- l: &rarr;.

### 操作键

- i: insert before cursor.
- I: insert the beginning of the line where the cursor is.
- a: insert after cursor.
- A: insert the ending of the line where the cursor is.
- c: selectively delete then insert.
- cc: delete all characters of the line where the cursor is except enter then insert.
- s: delete the character under the cursor then insert.
- S: delete all characters of the line where the cursor is except enter then insert.
- w: 移动到下一个单词开头
- e: 移动到当前单词尾部
- b：移动到上一个单词开头
- ge：移动到上一个单词结尾
- o: 下一行创建
- .：重复上次命令
- ^：行首
- $：行尾

### 文件操作

- `:w`: wite
- `:q`: quit

:qa可以退出所有

查找字符串

/\<pattern string\>

替换字符串


:\<range\>s/\<targetstring\>/\<repalced string\>[/g]

删除字符串所在行

: g/\<string\>,[end raw]/d

比如删除包含特定字符行和接下来两行：g/pattern/,.+2d

\<range\>表示范围，`%`表示全文，n表示第n行，.表示当前行，$表示末行，^表示首行

距离：

:n,$s/vivian/sky/ 替换第 n 行开始到最后一行中每一行的第一个 vivian 为 sky

gg=G 将全部代码格式化

### 窗口操作

:split

:vsplit

Ctrl + w + h：向左移动窗口

Ctrl + w + j： 向下移动窗口

Ctrl + w + j： 向上移动窗口

Ctrl + w + l： 向右移动窗口

改变当前窗口的尺寸，同时当然也会影响到其他窗口。
在gvim和vim中，可以用鼠标点击窗口的顶部白色条并窗口直接调整尺寸。

也可以直接用命令，调整尺寸命令也是以Ctrl + W开头：
Ctrl + W + =  ：让所有窗口调整至相同尺寸（平均划分）

Ctrl + W + _  ：让当前窗口最大

Ctrl + W + -：将当前窗口的高度减少一行，也可在ex命令中，：resize -4明确指定减少的尺寸
Ctrl + W + +：将当前窗口的高度增加一行。同样在ex命令中，：resize +n 明确指定增加尺寸

Ctrl + W + < ：将当前窗口的宽度减少
Ctrl + W + > ：将当前窗口的宽度增加

也可以通过命令：vertical resize n明确指定改变宽度

nmap \<C-k\> :res +5\<CR\>
nmap \<C-j\> :res -5\<CR\>
nmap \<C-h\> :vertical resize-5\<CR\>
nmap \<C-l\> :vertical resize+5\<CR\>

## 补全技巧

自动补全 ctrl+p ctrl+n

前面声明了结构体T，想在输入T.时弹出成员供选择，只需在用之前按一下：ctrl+f12

ctrl+x ctrl+o（智能补全）

ctrl+x ctrl+f（补全文件名）

 jump in: ctrl+]

jump back: ctrl+o / ctrl+t

## 帮助文档

在VIM中使用下述命令

```vim
:help
```

如果你有制定的文件需要打开，可以指定：

```
:help term.txt
```



---

relative line number: 

.vimrc:

```
set relative number
```

command:

```
[number]j` or `[number]k
```