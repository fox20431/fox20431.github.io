# Virt Network

Linux配置虚拟网络

参考：https://linuxconfig.org/configuring-virtual-network-interfaces-in-linux

## Config

Step 1: Start off by enabling the `dummy` kernel module with the following command. 

```sh
sudo modprobe dummy
```

Step 2: Now that the module has been loaded, we can create a new virtual interface. Feel free to name yours however you want, but we will name ours `eth0` in this example. 

```sh
sudo ip link add eth0 type dummy
```

You will be able to verify that the link was added by executing the following command afterwards:

```sh
ip link show eth0
```

Step 3: We have our virtual interface, but it’t not much use to us without an IP address or MAC address. Let’s give the interface a MAC address with the following command. Feel free to substitute any address you want to use, as ours is just a randomly generated one. \

```sh
ip link set dev interface address C8:D7:4A:4E:47:50
```

Step 4: We can now add an alias to the interface and configure an it with an IP address. 

```sh
sudo ip addr add 192.168.1.100/24 brd + dev eth0 label eth0:0
```

Step 5: Don’t forget to put the interface up, or it probably won’t be very useful. 

```sh
sudo ip link set dev eth0 up
```

Step 6: You should now be able to use your virtual network interface for whatever you want. You can see the full configuration by viewing the output of the ip a command. 

```sh
ip a
```

Step 7: If the virtual network interface has finished serving its purpose, you can revert all your changes with the following commands. If the virtual network interface has finished serving its purpose, you can revert all your changes with the following commands. 

```sh
sudo ip addr del 192.168.1.100/24 brd + dev eth0 label eth0:0
sudo ip link delete eth0 type dummy
sudo rmmod dummy
```

| 对比的方面       | 虚电路                                         | 数据报                                               |
| ---------------- | ---------------------------------------------- | ---------------------------------------------------- |
| 连接的建立       | 必须有                                         | 不要                                                 |
| 目的站地址       | 仅在连接建立阶段使用，每个分组使用短的虚电路号 | 每个分组都有目的站的全地址                           |
| 路由选择         | 在虚电路连接建立时进行，所有分组均按同一路由   | 每个分组独立选择路由                                 |
| 当路由器出故障   | 所有通过了出故障的路由器的虚电路均不能工作     | 出故障的路由器可能会丢失分组，一些路由可能会发生变化 |
| 分组的顺序       | 总是按发送顺序到达目的站                       | 到达目的站时可能不按发送顺序                         |
| 端到端的差错处理 | 由通信子网负责                                 | 由主机负责                                           |
| 端到端的流量控制 | 由通信子网负责                                 | 由主机负责                                           |