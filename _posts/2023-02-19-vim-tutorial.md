# Vim指南

## 简介

Vim是Vi的增强版。图形界面下建议安装`gvim`，同样可以在终端下使用`vim`。

## 操作



### 移动光标

**moving cursor in normal mode**

h: left; j: up; k: down; l: left.

**move cursor shortcut for word in normal mode**

- `w`：下一个单词的开头。
- `W`：下一个单词的开头，以空白字符为界。
- `b`：上一个单词的开头。
- `B`：上一个单词的开头，以空白字符为界。
- `e`：下一个单词的末尾。
- `E`：下一个单词的末尾，以空白字符为界。
- `ge`：上一个单词结尾。
- `gE`：上一个单词结尾，以空白字符为界。

**move cursor shortcut for line in normal mode**

- `^`：行首
- `$`：行尾

**move cursor shortcut for text in normal mode**

- `gg`：the start of text
- `G`: The end of text

### 模式切换

vim模式有如下种类：

- normal
- insert
- visual
- command-line
- replace
- visual block

**任何模式的切换都需要通过normal模式！**

**switch to insert mode shortcut from normal mode**

- i: insert before cursor.
- a: insert after cursor.
- I: insert the beginning of the line where the cursor is.
- A: insert the ending of the line where the cursor is.
- c: selectively delete then insert.
- cc: delete all characters of the line where the cursor is except enter then insert.
- s: delete the character under the cursor then insert.
- S: delete all characters of the line where the cursor is except enter then insert.

**switch to other mode shortcut from normal mode**

- `v`: visual mode
- `c-v`: visual block mode
- `:`: command-line mode
- `R`: replace mode

**undo&redo**

- `u`: undo
- `<Ctrl-r>`: redo

## 文本操作

**replace**

- `R`: replace mode
- `r`: replace the charactor on the cursor

**delete**

**如果 `normal ` 模式下显示的光标是方块，`d`选中的范围为光标方块前侧到光标移动的字符（包含方块光标指向的字符）。**

- `x`：删除当前字符
- `d`：选择范围删除，比如 `de` 删除从当前到单词尾部的内容
- `dd`：删除当前行

**格式化**

`==`: 格式化当前行

`gg=G`: 将全部代码格式化

**字符串操作**

`/<pattern string>`: 查找

`:<range>s/<targetstring>/<repalced string>[/g]`: 替换

`: g/<string>,[end raw]/d`：删除字符串所在行，比如删除包含特定字符行和接下来两行：g/pattern/,.+2d

\<range\>表示范围，`%`表示全文，n表示第n行，.表示当前行，$表示末行，^表示首行

### 文件操作

- `:w`: wite
- `:q`: quit
- `:qa`: quit all buffers

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

## Vimrc

**切忌在 ArchLinux 的 `/etc/vimrc` 中 `runtime! archlinux.vim` 不能删除。**否则会产生一些影响，已知影响map不可用。

下面是 `/etc/vimrc` 的示范配置，后续会跟进更改。

```vimrc
" This line should not be removed as it ensures that various options are
" properly set to work with the Vim-related packages.
runtime! archlinux.vim


" editor
" >>>
set encoding=utf-8

" '\t' displays space width
set tabstop=4
set expandtab
" <Tab> and <BS> operate space width
set softtabstop=4
" expand tab into spaces
set smarttab

set autoindent
set cindent
" indent width
set shiftwidth=4
set smartindent

" not working
"set pastetoggle=<F2>
nnoremap <F2> :set invpaste paste?<CR>


"nnoremap <C-k> :set invpaste paste?<CR>
"set nopaste

set scrolloff=8
" <<<

" appearance
" >>>
syntax on

set wrap

set nolist
"set list
set listchars=eol:⮐,tab:-->,trail:·
"set listchars=eol:!,tab:-->,trail:.

set showcmd
set cmdheight=1
"set showmode

set number
set relativenumber

" status line appearance
" 0: never; 1: only if there are at least two windows; 2: always
set laststatus=2
set statusline=%<
"full path
set statusline+=%F            
set statusline+=\ %m
"modified flag
" Separation point between left and right aligned items.
set statusline+=%=
set statusline+=%l:%c             "current line
set statusline+=\ 0x%B          "character under cursor

" <<<


" feature
" >>>
" forbid indent when adding comments
"keep the format for pasting action
"set mouse=a
" Display tab and space
"set list
" fold method
"set fdm=indent

" Open a new buffer, hide instead of close
set hidden

" Set the time(ms) that wait for next key of leader
set timeoutlen=1000

set updatetime=300

"set signcolumn=yes
" <<<
```
