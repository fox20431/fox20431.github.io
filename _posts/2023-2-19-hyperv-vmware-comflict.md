# Hyper-v 与 Vmware 的冲突

WSL 底层也是使用 Hyper-V

当电脑使用 Hyper-V 的时候，VMWare 则无法使用 ` Intel VT-x/EPT` 功能。

这将导致虚拟机的性能表现不佳。

所以要么使用 hyperv，要么使用 vmware。

考虑到 Docker 使用了 WSL/Hyper-V 。被迫无奈选择 hyperv 作为解决方案。

## Solution

首先需要在特性里面添加/去除 Hyper-V/Virtual Manchine Platform/Windows Hypervisor Platform/WSL 。

管理员权限下开启 hyper-v ：

```sh
bcdedit /set hypervisorlaunchtype auto
```

管理员权限下关闭 hyper-v ：

```sh
bcdedit /set hypervisorlaunchtype off
```

最终重启