---
title: Install K8S on Debian
---



# Install K8S on Debian

Debian Version: 11

不同发行版的安装大同小异。

以下镜像均拉去自阿里云，如需修改请自行修改。

参考：

- https://snapshooter.com/learn/linux/install-kubernetes

## 系统设置

为满足K8S的运行条件，我们需要对系统进行设置。

```sh
# 关闭swap分区
sudo swapoff -a
# 从文件系统表中注释掉swap分区，防止重启swap分区自动生效
# 这个命令有时候不生效，建议去/etc/fstab中确认一下
sudo sed -i '/ swap / s/^(.*)$/#1/g' /etc/fstab
```

## 安装K8S

为了规避GFW带来的网络问题，接下来将针对[阿里云K8S镜像站](如果你想要安装官方的镜像请查[the official documentation](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)。)进行配置。如果你想要使用官方的镜像请查[官方文档](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)。

**安装实用工具**

```sh
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl
```

**配置K8S镜像**

```sh
# 下载GPG密钥并导入APT中
curl -sSL https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /usr/share/keyrings/kubernetes-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/kubernetes-archive-keyring.gpg] https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

```

**安装k8s**

```sh
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

## 安装

### Containerd

```sh
sudo apt install -y containerd.io
# 如果还想保留docker，请选择没冲突的docker-ce，而不是docker.io(docker.io已经停止维护了)
```

修改containerd的配置：

```sh
# 将containerd的配置设置为默认模板
containerd config default | sudo tee /etc/containerd/config.toml >/dev/null 2>&1
# 用阿里云镜像替换官方镜像
sudo sed -i "s#registry.k8s.io/pause#registry.cn-hangzhou.aliyuncs.com/google_containers/pause#g" /etc/containerd/config.toml
# 开启SystemdCgroup
sudo sed -i "s#SystemdCgroup = false#SystemdCgroup = true#g" /etc/containerd/config.toml
```

启动containerd

```sh
sudo systemctl restart containerd
sudo systemctl enable containerd
```

使配置生效：

```sh
sudo sysctl --system
```

## 运行

### 主节点的控制面板的初始化

**THERE BE DRAGONS:**

一般服务器是没有公网网卡的（只有内网），但是k8s要想在公网搭建集群，需要公网网卡，通过下书命令可以创建虚拟的公共网网卡：

```sh
sudo ifconfig eth0:1 192.168.175.128
```

运行

```sh
# sudo kubeadm init
# --pod-network-cidr：集群中分给pod网络的IP地址，默认10.244.0.0/16
# --service-cidr：为Service分配的IP地址，默认10.96.0.0/12
# --image-repository：指定阿里云镜像，
# --apiserver-advertise-address 指定公网ip
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 \
  --service-cidr=10.96.0.0/12 \
  --apiserver-advertise-address 192.168.175.128 \
  --image-repository registry.aliyuncs.com/google_containers
```

完成后，根据终端输出的内容配置：

```sh
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

### 从节点加入到集群中

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

### 检查集群节点

通过下述命令可以检测集群状态

```sh
kubectl get nodes
```

## Helm

后续安装插件会遇到各种问题，比如配置文件繁杂、不能够一键部署、网络问题等等。helm`类似包管理可以解决这个问题。

这个安装参考[官方网站](https://helm.sh/docs/intro/install/)：

```sh
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

给helm更换阿里云镜像：

```sh
helm repo add stable  https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts/
```

查看镜像列表：

```sh
helm repo list
```

## 插件

这里推荐一些需要安装的插件，以便后续操作。

### flannel(必须)

通过`kubectl get nodes`查看节点状态均为 `NotReady` ，因为需要安装网络插件flannel。

flannel 会自动配置各个节点的网络。

**手动安装**

从[Github Kube-Flannel](https://github.com/flannel-io/flannel/blob/master/Documentation/kube-flannel.yml)页面获取yaml内容，任意命名，这里命名为`kube-flannel.yml`，应用该配置：

*值得注意的是yaml的key中net-conf.json要与kubeadm启动时的设置的--pod-network-cidr保持一致！*

```sh
kubectl apply -f kube-flannel.yml
```

**helm安装（推荐）**

```sh
helm install flannel --set podCidr="10.244.0.0/16" https://github.com/flannel-io/flannel/releases/latest/download/flannel.tgz
```

更多可看：https://github.com/flannel-io/flannel#deploying-flannel-manually

### 安装Dashboard UI（推荐）

官方教程：https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#deploying-the-dashboard-ui

国内大神教程：https://www.yuque.com/xuxiaowei-com-cn/gitlab-k8s/k8s-dashboard

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
