---
title: linux transparent proxy with xray
date: 2024-01-06
---

# Linux 透明代理

## 透明代理是什么

什么是透明代理（tproxy，Transparent Proxy），其本质就是不再使用端对端（以及协议对协议，属于应用层）传输；而透明代理则代理整个网卡（属于传输层），所有经过网卡的流量均会走代理，这个技术的底层由Linux内核的TPROXY功能支持。

## 方案思路

参考：https://xtls.github.io/document/level-2/tproxy_ipv4_and_ipv6.html

大致思路是使用：使用Netfilter（Linux内核提供的网络操作相关的框架）的工具iproutes，ipnftables（iptables替代品），将网络请求全部路由到xray进行代理。

## Xray配置

### 客户端

```json
{
  "log": {
    "loglevel": "warning"
  },
  "inbounds": [
    {
      "tag": "all-in",
      "port": 12345,
      "protocol": "dokodemo-door",
      "settings": {
        "network": "tcp,udp",
        "followRedirect": true
      },
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls", "quic"]
      },
      "streamSettings": {
        "sockopt": {
          "tproxy": "tproxy"
        }
      }
    },
    {
      "port": 10808,
      "protocol": "socks",
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls", "quic"]
      },
      "settings": {
        "auth": "noauth",
        "udp": true
      }
    },
    {
      "port": 10809,
      "protocol": "http"
    }
  ],
  "outbounds": [
    {
      "tag": "proxy",
      "protocol": "<protocol>",
      // proxy setting
      "streamSettings": {
        // proxy config
        "sockopt": {
          "mark": 255
        }
      }
    },
    {
      "tag": "direct",
      "protocol": "freedom",
      "settings": {
        "domainStrategy": "UseIP"
      },
      "streamSettings": {
        "sockopt": {
          "mark": 255
        }
      }
    },
    {
      "tag": "block",
      "protocol": "blackhole",
      "settings": {
        "response": {
          "type": "http"
        }
      }
    },
    {
      "tag": "dns-out",
      "protocol": "dns",
      "streamSettings": {
        "sockopt": {
          "mark": 255
        }
      }
    }
  ],
  "dns": {
    "hosts": {
      "dns.google": ["8.8.8.8", "8.8.4.4"],
      "connect.hihusky.com": "212.50.249.175"
    },
    "servers": [
      "1.1.1.1",
      "8.8.8.8",
      {
        "address": "223.5.5.5",
        "port": 53,
        "domains": ["geosite:cn"]
      },
      "https://1.1.1.1/dns-query",
      "https://8.8.8.8/dns-query",
      "localhost"
    ]
  },
  "routing": {
    "domainMatcher": "hybrid",
    "domainStrategy": "IPOnDemand",
    "rules": [
      {
        "type": "field",
        "inboundTag": ["all-in"],
        "port": 53,
        "network": "udp",
        "outboundTag": "dns-out"
      },
      {
        "type": "field",
        "protocol": ["bittorrent"],
        "outboundTag": "direct"
      },
      {
        "type": "field",
        "ip": [
					"1.1.1.1",
 					"8.8.8.8"
				],
        "outboundTag": "proxy"
      },
      {
        "type": "field",
        "domain": [
          "geosite:geolocation-!cn",
          "domain:googleapis.cn",
          "dns.google"
        ],
        "outboundTag": "proxy"
      },
      {
        "type": "field",
        "ip": [
          "geoip:private", 
          "geoip:cn",
		  		"223.5.5.5",
          "212.50.249.175"
        ],
        "outboundTag": "direct"
      },
      {
        "type": "field",
        "domain": [
          "geosite:private",
          "geosite:cn",
          "geosite:category-games@cn",
          "domain:hihusky.com",
          "domain:iimn.net"
        ],
        "outboundTag": "direct"
      },
      {
        "type": "field",
        "domain": ["geosite:category-ads-all"],
        "outboundTag": "block"
      }
    ]
  }
}
```

### 服务端

正常配置，无额外要求。

## 系统设置

### 手动

设置：

```sh
# 设置策略路由 v4
sudo ip rule add fwmark 1 table 100
sudo ip route add local 0.0.0.0/0 dev lo table 100

# 设置策略路由 v6
sudo ip -6 rule add fwmark 1 table 106
sudo ip -6 route add local ::/0 dev lo table 106
```


这四行行代码是用于在Linux系统中设置路由表和规则的命令，通常用于配置网络路由和流量控制。让我解释一下这两行代码的作用：

1. `sudo ip route add local default dev lo table 100`：

   - `sudo`: 以超级用户权限执行命令。
   - `ip`: 是用于配置网络设备和路由表的工具。
   - `route add`: 添加路由表项的命令。
   - `local default`: 表示将所有本地流量（Local）指向默认（Default）的本地回环设备（lo），即路由到本地机器上。
   - `dev lo`: 指定本地回环设备作为出口接口，表示流量不会通过实际的网络接口，而是在本地环回。
   - `table 100`: 将该路由表项添加到表号为100的路由表中。

   这一行代码的作用是将所有本地流量通过本地回环设备处理，并将相关路由表项添加到表号为100的路由表中。

