---
title: Get Started With WSL
excerpt: "WSL(Windows Subsystem for Linux) is released by Microsoft Company. It provides a possibility of using the POSIX operation method in Windows."
---

# WSL

Windows Subsystem for Linux.

The following content is for WSL version 2(WSL2).

## Install

First of all, you need to enable the following features:

1. Open the Windows Features;
2. Open the `Hyper-V`, `Virtual Machine Platform`, and `Windows Subsystem for Linux`.

Install the `Debian` (I recommend it extremely!) from the Microsoft Store after enabling all the above features.

Then open the `Debian` application and wait for it to finish installation automatically.

More about it referring to [WSL installation documentation on the Microsoft Learn platform](https://learn.microsoft.com/zh-cn/windows/wsl/install).

## WSL Config

你可以在两处地方设置，分别为宿主机的 `%USERPROFILE%\.wslconfig`，另外一个是WSL内部的`/etc/wsl.conf`

To use the subsystem more comfortably and show you the customizability of the system, let's dive into the config chapter!

Please modify the file's content; create it if it doesn't exist.  

```sh
sudo vim /etc/wsl.conf
```
**Enable Systemd**

```conf
[boot]
systemd=true
```

**Not Append Windows Path**

这个将会拖慢系统的自动补全速度

```conf
[interop]
appendWindowsPath = false
```

## Network

You should know the domain of WSL is `wsl.localhost`, and the host port is shared with WSL which means it's a conflict if a port of the host's service is the same as the WSL's. 

### Proxy

The proxy is necessary for the Chinese. As we all know, we usually run `Clash for Windows` on hosts; it can enable the `LAN` feature, which means you can share the port for other terminals by the local network. How does WSL use the port to implement the proxy?

1. use the command to check the gateway `cat /etc/resolv.conf`;

2. set the `http_proxy` and `https_proxy` environments.

## Peripheral Device Mount

Windows can't resolve the ext4, btrfs, and so on the file system by default. To address the problem, we can use the WSL that support the file system of the previously motioned types. The specific steps as the follows:

1. Check the storage devices on the host(Windows):

   ```powershell
   wmic diskdrive list brief
   ```

   The output looks like this:

   ```
   Caption                     DeviceID            Model                       Partitions  Size
   Samsung SSD 980 PRO 1TB     \\.\PHYSICALDRIVE0  Samsung SSD 980 PRO 1TB     2           1000202273280
   SAMSUNG MZVL2512HCJQ-00BL2  \\.\PHYSICALDRIVE1  SAMSUNG MZVL2512HCJQ-00BL2  2           512105932800
   ```

2. Select the storage device and its partitions you want to mount then execute the following command on the host:

   ```powershell
   wsl --mount \\.\PHYSICALDRIVE1 --partition 1
   ```

   If it's successful, it will output like this:

   ```
   The disk was successfully mounted as '/mnt/wsl/PHYSICALDRIVE1p1'.
   ```

3. No matter which partitions you has mounted, WSL can recognize the entire device. You can use the following command to check it:

   ```
   sudo parted -l
   ```

4. I don't need to say more if the WSL scans the device. Just mount it.

   ```
   sudo mount /dev/device /mount/path
   ```


## Connect the USB

WSL 的端口和宿主机端口绑定的，比如 WSL 的 Postgresql 占用了 5432 端口，那么宿主机的这个端口会被占用并成为 Postgresql 端口。

因此你想访问 WSL 中的 Postgresql 服务可以通过 `wsl.localhost:5432` 或者 `localhost:5432` 。

## Sharing Host Proxy

The WSL is thought the machine which is in LAN, so you can use the host proxy.

Get the host IP address:

```
cat /etc/resolv.conf
```

Change the `~/.bashrc`:

```
export http_proxy="http:{host_ip}:7890"
export https_proxy="http:{host_ip}:7890"
export all_proxy="http:{host_ip}:7890"
```

From my personal experience, the key name of proxy in uppercase will not work, only lowercase ones will take effect.

However, the IP address of WSL changes.

There are a automated solution here.

Create a file named `wsl-proxy-config.sh`:

```shell
#!/bin/bash
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ")

export http_proxy="http://$host_ip:7890"
export https_proxy="http://$host_ip:7890"
export all_proxy="http://$host_ip:7890"
```

Let it be executed by `.bashrc`.

## 配置网络

这样设置之后，端口不共用了，且网关地址固定了。（具体原因不明，可能需要查看更多的微软商店）

```sh
New-NetIPAddress -InterfaceAlias 'vEthernet (WSL)' -IPAddress '172.29.122.1' -PrefixLength 20
```

