---
title: top command
date: 2023-08-07
---

# Top Command

The top program provides a dynamic real-time view of a running system.

推荐使用 `man` 查看帮助手册：

```sh
man top
```

## 界面解释

### 概览信息

```
top - 16:12:42 up 23:49,  2 users,  load average: 1.83, 1.52, 1.29
Tasks: 399 total,   3 running, 396 sleeping,   0 stopped,   0 zombie
%Cpu(s):  5.7 us,  1.1 sy,  0.0 ni, 92.8 id,  0.1 wa,  0.2 hi,  0.1 si,  0.0 st 
MiB Mem :  31822.6 total,  17752.4 free,   7423.0 used,   8500.9 buff/cache     
MiB Swap:  32768.0 total,  32765.5 free,      2.5 used.  24399.6 avail Mem 
```

**首行：系统概览**

```
名称 - 当前时间 已经运行23:49分钟, 两个用户, 平均负载: 近1分钟的平均负载, 近5分钟的, 近15分钟的
top - 16:12:42 up 23:49,  2 users,  load average: 1.83, 1.52, 1.29
```

负荷的数值：1表示1个CPU的线程满负荷。比如我的电脑 6 个性能核心 8个能效核心，每个性能核心2个线程，每个能效核心1个线程，共计20线程， 所以电脑满负载为20。

**第二行：进程状态**

```
进程任务数：共计399个	3个正在运行， 396个正在睡眠， 0个被停止， 0个僵尸进程
Tasks: 399 total,   3 running, 396 sleeping,   0 stopped,   0 zombie
```

**第三行：CPU状态**

```
Cpu使用时间占用百分比：
用户空间（user space），
内核空间（system），
修正的用户进程（nice），
空闲（idle），
等待（wait），
硬中断（hard interrupt），
软中断（soft interrupt），
虚拟化偷走的时间（stolen）
%Cpu(s):  5.7 us,  1.1 sy,  0.0 ni, 92.8 id,  0.1 wa,  0.2 hi,  0.1 si,  0.0 st 
```

现在解释缩写：

- us（user）：用户进程使用CPU的时间。
- sy（system）：操作系统内核执行系统级任务的时间。
- ni（nice）：优先级被调整的（niced）进程占用CPU时间的百分比。
- id:（idle）：CPU空闲的百分比，表示CPU没有运行任务的时间。
- wa（wait）：等待I/O的进程占用CPU时间的百分比，即等待磁盘或网络I/O完成的时间。
- hi（hardware interrupt）：硬中断（Hardware Interrupt）占用CPU时间的百分比，表示处理硬件设备引发的中断。
- si（software interrupt）：软中断（Software Interrupt）占用CPU时间的百分比，由操作系统内核发起的中断。
- st（stolen）：被偷取（stolen）的CPU时间的百分比，用于虚拟化环境中，表示被其他虚拟机“偷取”的时间。

这里讲一下，niceness（优先级）的概念：

nicess值的范围 -20 ~ 19 （Linux最高是19，BSD最高是20），数值越低代表越高的优先级，进程默认的nicness集成父进程，默认为0。

The following digest from [the reddit](https://askubuntu.com/questions/812144/what-exactly-is-meant-by-a-niced-and-an-un-niced-user-process)

> A "niced" process is one that has been run with the `nice` command (or whose niceness has been changed by `renice`) and an "un-niced" process is one that hasn't been run with `nice`. 

niced 进程表示被其niceness 被 `nice` 或 `renice` 调整过，un-niced 表示其 niceness 没有被调整过。

**第四行：内存和SWAP分区状态**

```
内存（单位：MB）  总量，	    空闲，	       已使用，	     缓冲/缓存用量
MiB Mem :  31822.6 total,  17752.4 free,   7423.0 used,   8500.9 buff/cache  
交换区（单位：MB） 总量，     空闲，	        已使用，       可用内存
MiB Swap:  32768.0 total,  32765.5 free,      2.5 used.  24399.6 avail Mem 
```

**可用内存 = 空闲内存 + 缓冲/缓存**

缓冲（buffer）是一种临时区域，用于数据传输期间缓冲数据。当数据从一个地方传输到另一个地方（例如，从磁盘到内存），缓冲可以暂时存储这些数据，以便在数据到达目的地之前可以进行处理。缓冲的主要目的是减少数据传输的不连续性，从而提高效率。

缓存（Cache）：缓存是一种将频繁访问的数据存储在更快速的存储介质（例如，内存）中的技术。缓存可以加速对数据的访问，因为内存访问速度远高于磁盘或其他较慢的存储介质。文件系统缓存是一种常见的缓存类型，它将磁盘上的数据暂时存储在内存中，以加速后续访问。

需要注意的是，`buff/cache`的内存通常是动态管理的，当系统需要更多内存来执行应用程序时，这些缓冲和缓存可以被释放以提供更多可用内存。

### 进程信息

```
PID		USER      PR	NI	VIRT	RES		SHR		S	%CPU	%MEM	TIME+		COMMAND
1473	ming      20	0	21.9g	701960	405604	S	13.6	2.2		39:01.16	gnome-shell 
...
```

分析表头：

```
进程ID 用户  优先级 Nice值 虚拟内存 物理内存 共享内存 进程状态 CPU   内存  CPU使用时间累加    命令
PID   USER   PR     NI    VIRT    RES      SHR     S   %CPU  %MEM	   TIME+     COMMAND
```

`PR`（Priority）和 `NI`（Niceness）都涉及进程的优先级，实际的调度优先级 `PR` 是由操作系统根据 `NI` 值计算得出的。

分析三个内存：

1. **VIRT**: 进程使用的虚拟内存大小。它包括进程使用的所有虚拟内存、共享库和映射文件等。
2. **RES**: 进程占用的物理内存大小，也称为"常驻内存集（Resident Set）"。它表示实际驻留在物理RAM中的部分。
3. **SHR**: 进程共享的内存大小，即被其他进程也使用的内存部分。

S（status）表示进程状态：R表示运行，S表示睡眠，Z表示僵尸，等等。

## 快捷键

注意区分大小写，比如在小写模式下，E 等价于 `shift + e`

### 程序控制

`q`: Quit the top.

`d`: Delay time for flush the interface

`ctrl-s`: Suspend to flush the interface

`ctrl-q`: Resume to flush the interface

### 展示控制

**进程列表**

`Arrow keys `

`page up/down`

**头部样式**

`1`: 查看每个内核的占用率

`t`: Changes the display of the CPU usage in the summary section.

`m`: Changes the display of memory usage in the summary section.

`E`: Change the memory unit.

**进程排序**

 `P`: Sort the processes by CPU.

`M`: Sort the processes by memory(%MEM) usage;

`T`: Sort the processes by runnig-time.

`N`: Sort the processes by process ID.

`R`: Sort the processes in ascending order instead of descending (default).

`V`: Shows the parent / child process hierarchy.

### 操作进程

`k`: Prompts for a process ID and closes the specified process.