2. `sudo ip rule add fwmark 1 table 100`：

   - `sudo`: 以超级用户权限执行命令。
   - `ip rule add`: 添加规则到路由策略数据库。
   - `fwmark 1`: 使用防火墙标记（Firewall Marking）为1的规则。
   - `table 100`: 指定当符合规则条件时使用路由表号为100的路由表。

   当流量的防火墙标记（fwmark）为1时，将使用路由表号为100的路由表处理这些流量。

撤销上述操作：

```sh
sudo ip route del local default dev lo table 100
sudo ip rule del fwmark 1 table 100

sudo ip -6 rule del fwmark 1 table 106
sudo ip -6 route del local ::/0 dev lo table 106
```

一般流量进入会根据rule的有先进选择不同的路由表进行转发，通过 `sudo ip rule show` 可以查看路由表从上到下的优先级，根据上述可知 `fwmark` 为 `1` 的回去查看 `table 100` 的 `route` 规则，该规则会将流量导入到本地（xray将所有指向本地的流量进行透明代理），但在导入到本地的时候遵守防火墙的规则，我们需要通过nftables进行配置。

创建 `/etc/nftables/xray.conf` ，写入：

```conf
#!/usr/sbin/nft -f

flush ruleset

table inet xray {

        chain prerouting {
                type filter hook prerouting priority 0
                policy accept
                # don't handle the packages that the destination is current computer.
                ip daddr { 127.0.0.0/8, 224.0.0.0/4, 255.255.255.255 } return
                ip6 daddr { ::1, fe80::/10 } return
                # exclude the docker
                ip daddr { 172.16.0.0/12 } return
                # exclude the virtual machine
                ip daddr { 192.168.122.0/24 } return
                # don't handle the packages that the destination is device in wlan, but dns
                meta l4proto tcp ip daddr 192.168.0.0/16 return
                meta l4proto tcp ip6 daddr fd00::/8 return
                ip daddr 192.168.0.0/16 udp dport != 53 return
                ip6 daddr fd00::/8 udp dport != 53 return
                # don't handle the packages marked 255, 255 mark express the package has been handled by xray.
                meta mark 255 return
                # if the above rules are not matched, the packages are accepted by 12345 which is opened by xray.
                meta l4proto { tcp, udp } tproxy ip to 127.0.0.1:12345 accept
                meta l4proto { tcp, udp } tproxy ip6 to [::1]:12345 accept
        }

        chain output {
                type route hook output priority 0
                policy accept
                # don't handle dns and mdns
                ip protocol udp udp dport { 53, 5353 } return
                # don't handle the packages that the destination is current computer.
                ip daddr { 127.0.0.0/8, 224.0.0.0/4, 255.255.255.255 } return
                ip6 daddr { ::1, fe80::/10 } return
                # exclude the docker
                ip daddr { 172.16.0.0/12 } return
                # exclude the virtual machine
                ip daddr { 192.168.122.0/24 } return
                # don't handle the packages that the destination is device in wlan, but dns
                meta l4proto tcp ip daddr 192.168.0.0/16 return
                meta l4proto tcp ip6 daddr fd00::/8 return
                ip daddr 192.168.0.0/16 udp dport != 53 return
                ip6 daddr fd00::/8 udp dport != 53 return
                # don't handle the packages marked 255, 255 mark express the package has been handled by xray.
                meta mark 255 return
                # if the above rules are not matched, the packages is marked 1
                # packages marked 1 are send to 'lo' by the table, then follow prerouting chains rules
                meta l4proto { tcp, udp } meta mark set 1 accept
        }

        chain divert {
                type filter hook prerouting priority mangle; policy accept;
                meta l4proto tcp socket transparent 1 meta mark set 1 accept
        }
}
```

`meta mark 0x000000ff return` 与xray客户端设置的 `mark` 为 `255` 有关，两者相互约束防止形成无法终止的循环。

执行命令应用防火墙规则：

```sh
nft -f /etc/nftables/xray.conf
```

### 自动

为了让上述开机自启动， `/etc/systemd/system/` 目录下创建一个名为 `tproxyrules.service`：

```
[Unit]
Description=Tproxy rules

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=/sbin/ip rule add fwmark 1 table 100 ; \
/sbin/ip -6 rule add fwmark 1 table 106 ; \
/sbin/ip route add local 0.0.0.0/0 dev lo table 100 ; \
/sbin/ip -6 route add local ::/0 dev lo table 106 ; \
/sbin/nft -f /etc/nftables/xray.conf
ExecStop=/sbin/ip rule del fwmark 1 table 100 ; \
/sbin/ip -6 rule del fwmark 1 table 106 ; \
/sbin/ip route del local 0.0.0.0/0 dev lo table 100 ; \
/sbin/ip -6 route del local ::/0 dev lo table 106 ; \
/sbin/nft flush ruleset

[Install]
WantedBy=multi-user.target
```

## 原理

正常情况下netfilter收发报要经历以下hooks。

发：

output -> 

收：

prerouting -> input -> 



上述规则配置根据判断 mark 的位置使得我们发送包的流向改变了

发：

output -> mark 1 -> lo -> prerouting -> xray -> 

## 问题

Ping会很久

使用：

```
ping -n domain
```

禁止反向DNS解析就可以解决。



## TODO

ping 国内地址DNS路由有问题，表现为速度很慢。

https://wiki.nftables.org/wiki-nftables/index.php/Configuring_chains
