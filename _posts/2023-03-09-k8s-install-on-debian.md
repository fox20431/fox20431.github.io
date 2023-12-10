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
# 这个命令将在/etc/fstab文件中找到包含" swap "的行，并在行首添加"#"，从而将其注释掉。
sudo sed -i '/ swap / s/^(.*)$/#1/g' /etc/fstab
```

## Intalling kubeadm

为了规避GFW带来的网络问题，下面教程将针对阿里云K8S镜像站进行配置。

- [阿里云镜像站地址](https://mirrors.aliyun.com/kubernetes/)
- (阿里云镜像站使用教程)[https://developer.aliyun.com/mirror/kubernetes/]

*如果你想要使用官方的镜像请查[官方文档](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)。*

**Install rrerequisite utils**

```sh
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
```

**Add the  appropriate Kubernetes `apt` repository **

```sh
# 下载GPG密钥并导入APT中
curl -fsSL https://mirrors.aliyun.com/kubernetes/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring-aliyun.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring-aliyun.gpg] https://mirrors.aliyun.com/kubernetes/apt/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
```

**Install k8s**

```sh
sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
systemctl enable --now kubelet
# hold the version
sudo apt-mark hold kubelet kubeadm kubectl
```

## Intalling container runtimes

K8S支持较多的容器运行时，具体可见[Container Runtimes](https://kubernetes.io/docs/setup/production-environment/container-runtimes/)。

这里推荐使用 `containerd` 。

### Containerd

1. Configure Dokcer's apt repository

   Docker 的 `apt` 仓库维护 `containerd` 

    ```sh
   # 卸载 docker apt 仓库包含的包
   for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
   # Add Docker's official GPG key:
   sudo apt-get update
   sudo apt-get install ca-certificates curl gnupg
   sudo install -m 0755 -d /etc/apt/keyrings
   curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
   sudo chmod a+r /etc/apt/keyrings/docker.gpg
   
   # Add the repository to Apt sources:
   echo \
       "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
       $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
   	sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
   
   sudo apt-get update
    ```

2. Insatll containerd

   ```sh
   sudo apt install containerd.io
   sudo systemctl enable --now containerd
   ```

3. Configure containerd

   [Container for K8S Introduce - K8S Official Doc](https://kubernetes.io/docs/setup/production-environment/container-runtimes/#containerd)

   [Containerd for K8S - Containerd Official Doc](https://github.com/containerd/containerd/blob/main/docs/getting-started.md)

   ```sh
   # 将containerd的配置设置为默认模板
   containerd config default | sudo tee /etc/containerd/config.toml >/dev/null 2>&1
   # 用阿里云镜像替换官方镜像
   sudo sed -i "s#registry.k8s.io/pause#registry.cn-hangzhou.aliyuncs.com/google_containers/pause#g" /etc/containerd/config.toml
   # 开启SystemdCgroup
   sudo sed -i "s#SystemdCgroup = false#SystemdCgroup = true#g" /etc/containerd/config.toml
   
   # 重启服务
   sudo systemctl restart containerd
   ```

## Config System to Pass K8S Preflight

**关闭swap分区**

```sh
# 关闭swap分区（仅在当前会话生效）
sudo swapoff -a
# 持久化关闭swap分区
# 从文件系统表中注释掉swap分区，防止重启swap分区自动生效
# 这个命令将在/etc/fstab文件中找到包含" swap "的行，并在行首添加"#"，从而将其注释掉。
sudo sed -i '/ swap / s/^(.*)$/#1/g' /etc/fstab
```

**配置内核模块和内核参数**

```sh
# 开启内核模块
# net.bridge.bridge-nf-call-iptables 需要开启这个模块
modprobe br_netfilter
# 开机默认开启内核模块（模块持久化）
echo "br_netfilter" >> /etc/modules

# 配置内核参数
sysctl net.ipv4.ip_forward=1
sysctl net.bridge.bridge-nf-call-iptables=1
# 持久化内核参数
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.conf
echo "net.bridge.bridge-nf-call-iptables=1" >> /etc/sysctl.conf

