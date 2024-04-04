---
title: irssi tutorial
date: 2024-04-04
---

# irssi 教程

`irssi` 是使用支持 `IRC（Internet Relay Chat）` 终端客户端。

新手教程参考官方文档：New users guide](https://irssi.org/New-users/#)

*个人猜测，`irssi`这个名字应该是根据 IRC 音译过来的，`ssi` 发音为 `C`。* 

## 使用

以下以irssi新人身份使用 `irssi` 加入 `gentoo` 官方频道。

1. 终端启动 `irssi`

   ```sh
   irssi
   ```

2. 设置nickname

   ```
   /set nick whatyouwant
   ```

3. 连接网络

   ```sh
   # 查看可用网络
   /network
   # gentoo 频道在 liberachat，所以我们加入这个频道
   /connect liberachat
   ```

   如果重名回到第二步更改后再进入

4. 加入频道（Channal）

   ```sh
   /join #gentoo
   ```

## 操作指令

| 指令                | 描述                          |
| ------------------- | ----------------------------- |
| /part               | 退出当前频道                  |
| `/part <channal>`   | 退出指定频道                  |
| /window             | 查看当前窗口信息              |
| /window list        | 仅适用在窗口1，即网络的主页面 |
| `/window <number>`  | 切换到指定序号的窗口          |
| `/window <channal>` | 切换到指定频道的窗口          |



