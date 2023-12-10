---
title: linux firewall tutorial
date: 2023-11-24
---

# Linux 防火墙教程

## nftables

nftables 比 iptables 更新，也更好用。

```sh
sudo apt-get install nftables
sudo systemctl --now enable nftables
```

比如你需要开放22、443端口，你可以编辑`/etc/nftables.conf`写入如下配置：

```sh
#!/usr/sbin/nft -f

flush ruleset

table inet filter {
	chain input {
		type filter hook input priority 0;
		
		# ICMP
		ct state established,related accept
		ip protocol icmp accept
		
		# Common Port
		tcp dport 22 accept
		tcp dport 443 accept

		# allow access to loopback 42222
		iif lo tcp dport 42222 accept

		# allow access to all loopback ports
		iif lo accept
		dropr
	}
	chain forward {
		type filter hook forward priority 0;
	}
    chain output {
		type filter hook output priority 0;
    }
}
```

然后使其生效：

```sh
sudo nft -f /etc/nftables.conf
```

查看

1. **查看规则集：**

   ```sh
   sudo nft list ruleset
   ```

   这个命令将显示当前 `nftables` 的规则集，包括所有表和规则。

2. **查看表信息：**

   ```sh
   sudo nft list tables
   ```

   这个命令将显示当前存在的 `nftables` 表的信息。

3. **查看某个表的规则：**

   ```sh
   sudo nft list table <table_name>
   ```

   用实际的表名称替换 `<table_name>`，以查看特定表的规则。

4. **查看计数器信息：**

   ```
   bashCopy code
   sudo nft list counters
   ```

   这个命令将显示计数器的信息，包括数据包和字节的计数。

5. **查看元集信息：**

   ```
   bashCopy code
   sudo nft list sets
   ```