# 应用内核参数的配置文件
sudo sysctl -p
# 或者系统级别应用内核配置文件
sudo sysctl --system
```

**设置虚拟网卡（针对于公网）**

比如阿里云，其公网IP是通过内网地址使用NAT技术手段转换成公网，因此在VPS中无法生成具有公网的IP网卡，这就会导致进行 `kubeadm init`  所指定的公网IP `kubelet` 无法与其通信，所以我们需要创建一个虚拟化网卡。

这里推荐 `systemd-networkd` （比 `networking` 更好）。

```sh
# 创建设备
cat <<EOF > /etc/systemd/network/vip.netdev \
[NetDev]
Name=vip
Kind=dummy
EOF

# 为设备指定网络
cat <<EOF > /etc/systemd/network/vip.network
[Match]
Name=vip

[Network]
Address=47.242.125.68/24
EOF

# 重启服务
systemctl restart systemd-networkd
```

## Create the cluster

1. Control Plane Init

    在要设置为控制面板的服务器上执行如下命令：

    ```sh
    # sudo kubeadm init
    # --pod-network-cidr：集群中分给pod网络的IP地址，默认10.244.0.0/16
    # --service-cidr：为Service分配的IP地址，默认10.96.0.0/12
    # --image-repository：指定阿里云镜像，
    # --apiserver-advertise-address 指定公网ip
    sudo kubeadm init --pod-network-cidr=10.244.0.0/16 \
      --service-cidr=10.96.0.0/12 \
      --apiserver-advertise-address 47.242.125.68 \
      --image-repository registry.aliyuncs.com/google_containers
    ```

    完成后，根据终端输出的内容配置：

    ```sh
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ```


2. Nodes join the cluster

   同时根据终端输出指定命令，我们可以将其他节点加入该集群中，集群在运行前的操作都相同，仅在kubeadm启动使使用控制面板初始化输出的命令内容：

    ```sh
    sudo kubeadm join 47.242.125.68:6443 --token qbnvdw.3hjczrqx8cc4ut08 \
        --discovery-token-ca-cert-hash sha256:dbca80fed10f3f35324c4f595e3b43fe85af0af7c3a601607ef876b40a6aec33
    ```

    如果打印信息忘记了，没关系，可以在控制面板服务器（Control Plane Server）使用下述命令再次打印出来：

    ```sh
    kubeadm token create --print-join-command
    ```

3. Check the cluster status

    ```sh
    kubectl get nodes
    ```

**（可选）集群创建帮助信息**

```sh
# 重置kubeadm，适用于：
# 1. kubeadm init 出错
# 2. kubeadm join 出错
kubeadm reset -f

# modify the label
kubectl label node <NODE-NAME> node-role.kubernetes.io/worker=worker
```

## Configure the k8s network

flannel 会自动配置各个节点的网络。

获取配置内容：

```
wget https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
```

编辑 `kube-flannel.yml` ，使其 `net-conf.json` 对象中的 `Network` 值与kubeadm启动时的设置的 `--pod-network-cidr` 保持一致。

然后应用配置文件：

```sh
kubectl apply -f kube-flannel.yml
```

## Create the First Pod

创建 `nginx.yaml` 的pod配置文件：

```yaml

apiVersion: v1
kind: Pod
metadata:
  name: nginx
  # 指定 label，便于检索
  labels:
    app: nginx
spec:
  containers:
  - name: nginx
    # 指定镜像
    image: nginx:alpine
    # 指定暴露端口
    ports:
    - containerPort: 80
```

让pod配置文件生效：

```sh
kubectl apply -f nginx.yaml
```

查看Pod创建进度：

```sh
kubectl get pods nginx -o wide
```

查看pod详细信息

```
kubectl describe pod nginx
```



## Install Helm

`Helm` 是一个在 Kubernetes 上管理应用程序的包管理工具。它允许用户定义、安装和升级 Kubernetes 应用程序，并处理与应用程序相关的所有资源，如部署、服务、持久卷等。

这个安装参考[官方网站](https://helm.sh/docs/intro/install/)：

```sh
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

更换镜像：

```sh
# 阿里云镜像
helm repo add stable https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts/
# 查看镜像列表
helm repo list
```

## Plugin Recommand

### flannel

```sh
helm install flannel --set podCidr="10.244.0.0/16" https://github.com/flannel-io/flannel/releases/latest/download/flannel.tgz
```

更多可看：https://github.com/flannel-io/flannel#deploying-flannel-manually

### 安装Dashboard UI（推荐）

官方教程：https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#deploying-the-dashboard-ui

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
