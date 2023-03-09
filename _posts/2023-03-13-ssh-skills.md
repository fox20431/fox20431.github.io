# SSH 命令行技巧

## 快速连接配置

修改配置文件，设置要SSH服务器：

```sh
vim .ssh/config
```

下面是模板：

```config
host k8s-master
  hostname 192.168.122.200
  user root
  port 22
  identityfile ~/.ssh/id_rsa
```

通过配置连接服务器：

```sh
ssh k8s-master
```

## 通过GitHub为服务器设置authorized_keys

获取指定github公钥

```sh
curl https://github.com/{username}.keys
```

```sh

```