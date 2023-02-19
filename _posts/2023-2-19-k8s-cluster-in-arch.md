# Build K8S Cluster in Arch

ref: https://wiki.archlinux.org/title/Kubernetes

## Install

```sh
sudo pacman -S containerd kubernetes-control-plane kubernetes-node kubeadm kubelet kubectl helm
yay -S etcd
```

Service:

```sh
sudo systemctl enable containerd && sudo systemctl restart containerd
```

## Config

`/etc/sysctl.d/50-kubelet.conf`

```conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
net.ipv4.ip_forward = 1
```

command

```sh
echo 1 >> /proc/sys/net/ipv4/ip_forward
modprobe overlay
modprobe br_netfilter

systemctl enable kubelet && systemctl restart kubelet
```
