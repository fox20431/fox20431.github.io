为当前终端设置代理，以 cmd 为例（PowerShell类似均为设置环境变量）：

```cmd
set HTTP_PROXY=http://127.0.0.1:7890
set HTTPS_PROXY=http://127.0.0.1:7890
```

持久化

设置 Windows 环境变量：

- `HTTP_PROXY` 为 `http://127.0.0.1:7890`
- `HTTPS_PROXY` 为 `http://127.0.0.1:7890`

ref: https://github.com/shadowsocks/shadowsocks-windows/issues/1489