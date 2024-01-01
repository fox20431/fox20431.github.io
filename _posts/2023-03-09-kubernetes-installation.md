---
title: kubernetes installation
date: 2023-12-25
---



# Kubernetes Installation

Debian Version: 11

不同发行版的安装大同小异。

以下镜像均拉去自阿里云，如需修改请自行修改。

参考：

- https://snapshooter.com/learn/linux/install-kubernetes

## Intalling kubeadm

为了规避GFW带来的网络问题，下面教程将针对阿里云K8S镜像站进行配置；如果你想要使用官方的镜像请查[官方文档](https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/)。

镜像配置帮助信息：

- [阿里云镜像站地址](https://mirrors.aliyun.com/kubernetes/)
- [阿里云镜像站使用教程](https://developer.aliyun.com/mirror/kubernetes/)

**Install rrerequisite utils**

```sh
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl gpg
```

**Add the appropriate Kubernetes `apt` repository **

```sh
# 添加阿里的 kubernetes 的 apt 镜像源
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
   # containerd责任之一就是拉取镜像
   # 由于国内无法下载registry.k8s.io的镜像，修改sandbox_image的值为阿里云的镜像
   sudo sed -i "s#k8s.gcr.io/pause#registry.cn-hangzhou.aliyuncs.com/google_containers/pause#g" /etc/containerd/config.toml
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
# 开启内核模块（当前会话生效）
# net.bridge.bridge-nf-call-iptables 需要开启这个模块
modprobe br_netfilter
modprobe ip_vs_rr

# 开机默认开启内核模块（模块持久化）
grep -q "br_netfilter" /etc/modules || echo "br_netfilter" | sudo tee -a /etc/modules
grep -q "ip_vs_rr" /etc/modules || echo "ip_vs_rr" | sudo tee -a /etc/modules


# 配置内核参数（当前会话生效）
# Swappiness 的取值范围是 0 到 100
# 当 Swappiness 为 0 时，操作系统会尽量避免使用交换空间，只有在绝对必要的情况下才会发生页面置换。
sysctl vm.swappiness=0
sysctl net.ipv4.ip_forward=1
sysctl net.bridge.bridge-nf-call-iptables=1
sysctl net.bridge.bridge-nf-call-ip6tables=1
# 持久化内核参数
grep -q "vm\.swappiness=0" /etc/sysctl.conf || echo "vm.swappiness=0" | sudo tee -a /etc/sysctl.conf
grep -q "net\.ipv4\.ip_forward=1" /etc/sysctl.conf || echo "net.ipv4.ip_forward=1" | sudo tee -a /etc/sysctl.conf
grep -q "net\.bridge\.bridge-nf-call-iptables=1" /etc/sysctl.conf || echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee -a /etc/sysctl.conf
grep -q "net\.bridge\.bridge-nf-call-ip6tables=1" /etc/sysctl.conf || echo "net.bridge.bridge-nf-call-ip6tables=1" | sudo tee -a /etc/sysctl.conf

# 应用内核参数的配置文件
# sudo sysctl -p
# 或者系统级别应用内核配置文件
# sudo sysctl --system
```

**设置虚拟网卡（针对于公网）**

比如阿里云，其公网IP是通过内网地址使用NAT技术手段转换成公网，因此在VPS中无法生成具有公网的IP网卡，这就会导致进行 `kubeadm init`  所指定的公网IP `kubelet` 无法与其通信，所以我们需要创建一个虚拟化网卡。

这里推荐 `systemd-networkd` （比 `networking` 更好）。

```sh
# 创建设备
cat <<EOF > /etc/systemd/network/vip.netdev
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
    # --pod-network-cidr：pod网段，默认10.244.0.0/16
    # --service-cidr：service网段，默认10.96.0.0/12
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
    # 如果有cni则需要删除如下文件夹，比如安装过flannel
    rm -rf /etc/cni/net.d/
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

由于上述配置仅用了了网络分配，获取节点是会出现状态为 `NotReady`：

```sh
root@main:~# kubectl get nodes
NAME     STATUS     ROLES           AGE     VERSION
main     NotReady   control-plane   3m24s   v1.28.2
node-1   NotReady   <none>          5s      v1.28.2
```

flannel 会自动配置各个节点的网络。

获取配置内容：

```sh
wget https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
```

编辑 `kube-flannel.yml` ，使其 `net-conf.json` 对象中的 `Network` 值与kubeadm启动时的设置的 `--pod-network-cidr` 保持一致。

然后应用配置文件：

```sh
kubectl apply -f kube-flannel.yml
```

## Create the First Pod

1. 创建POD

    编辑名为 `nginx.yml` 的POD配置文件：

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

    让POD配置文件生效：

    ```sh
    kubectl apply -f nginx.yml
    ```

2. 检验 POD 是否可用

    查看Pod状态，如果为 `Running` 则表示正在运行：

    ```
    $ kubectl get pods nginx -o wide
    
    NAME    READY   STATUS    RESTARTS   AGE   IP           NODE     NOMINATED NODE   READINESS GATES
    nginx   1/1     Running   0          19m   10.244.1.9   node-1   <none>           <none>
    ```

    **在 pod 运行的节点上**运行下述命令，检查服务是否正常工作：

    ```sh
    curl 10.244.1.9:80
    ```

     可以获取Nginx的返回的默认HTML页面。

3. （可选）映射POD端口到宿主机上

   这是Service的工作，我们可以新建针对该功能的Service新文件，也可以对 `nginx.yml` 文件追加如下内容：

   ```yaml
   --- # split two configurations
   # Create the service to route the network traffic
   apiVersion: v1
   kind: Service
   metadata:
     name: nginx-service
   spec:
     selector:
       app: nginx
     ports:
       - protocol: TCP
         port: 80
         nodePort: 30001
     type: NodePort
   ```

## Advanced

### 启动针对kubectl的补全

安装 `bash-completion` ，启用自动不全特性：

```sh
echo 'source <(kubectl completion bash)' >>~/.bashrc
```

### Namespace 特性介绍

> In Kubernetes, *namespaces* provides a mechanism for isolating groups of resources within a single cluster.	
>
> From kubernetes doc

namespace为单一集群提供了将资源隔离成组的一个方法。

```sh
# 查看所有的 namespace
kubectl get namespaces
# 删除指定的 namespace
kubectl delete namespace <namespace_name>
# 获取指定namespace的所有pods节点
kubectl get pods --namespace=ingress-nginx
```

### Nignx Ingress

[Ingress Nginx 安装文档](https://kubernetes.github.io/ingress-nginx/deploy/)

**对于有网络问题的建议看下如下教程！！！**

虽然执行 `--dry-run` 成功，他仅代表在 `control plane` 能成功，实际上部署的 pod 是运行在 worker 节点上的，这时候可能会因为 worker 的网络环境导致执行不成功（比如国内网络环境）。

with `kubectl apply`, using YAML manifests.

1. 拉取部署配置文件

    ```sh
    wget https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml
    ```

2. 更换无法拉去的镜像地址

    ```sh
    # registry.k8s.io 国内无法访问，更换为k8s.dockerproxy.com镜像站
    sed -i "s#registry.k8s.io#k8s.dockerproxy.com#g" deploy.yaml
    ```

3. 应用修改后的配置文件

    ```sh
    kubectl apply -f deploy.yaml
    ```

运行完后还有问题，

> Error from server (InternalError): error when creating "yaml/xxx/xxx-ingress.yaml": Internal error occurred: failed calling webhook "validate.nginx.ingress.kubernetes.io": Post https://ingress-nginx-controller-admission.ingress-nginx.svc:443/extensions/v1beta1/ingresses?timeout=30s: Temporary Redirect

解决方案：

```sh
kubectl delete -A ValidatingWebhookConfiguration ingress-nginx-admission
```

参考

https://stackoverflow.com/questions/61616203/nginx-ingress-controller-failed-calling-webhook

### (Optional) Install Helm - K8S Automate Tool

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

### Plugin Recommand

### 安装Dashboard UI（推荐）

官方教程：https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/#deploying-the-dashboard-ui

### 安装Prometheus（推荐）

[Prometheus](https://github.com/prometheus-operator/kube-prometheus/tree/main)
