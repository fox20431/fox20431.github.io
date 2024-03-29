---
title: Shell tutorial
---



# Shell Tutorial

## How to create a simple shell script

1. Create the file with `.sh` suffix.

2. Insert the `#!/bin/sh` in the first line of the file to specify which shell it is to be executed by.

3. Make the file executable.

   ```sh
   chmod +x script.sh
   ```

## Comment

Single comment: `#`

Multiple line comment:

```sh
:<<[character]
the words to be commented
[character]
```
For example:
```sh
:<<!
the words to be commented
!
```

## Variable

**define the variable**

`your_name="null"`

变量命名规范：

- 命名只能使用英文字母，数字和下划线，首个字符不能以数字开头。
- 中间不能有空格，可以使用下划线（_）。
- 不能使用标点符号。
- 不能使用bash里的关键字（可用help命令查看保留关键字）。

### call the variable

`$your_name`或`${your_name}`  

### read-only variable

`read-only your_name`

只读变量的值不能被改变。  

### delete variable

`unset your_name`

unset 命令不能删除只读变量。  

### variable type

- 局部变量

- 环境变量
	
	所有程序都能访问环境变量。  
	
- shell变量

  是由shell程序设置的特殊变量。  

## Value

### String

### 单引号
`str='this is a string'`  
单引号里的任何字符都会原样输出  
### 双引号
`str="this is a string"`

- 双引号里可以有变量  
- 双引号里可以出现转义字符  
### 获取字符串长度
`${#str}`  

### 提取子字符串
`${str:a:b}`  
提取对象为变量str，长度为从a到b  
### 查找子字符串
```
str="your name is array"
echo `expr index "$str" io`
# 查找字符i或o
# 输出最先出现字符的位置
# 输出2
```
### Array

### 定义数组

`数组名=(值1 值2 ... 值n)`

例如：  

```
array_name=(value0 value1 value2 value3)
```
或者
```
array_name=(
value0
value1
value2
value3
)
```
或者
```
array_name[0]=value0
array_name[1]=value1
array_name[n]=valuen
```
### 读取数组
`${数组名[下标]}`  
例如：  
```
valuen=${array_name[n]}
```
使用 @ 符号可以获取数组中的所有元素  
例如：  
`echo ${array_name[@]}`
### 获取数组的长度
- 取得数组元素的个数  
	`length=${#array_name[@]}`或`length=${#array_name[*]}`  
- 取得数组单个元素的长度  
	`lengthn=${#array_name[n]}`  

- 手动阀

## Exit Code

The exit code is provided when the command has been finished.

0 Successful

1 Failed

you can use follow the command to get the exit code:

```sh
echo $?
# or
echo $#
```

