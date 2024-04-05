---
title: irssi tutorial
date: 2024-04-04
---

# irssi 教程

`irssi` 是使用支持 `IRC（Internet Relay Chat）` 终端客户端。

新手教程参考官方文档：New users guide](https://irssi.org/New-users/#)

*个人猜测，`irssi`这个名字应该是根据 IRC 音译过来的，`ssi` 发音为 `C`。* 

## 使用

以下以 `irssi` 新人身份使用 `irssi` 加入 `gentoo` 官方频道。

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

| 指令                 | 描述                                                         |
| -------------------- | ------------------------------------------------------------ |
| /quit                | 退出 irssi                                                   |
| /part                | 退出当前频道                                                 |
| `/part <channel>`    | 退出指定频道。`part` 源自 `depart` 的缩写。                  |
| /window              | 查看当前窗口信息                                             |
| /window list         | 仅适用在窗口1，即网络的主页面                                |
| `/window <number>`   | 切换到指定序号的窗口                                         |
| /wc 或 /window close | 关闭当前窗口，非 channal 的窗口无法使用 `/part` 生效，可以使用该命令。 |
| ctrl + n             | 切换到下一个窗口                                             |
| ctrl + p             | 切换到上一窗口                                               |
| `alt + <number>`     | 切换到 `<number>` 窗口，前提是和全局快捷键没冲突。           |

## Libera Chat 账号注册

虽然 nickname 可以使用，但是有被别人注册的风险，为了确保能够一直使用 nickname 需要我们注册。

参考：https://libera.chat/guides/registration

1. 设置要注册的 nickname

   ```sh
   /nick YourNick
   ```

2. 对话 NickServ 进行注册

   ```sh
   /msg NickServ REGISTER YourPassword youremail@example.com
   ```

3. 进入邮箱按操作确认

   默认从邮箱获取验证代码，向 NickServ 进行确认邮箱可用

   ```sh
   /msg NickServ VERIFY REGISTER YourNick VerifyCode
   ```


## 关于配置

**聊天网络配置**

```json
chatnets = {
  liberachat = {
    type = "IRC";
    max_kicks = "1";
    max_msgs = "4";
    max_whois = "1";
  };
  // ...
};
```

**服务器配置**

```json
servers = (
  {
    address = "irc.libera.chat";
    chatnet = "liberachat";
    port = "6697";
    use_tls = "yes";
    tls_verify = "yes";
    autoconnect = "yes";
  },
  // ...
);
```

配置聊天网络服务器的信息，用于建立网络。`autoconnect`设置为`"yes"`用于启动`irssi`自动连接。

*这里的 `chatnet` 要求为上述网络配置中的别名。*

**频道配置**

```json
channels = (
  { name = "#libera"; chatnet = "liberachat"; autojoin = "Yes"; },
  // ...
);
```

上述表示自动加入 `liberachat` 的 `#libera`，如果 `autojoin` 的值设置为 `"No"` 则不会自动加入，但会在 `/join` 指令中触发补全。

*这里的 `chatnet` 要求为上述网络配置中的别名。*

