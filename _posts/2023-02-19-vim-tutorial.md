# Vim指南

`Vim` is abbr. of `Vi Improved`.

`Vim` 是 `Vi` 的增强版。

## Installation

仅终端安装`vim`，图形界面建议安装 `gvim`  。

```sh
sudo pacman -S vim
# or
sudo pacman -S gvim
```

## Conception

VIM 在Eidtor有三种常见模式，分别为：Normal、Insert、Visual。

### 模式状态编辑

VIM 具有多种模式，允许用户在不同的环境下执行不同的操作：

1. **普通模式 (Normal Mode)**：这是默认模式，用于导航、复制、粘贴和删除文本。
2. **插入模式 (Insert Mode)**：在这个模式下，你可以像普通文本编辑器一样输入和编辑文本。
3. **可视模式 (Visual Mode)**：允许以可视方式选择文本块，然后执行复制、删除等操作。
4. **可视行模式 (Visual Line Mode)**：类似于可视模式，但以整行为单位选择文本。
5. **可视块模式 (Visual Block Mode)**：以块为单位选择文本，可以在列中选择文本。
6. **替换模式 (Replace Mode)**：允许替换光标所在位置的字符。
7. **命令行模式 (Command-Line Mode)**：用于执行一些底层命令，如保存、退出等。

## Operation In `Normal Mode`

Vim 打开默认为 `Normal Mode`。如果编辑器处于其他 `Mode`，均可以使用 `<ESC>` 回到 `Normal Mode` ，比如：

Press `<ESC>` to switch to `Normal Mode` in the `Insert Mode`.

Press `<ESC>` to switch to `Normal Mode` in the `Visual Mode`.

### Basic Movement

| direction | distance | key                  |
| --------- | -------- | -------------------- |
| up        | 1 char   | `J` or `up arrow`    |
| down      | 1 char   | `K` or `down arrow`  |
| left      | 1 char   | `H` or `left arrow`  |
| right     | 1 char   | `L` or `right arrow` |

### Advanced Movement

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

### Edition

first and most common:

| command    | effect |
| ---------- | ------ |
| `u`        | undo   |
| `<Ctrl-r>` | redo   |

Vim 的复制粘贴：

| command | effect                                                       |
| ------- | ------------------------------------------------------------ |
| `y`     |                                                              |
| `y`     | 选择范围复制，比如  `ye`  会复制从当前光标指向的字符（包含）到单词尾部的内容 |
| `dd`    | 删除                                                         |

Vim 的删除不仅仅是删除，还会把删除的字符串保存到Vim的寄存器中，通过 `p` 粘贴出来：

| command | effect                                             |
| ------- | -------------------------------------------------- |
| `x`     | undo                                               |
| `d`     | 选择范围删除，比如 `de` 删除从当前到单词尾部的内容 |
| `dd`    | 删除                                               |

- `x`：删除当前字符
- `d`：选择范围删除，比如 `de` 删除从当前到单词尾部的内容
- `dd`：delete the current line and count the line into register

**格式化**

`==`: 格式化当前行

`gg=G`: 将全部代码格式化

**字符串操作**

`/<pattern string>`: 查找

`:<range>s/<targetstring>/<repalced string>[/g]`: 替换

`: g/<string>,[end raw]/d`：删除字符串所在行，比如删除包含特定字符行和接下来两行：g/pattern/,.+2d

\<range\>表示范围，`%`表示全文，n表示第n行，.表示当前行，$表示末行，^表示首行

## Operation In `Visual Mode`

常见

| Command | Effect                          |
| ------- | ------------------------------- |
| gu      | lowercase the select characters |
| gU      | uppercase the select characters |

## Operation In `Insert Mode`

Press `i` to switch to `Insert Mode` under the `Normal Mode`.

基本操作和普通编辑器相同，略过。

### 补全技巧

自动补全 ctrl+p ctrl+n

前面声明了结构体 `T` ，想在输入 `T.` 时弹出成员供选择，只需在用之前按一下：ctrl+f12

ctrl+x ctrl+o（智能补全）

ctrl+x ctrl+f（补全文件名）

 jump in: ctrl+]

jump back: ctrl+o / ctrl+t

## Operation Mode in `Command Mode`

### Help Doc

在VIM中使用下述命令

```vim
:help
```

如果你有制定的文件需要打开，可以指定：

```
:help term.txt
```

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
