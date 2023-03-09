# Docker Desktop for Windows

现在安装 Docker 支持 `WSL(Recommended)` 和 `Hyper-V` 。

我错的以为它的结构类似于 `VS Code` 的 `服务器-客户端` 的结构，会在我之前的 Ubuntu 的 WSL 中安装 Docker 的后台的服务，实际上它是创建了新的 WSL 。这点可以通过 `wsl -l -v` 来验证，输出除了 Ubuntu 还有 `docker-desktop` 和 `docker-desktop-data` 。

因为我在创建卷的时候无法在 Ubuntu 的 WSL 中 `/var/lib/docker/volumes` 路径找到创建的文件，所以发现了这个问题。

产生这个错误认知的原因很简单，就是 Windows 的 PATH 共享给 WSL，导致我的 Ubuntu 也能使用 `docker` 命令 ，以为是 Docker Desktop 安装到 Ubuntu 中的。实际上是在 Windows 的命令。

最后认知这个问题来源这个 issue ：https://github.com/microsoft/WSL/discussions/4176

通过 Windows Explorer 路径进入：

```
\\wsl$\docker-desktop
\\wsl$\docker-desktop-data
```

终端运行

```
wsl -d docker-desktop
```

可以进入Docker的WSL。
