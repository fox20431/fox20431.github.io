# Linux Top Command

PID USER PR NI VIRT RES SHR S %CPU %MEM TIME+ COMMAND

序号列名含义
PID 进程id
PPID 父进程id
RUSER Realusername
UID 进程所有者的用户id
USER 进程所有者的用户名
GROUP 进程所有者的组名
TTY 启动进程的终端名。不是从终端启动的进程则显示为?
PR 优先级
NInice 值。负值表示高优先级，正值表示低优先级
P 最后使用的CPU，仅在多CPU环境下有意义
%CPU 上次更新到现在的CPU时间占用百分比
TIME 进程使用的CPU时间总计，单位秒
TIME+ 进程使用的CPU时间总计，单位1/100秒
%MEM 进程使用的物理内存百分比
VIRT 进程使用的虚拟内存总量，单位kb。VIRT=SWAP+RES
SWAP 进程使用的虚拟内存中，被换出的大小，单位kb。
RES 进程使用的、未被换出的物理内存大小，单位kb。RES=CODE+DATA
CODE 可执行代码占用的物理内存大小，单位kb
DATA 可执行代码以外的部分(数据段+栈)占用的物理内存大小，单位kb
SHR 共享内存大小，单位kb
nFLT 页面错误次数
nDRT 最后一次写入到现在，被修改过的页面数。
S 进程状态。
D= 不可中断的睡眠状态
R= 运行
S= 睡眠
T= 跟踪/停止
Z= 僵尸进程
COMMAND 命令名/命令行
WCHAN 若该进程在睡眠，则显示睡眠中的系统函数名
Flags 任务标志，参考sched.h


PID       进程 id
COMMAND   命令
%CPU      cup 占比
TIME      运行时间
#TH       线程数量
#WQ
#PORT
MEM       内存
PURG
CMPRS     表示属于您的进程的压缩数据的字节数（不是位）。
PGRP
PPID    父进程ID
STATE
BOOSTS
%CPU_ME
%CPU_OTHRS
UID