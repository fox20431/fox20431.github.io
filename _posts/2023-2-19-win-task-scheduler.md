# Windows Task Scheduler

Recently, I want run `clash` which is terminal application in background in windows.

I think if Windows has the program like `systemd` of linux is a good things.

After my search, `Task scheduler` is the program.


## Usage

开始 > 任务计划程序 > 创建基本程序

选择触发器和启动程序，就可以使得应用程序在触发器被触发时启动。

为了让其后台运行，在 `常规` 中选择 `不管用户是否登录都要运行` 。

其实选择其他用户运行也有后台运行的效果，只是 `clash` 其他用户运行时我的用户无法打开指定端口，也就无法起到代理作用。