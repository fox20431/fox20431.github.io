---
title: GNU make utility tutorial
date: 2023-09-26
---

# GNU Make 教程

## Introduce

`make` 是构建的自动化工具。

`make` 工具可以被用于任何可以通过shell命令运行的编程语言。

[官方手册](https://www.gnu.org/software/make/manual/make.pdf)摘录：

> Our examples show C programs, since they are most common, but you can use `make`
> with **any programming language whose compiler can be run with a shell command**. 

## An Introduction to Makefiles

>  You need a file called a `makefile` to tell `make` what to do. Most often, the makefile tells `make` how to compile and link a program.

### A Simple Makefile

```makefile
edit : main.o kbd.o command.o display.o \
	insert.o search.o files.o utils.o
	cc -o edit main.o kbd.o command.o display.o \
		insert.o search.o files.o utils.o
main.o : main.c defs.h
	cc -c main.c
kbd.o : kbd.c defs.h command.h
	cc -c kbd.c
command.o : command.c defs.h command.h
	cc -c command.c
display.o : display.c defs.h buffer.h
	cc -c display.c
insert.o : insert.c defs.h buffer.h
	cc -c insert.c
search.o : search.c defs.h buffer.h
	cc -c search.c
files.o : files.c defs.h buffer.h command.h
	cc -c files.c
utils.o : utils.c defs.h
	cc -c utils.c
clean :
	rm edit main.o kbd.o command.o display.o \
		insert.o search.o files.o utils.o
```

### What a Rule Looks Like

A simple makefile consists of "rules" with the following shape:

```makefile
target ... : prerequisites ...
	recipe
	...
	...
```



## 参考文档

参考：

- [官方文档](chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://www.gnu.org/software/make/manual/make.pdf)