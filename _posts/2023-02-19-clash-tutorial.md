# Clash

[Clash GitHub](https://github.com/Dreamacro/clash)

Clash可以为不同协议和应用提供统一的代理接口。

Clash分为“开源”和“闭源”两个版本。闭源的版本叫做Clash Premium。

## Clash Feature

### Why do I choose Clash?

- Clash为Shadowsocks、V2ray、Trojon提供了新的一层抽象；
- Clash可以检测多个节点的网络状况，并选择合适的网络，比较适合机场；

## Config

[wiki](https://dreamacro.github.io/clash/)

### UI

Clash提供了指定的API，并允许用户自定义UI界面。下面为开源的Clash的Web用户界面，可以通过配置指定页面位置。

- [yacd](https://github.com/haishanh/yacd)

- [clash-dashboard](https://github.com/Dreamacro/clash-dashboard)

## Extended

很多机场仅提供V2ray订阅连接，理论上可以将V2ray订阅连接转为Clash订阅，以下为解决方案：

订阅转换器地址：https://sub-web.netlify.app/

开源地址：https://github.com/CareyWang/sub-web

## Clash On Windows

Clash 在 Windows 平台下的解决方案：

首先编写 PowerShell 后台运行 Clash 并输出日志的脚本：

```ps1
$program = "program.exe" # replace with the name of the terminal program you want to run
$outputFile = "program_output.txt" # replace with the desired name of the output file

# Start the program and redirect its output to a file
Start-Process $program -NoNewWindow -RedirectStandardOutput $outputFile
```

然后将该脚本设置为 Task Scheduler 开机自启动：

1. 指定 `C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` 作为应用程序，参数选择 `-ExecutionPolicy Bypass -File "C:\path\to\script.ps1"`
2. 选择 `Run whether user is logged on or not` ，该选项确保应用后台运行。