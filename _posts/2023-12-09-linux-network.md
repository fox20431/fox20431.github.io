---
title: linux network
date: 2023-12-09
---

# Linux network

关于网络服务 

- networking
- systemd-networkd

网络工具

- ipconfig
- ip addr

systemd-networkd 更先进



## 创建具有IP地址的虚拟网卡



```
sudo vi /etc/systemd/network/vip.network
```

配置

```shell
# 创建 tun 设备
cat <<EOF > /etc/systemd/network/50-eth1.netdev
[NetDev]
Name=my-virtual-net
Kind=dummy
EOF

# 为 tun 设备指定网络
cat <<EOF > /etc/systemd/network/50-eth1.network
[Match]
Name=eth1

[Network]
Address=47.242.125.68/24
EOF
```

重启

```
sudo systemctl restart systemd-networkd
```

