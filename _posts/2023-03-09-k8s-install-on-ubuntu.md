# Install K8S on Ubuntu

Ubuntu Version: 22.04

参考：

- https://www.cnblogs.com/Gdavid/p/13353714.html
- https://blog.csdn.net/qq_32596527/article/details/127735327

## 系统设置

为满足K8S的运行条件，我们需要对系统进行设置。

```sh
# 关闭swap分区
sudo swapoff -a
# 从文件系统表中注释掉swap分区，防止重启swap分区自动生效
sudo sed -i '/ swap / s/^(.*)$/#1/g' /etc/fstab
```

修改内核参数：

```sh
sudo tee /etc/modules-load.d/containerd.conf <<EOF
overlay
br_netfilter
EOF

sudo modprobe overlay
sudo modprobe br_netfilter
```

<!-- ```
sudo tee /etc/sysctl.d/kubernetes.conf <<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
``` -->

## 配置镜像

这里需要配置 Docker 和 K8S 两个镜像。

配置Docker镜像：

```sh
# 添加源
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
# 安装源对应的PGP公钥用于验证安装包的完整
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmour -o /etc/apt/trusted.gpg.d/docker.gpg
```

配置K8S镜像：

```sh
# 添加源
sudo apt-add-repository "deb https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main"
# 安装源对应的GPG公钥，最后的公钥指纹（标识符）可以根据情况更换
gpg --keyserver keyserver.ubuntu.com --recv B53DC80D13EDEF05
gpg --export B53DC80D13EDEF05 | sudo tee /etc/apt/trusted.gpg.d/B53DC80D13EDEF05.gpg >/dev/null
```

添加源后不要忘了更新：

```sh
sudo apt update
```

## 安装


### 实用工具

```sh
sudo apt install -y curl gnupg2 software-properties-common apt-transport-https ca-certificates
```

### Containerd

```sh
sudo apt install -y containerd.io
# 如果还想保留docker，请选择没冲突的docker-ce，而不是docker.io
# sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```

修改containerd的配置：

```sh
containerd config default | sudo tee /etc/containerd/config.toml >/dev/null 2>&1
# 配置镜像
sudo sed -i "s#registry.k8s.io/pause#registry.cn-hangzhou.aliyuncs.com/google_containers/pause#g" /etc/containerd/config.toml
# 开启SystemdCgroup
sudo sed -i "s#SystemdCgroup = false#SystemdCgroup = true#g" /etc/containerd/config.toml
```

启动containerd

```sh
sudo systemctl restart containerd
sudo systemctl enable containerd
```

### 安装K8S组件

```sh
sudo apt install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

配置K8S网络：

```sh
sudo tee /etc/sysctl.d/kubernetes.conf <<EOF
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
EOF
```

使配置生效：

```sh
sudo sysctl --system
```

## 运行

控制面板的初始化（主节点）

```sh
# sudo kubeadm init
# 国内初始化很大可能性会卡在拉取的过程中，我们可以通过指定镜像地址解决这个问题
sudo kubeadm init --image-repository registry.aliyuncs.com/google_containers
```

完成后，根据终端输出的内容配置：

```sh
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

同时根据终端输出指定命令，我们可以将其他节点加入该集群中，集群在运行前的操作都相同，仅在kubeadm启动使使用控制面板初始化输出的命令内容，内容如下（我加了sudo确保运行权限）：

```sh
sudo kubeadm join 192.168.122.144:6443 --token qbnvdw.3hjczrqx8cc4ut08 \
	--discovery-token-ca-cert-hash sha256:dbca80fed10f3f35324c4f595e3b43fe85af0af7c3a601607ef876b40a6aec33
```

这时候通过`kubectl get nodes`查看节点状态均为 NotReady ，需要安装网络插件flannel：

从[Github Kube-Flannel](https://github.com/flannel-io/flannel/blob/master/Documentation/kube-flannel.yml)页面获取yaml内容，任意命名，这里命名为`kube-flannel.yaml`，应用该配置：

*值得注意的是yaml的key中net-conf.json要与k8s的cidr保持一致！*

```sh
kubectl apply -f kube-flannel.yaml
```

### 注意

运行过程中的任意不对地方都可以通过下述命令从初始化重新开始：

```sh
kubeadm reset -f
```



