# Linux Network Setting

对于网络地址的获取一般存在两种途径，动态和静态。

动态获取使用的是DHCP，其通过网关和主机都支持的DHCP协议来沟通获取地址，避免了IP冲突。

静态获取由主机设置IP，可能存在冲突。

## 动态IP

Linux下使用DHCP协议很简单，及安装`dhcpcd`并用`systemctl`启动它。

## 静态IP

对于静态IP的设置，要看使用的网络管理是什么。

### for Systemd-Networkd

该网络管理为 Systemd 自带的网络管理，常见于 Arch 发行版。

配置方法很简单，只需要修改 `/etc/systemd/network/<name>.network`

```conf
# special configuration for office WiFi network
[Match]
Name=wlp2s0
SSID=office_ap_name
#BSSID=aa:bb:cc:dd:ee:ff

[Network]
Address=10.1.10.9/24
Gateway=10.1.10.1
DNS=10.1.10.1
#DNS=8.8.8.8
```
然后重启服务

```sh
# 建议开启
sudo systemctl enable systemd-networkd.service
sudo systemctl restart systemd-networkd.service
```

### for Netplan

对于使用 netplan 作为网络管理器的 Linux 发行版（比如Ubuntu）设置静态IP方式如下：

```sh
cd /etc/netplan/
```

```sh
cat 00-installer-config.yaml
```

```sh
sudo vim /etc/netplan/00-installer-config.yaml
```

```yaml
network:
  renderer: networkd
  ethernets:
    eth0:
      addresses:
        - 192.168.1.247/24
      nameservers:
        addresses: [4.2.2.2, 8.8.8.8]
      routes:
        - to: default
          via: 192.168.1.1
  version: 2
```

`network.ethernets.routes[1].via` 表示的是网关，再 `NAT` 已经分配好 IP 的情况下可以通过 `ip route` 查看。

让配置文件生效：

```
sudo netplan apply
```

refer：https://www.linuxtechi.com/static-ip-address-on-ubuntu-server/


### for Networking

典型代表，debian

修改配置文件

```sh
vim /etc/network/interfaces
```

将dhcp替换成静态ip

```sh
iface eth0 inet dhcp
```

```sh
iface eth0 inet static
address 192.168.122.200
netmask 255.255.255.0
gateway <网关地址>
```

重启服务

```sh
systemctl restart networking
```

如果不行，尝试重启