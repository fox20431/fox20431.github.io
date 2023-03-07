# MiniKube

总之配置的过程非常的难（dan）受（teng）。

## 准备环境

1. 安装

```sh
sudo pacman -S minikube
```

2. 启动

这一步坑非常之多！

首先是镜像拉取的问题！国内的话通过参数需要指定镜像源！在其次就是不指定合适版本也可能面临不能启动！！！

综合下来，这个就是我的启动命令。

```sh
minikube start --image-mirror-country="cn"  --image-repository="registry.cn-hangzhou.aliyuncs.com/google_containers" --kubernetes-version=v1.23.3
```

输出信息也张贴下来：

```
😄  minikube v1.29.0 on Arch 
✨  Automatically selected the docker driver. Other choices: kvm2, ssh
✅  Using image repository registry.cn-hangzhou.aliyuncs.com/google_containers
📌  Using Docker driver with root privileges
❗  Local proxy ignored: not passing HTTP_PROXY=http://127.0.0.1:7890 to docker env.
❗  Local proxy ignored: not passing HTTPS_PROXY=http://127.0.0.1:7890 to docker env.
❗  Local proxy ignored: not passing HTTP_PROXY=http://127.0.0.1:7890 to docker env.
❗  Local proxy ignored: not passing HTTPS_PROXY=http://127.0.0.1:7890 to docker env.
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
❗  minikube was unable to download registry.cn-hangzhou.aliyuncs.com/google_containers/kicbase:v0.0.37, but successfully downloaded docker.io/kicbase/stable:v0.0.37 as a fallback image
🔥  Creating docker container (CPUs=2, Memory=7900MB) ...
❗  Local proxy ignored: not passing HTTP_PROXY=http://127.0.0.1:7890 to docker env.
❗  Local proxy ignored: not passing HTTPS_PROXY=http://127.0.0.1:7890 to docker env.
❗  Local proxy ignored: not passing HTTP_PROXY=http://127.0.0.1:7890 to docker env.
❗  Local proxy ignored: not passing HTTPS_PROXY=http://127.0.0.1:7890 to docker env.
🌐  Found network options:
    ▪ HTTP_PROXY=http://127.0.0.1:7890
    ▪ HTTPS_PROXY=http://127.0.0.1:7890
    ▪ NO_PROXY=localhost,127.0.0.0/8,192.168.0.0/16,::1
    ▪ http_proxy=http://127.0.0.1:7890
    ▪ https_proxy=http://127.0.0.1:7890
    ▪ no_proxy=localhost,127.0.0.0/8,192.168.0.0/16,::1
❗  This container is having trouble accessing https://registry.cn-hangzhou.aliyuncs.com/google_containers
💡  To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
🐳  Preparing Kubernetes v1.23.3 on Docker 20.10.23 ...
    ▪ env NO_PROXY=localhost,127.0.0.0/8,192.168.0.0/16,::1
    > kubectl.sha256:  64 B / 64 B [-------------------------] 100.00% ? p/s 0s
    > kubelet.sha256:  64 B / 64 B [-------------------------] 100.00% ? p/s 0s
    > kubeadm.sha256:  64 B / 64 B [-------------------------] 100.00% ? p/s 0s
    > kubectl:  44.43 MiB / 44.43 MiB [-------------] 100.00% 6.18 MiB p/s 7.4s
    > kubeadm:  43.12 MiB / 43.12 MiB [--------------] 100.00% 3.57 MiB p/s 12s
    > kubelet:  118.75 MiB / 118.75 MiB [------------] 100.00% 9.28 MiB p/s 13s
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
    ▪ Using image registry.cn-hangzhou.aliyuncs.com/google_containers/storage-provisioner:v5
🌟  Enabled addons: storage-provisioner, default-storageclass
🔎  Verifying Kubernetes components...
💡  kubectl not found. If you need it, try: 'minikube kubectl -- get pods -A'
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
```

3. Dashboard查看信息

```sh
minikube dashboard
```

## 使用Kube

1. 安装kube的控制器

```sh
sudo pacman -S kubectl
```

2. 查看`kubectl`信息

```sh
kubectl version
```

张贴一下打印信息：

```
Client Version: version.Info{Major:"1", Minor:"26", GitVersion:"v1.26.2", GitCommit:"fc04e732bb3e7198d2fa44efa5457c7c6f8c0f5b", GitTreeState:"archive", BuildDate:"2023-03-01T12:14:03Z", GoVersion:"go1.20.1", Compiler:"gc", Platform:"linux/amd64"}
Kustomize Version: v4.5.7
Server Version: version.Info{Major:"1", Minor:"23", GitVersion:"v1.23.3", GitCommit:"816c97ab8cff8a1c72eccca1026f7820e93e0d25", GitTreeState:"clean", BuildDate:"2022-01-25T21:19:12Z", GoVersion:"go1.17.6", Compiler:"gc", Platform:"linux/amd64"}
WARNING: version difference between client (1.26) and server (1.23) exceeds the supported minor version skew of +/-1
```

上述内容告知了 client（即kubectl）的版本信息，以及服务器（启动的minikube）版本信息等信息。

3. 启动一个nginx的pod

```sh
kubectl run ngx --image=nginx:alphine
```

执行命令后会拉取镜像会须要些时间，可以通过下述命令查看所有pod当前状态概览：

```sh
kubectl get pod
```

使用该命令可以查看指定pod更详尽的内容，包括进度：

```sh
kubectl describe pod ngx
```

