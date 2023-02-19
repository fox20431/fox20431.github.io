# Power Shell


Power Shell 是支持 Docker 自动补全的。

1. 确保已经安装Docker。

2. 安装 PowerShell 模块 DockerCompletion。

```ps1
Install-Module DockerCompletion
```

3. 引入该模块到 PowerShell 中。

```ps1
Import-Module DockerCompletion
```

4. (Optional)如果想每次启动终端默认引入，请添加到配置文件。

```ps1
notepad $PROFILE
```