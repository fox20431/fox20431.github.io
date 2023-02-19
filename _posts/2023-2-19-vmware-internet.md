## 如何修改 VMware Fusion 中的虚机网络 IP 地址段

作者：gc(at)[http://sysin.org](https://link.zhihu.com/?target=http%3A//sysin.org)，主页：[www.sysin.org](https://link.zhihu.com/?target=https%3A//www.sysin.org/)

原文发布地址：[https://sysin.org/article/change-vmware-fusion-networking/](https://link.zhihu.com/?target=https%3A//sysin.org/article/change-vmware-fusion-networking/)

VMware Fusion 网络默认使用了“172.16”开头的地址段，图形界面无法直接修改。

## 一、了解 VMware Fusion 中的网络类型 (1022264)

可用于虚拟机的网络类型有三种。每种网络类型都由其自身用途、行为和功能。

注意：使用错误的网络类型或配置设置可能会导致出现不良行为。

### 桥接模式网络连接

如果您的 Mac 位于以太网、无线网或 FireWire 网络中，则使用桥接网络连接通常是使您的虚拟机可以访问该网络的最简单方法。使用桥接网络连接，虚拟机将显示为与 Mac 相同的物理以太网网络中的其他计算机。

使用桥接网络连接的虚拟机可能会使用在该虚拟机桥接到的网络上提供的任何服务，其中包括文件服务器、打印机和网关。同样，配置有桥接网络连接的任意物理主机或其他虚拟机可以使用虚拟机上的资源，就好像该虚拟机是同一个网络中的物理计算机。

桥接网络适配器称为 vmnet0。在 Fusion 3.x 及更高版本中，该适配器使用 vmnet-bridge 和 vmnet-netifup 服务。

### 仅主机型网络 -- vmnet1

当使用此类型的网络连接时，虚拟机将连接到虚拟专用网络中的 Mac，这在 Mac 以外通常不可见。在同一个 Mac 中配置有仅主机网络的多个虚拟机将位于同一个网络中，并且互相可见。

仅主机网络适配器称为 vmnet1。在 Fusion 3.x 及更高版本中，该适配器使用 vmnet-dhcpd 服务。

### 网络地址转换 (NAT) 网络 -- vmnet8

如果要使用 Mac 拨号网络连接的方法将虚拟机连接到 Internet 或其他 TCP/IP 网络，或者无法向虚拟机提供 Mac 的网络中的 IP 地址，则此类型通常是使您的虚拟机可以访问网络的最简单方法。此类型还允许虚拟机访问 Mac 已连接到的 VPN。

虚拟机在外部网络中没有自己的 IP 地址。相反，会在 Mac 中设置单独的专用网络。虚拟机从 VMware 虚拟 DHCP 服务器中获取该网络上的地址。除非虚拟机启动连接，否则无法直接通过除 Mac 以外的任意计算机或网站连接该虚拟机。

NAT 网络适配器称为 vmnet8。在 Fusion 3.x 及更高版本中，该适配器使用 vmnet-natd、vmnet-dhcpd 和 vmnet-netifup 服务。

## 二、自定义网络 IP 地址段

VMware Fusion 有三个网络配置文件：networking、dhcpd.conf 和 nat.conf。

全局：

```text
/Library/Preferences/VMware\ Fusion/networking
```

vmnet1：

```text
/Library/Preferences/VMware\ Fusion/vmnet1/dhcpd.conf
/Library/Preferences/VMware\ Fusion/vmnet1/nat.conf
```

vmnet8：

```text
/Library/Preferences/VMware\ Fusion/vmnet8/dhcpd.conf
/Library/Preferences/VMware\ Fusion/vmnet8/nat.conf
```

修改 IP 地址段步骤如下，在 VMware Fusion 11.5 版本中测试通过。

### 1. 停止 vmnet 网络服务

执行命令：

```c
sudo /Applications/VMware\ Fusion.app/Contents/Library/vmnet-cli --stop
```

备注：这步是可选的，直接下一步也可以

### 2. 只需要修改 networking 配置文件

执行命令：

```c
sudo vi /Library/Preferences/VMware\ Fusion/networking
```

示例：将 vmnet1 中的 IP 段修改为 192.168.1.0，将 vmnet8 中的 IP 段修改为 10.10.1.0

```text
VERSION=1,0
answer VNET_1_DHCP yes
answer VNET_1_DHCP_CFG_HASH 305D3393C78096F94C8C979DF2321B14BEE94AB1
answer VNET_1_HOSTONLY_NETMASK 255.255.255.0
answer VNET_1_HOSTONLY_SUBNET 172.16.178.0  # 修改为 192.168.1.0
answer VNET_1_VIRTUAL_ADAPTER yes
answer VNET_8_DHCP yes
answer VNET_8_DHCP_CFG_HASH DE662EAB01380DE3338128A859C717A8F863F3CF
answer VNET_8_HOSTONLY_NETMASK 255.255.255.0
answer VNET_8_HOSTONLY_SUBNET 172.16.24.0  # 修改为 10.10.1.0
answer VNET_8_NAT yes
answer VNET_8_VIRTUAL_ADAPTER yes
```

### 3. 配置网络

执行命令：

```c
sudo /Applications/VMware\ Fusion.app/Contents/Library/vmnet-cli --configure
```

vmnet-cli 将根据上述修改的地址段自动修改 dhcpd.conf 和 nat.conf 中的 IP 地址。

查看 dhcpd.conf 和 nat.conf 配置文件：

```text
cat /Library/Preferences/VMware\ Fusion/vmnet1/dhcpd.conf
cat /Library/Preferences/VMware\ Fusion/vmnet1/nat.conf

cat /Library/Preferences/VMware\ Fusion/vmnet8/dhcpd.conf
cat /Library/Preferences/VMware\ Fusion/vmnet8/nat.conf
```

可以看到配置已经修改成功。

### 4. 启动网络服务

执行命令：

```c
sudo /Applications/VMware\ Fusion.app/Contents/Library/vmnet-cli --start
```

### 5. 验证

执行命令：

```text
ifconfig
```

可以看到 vmnet1 和 vmnet8 的 IP 地址已经更改成功。

### 6. 虚拟机重新获取配置

虚机如果是手动配置的 IP，直接修改即可。

虚机如果是 DHCP，可以直接重启 vmware fusion 和 虚机系统，也可以直接在虚机重新获取地址，比如 Linux 命令行中执行 `sudo dhclient -v -r eth0` ，**eth0** 为对应网卡。



## Q&A

在share with my mac(NAT)的网络连接配置中，主机和客机的相互连接的IP？

由于客机（虚拟机）的网络由主机产生（因为NAT），所以获取客机IP之后，主机可以直接Ping通。

但是客机如何访问主机呢？为此我用主机搭建了http页面，方便客机测试。

我测试了一下用客机的去访问主机的IP，虽然不是通网段，但是可以访问。然后我有测试了客机IP的默认网关，客机的IP为192.168.249.3，我去访问192.168.249.1，发现依旧能访问主机。

综上：主机访问客机：客机IP；客机访问主机：主机IP、客机IP默认网关。