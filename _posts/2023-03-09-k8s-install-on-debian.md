# Install K8S on Ubuntu

Debian Version: 11

不同发行版的安装大同小异。

参考：

- https://snapshooter.com/learn/linux/install-kubernetes

## 系统设置

为满足K8S的运行条件，我们需要对系统进行设置。

```sh
# 关闭swap分区
sudo swapoff -a
# 从文件系统表中注释掉swap分区，防止重启swap分区自动生效
sudo sed -i '/ swap / s/^(.*)$/#1/g' /etc/fstab
```

## 配置镜像

这里需要配置 Docker 和 K8S 两个镜像。

配置Docker镜像：

```sh
curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list
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

如果安装了Docker，也需要配置对应源和操作配置`/etc/docker/daemon.json`：


```sh
{
    "registry-mirrors": ["https://hnkfbj7x.mirror.aliyuncs.com"],
    "exec-opts": ["native.cgroupdriver=systemd"]
}
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
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --image-repository registry.aliyuncs.com/google_containers
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

如果打印信息忘记了，没关系，可以使用下述命令再次打印出来：

```sh
kubeadm token create --print-join-command
```

运行过程中的任意不对地方都可以通过下述命令从初始化重新开始：

```sh
kubeadm reset -f
```

## Helm

上述问题就在于配置文件多繁杂，而且不能够一键部署，其次可能遇到网络问题。

helm类似包管理可以解决这个问题。

给helm更换阿里云镜像：

```sh
helm repo add stable  https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts/
```

查看镜像列表：

```sh
helm repo list
```

## 插件

通过`kubectl get nodes`查看节点状态均为 NotReady ，因为需要安装网络插件flannel：

### flannel(必须)

**手动安装**

从[Github Kube-Flannel](https://github.com/flannel-io/flannel/blob/master/Documentation/kube-flannel.yml)页面获取yaml内容，任意命名，这里命名为`kube-flannel.yaml`，应用该配置：

*值得注意的是yaml的key中net-conf.json要与kubeadm启动时的设置的--pod-network-cidr保持一致！*

```sh
kubectl apply -f kube-flannel.yaml
```

**helm安装（推荐）**

```sh
helm install flannel --set podCidr="10.244.0.0/16" https://github.com/flannel-io/flannel/releases/latest/download/flannel.tgz
```

更多可看：https://github.com/flannel-io/flannel#deploying-flannel-manually

### 安装Dashboard UI（推荐）

查看该教程！https://www.yuque.com/xuxiaowei-com-cn/gitlab-k8s/k8s-dashboard


### 安装Prometheus（推荐）

[Prometheus](https://github.com/prometheus-operator/kube-prometheus/tree/main)

拉取配置：

```sh
wget https://github.com/prometheus-operator/kube-prometheus/archive/refs/tags/v0.12.0.tar.gz
```

解压缩：

```sh
tar -xzvf v0.12.0.tar.gz
```

由于网络环境问题，需要对image的地址进行更换。

首先进入到工作目录文件：

```sh
cd ./kube-prometheus-0.12.0/manifests
```

定位需要修改的文件（文本内容含有境外源，这里主要是`quay.io|k8s.gcr|grafana/`）：

```sh
# -i 忽略大小写
# -r 递归
# -E 正则
grep -riE 'quay.io|k8s.gcr|grafana/' *
```

然后将定位到的文件进行替换：

```sh
sed -i 's/quay.io/quay.mirrors.ustc.edu.cn/g' <file>
sed -i 's/k8s.gcr.io/lank8s.cn/g' <file>
grep "image: " * -r		# 确认一下是否还有国外镜像
```
