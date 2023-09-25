# Virt Tutorial

Virt 是基于 KVM 技术的虚拟化方案，有以下特性：

- KVM是一种基于Linux内核的虚拟化技术，允许在主机操作系统上创建虚拟机。
- KVM通过与Linux内核一起工作，可以实现更高的性能和更好的资源利用率。
- KVM允许直接在宿主机硬件上运行虚拟机，这通常被称为硬件加速虚拟化。这意味着虚拟机可以直接访问主机的硬件资源，从而获得更好的性能。
- 与QEMU相比，KVM在性能和资源利用率方面通常更优秀，特别是在需要高性能虚拟机时。

## Install

下载安装后续需要的工具：

**MacOs**

```sh
brew install gcc qemu virt-manager
brew services restart libvirt
```

**Linux**

```sh
# edk2-ovmf is to support UEFI
# swtpm is to support for TPM
sudo pacman -S qemu virt-manager virt-viewer dnsmasq vde2 bridge-utils openbsd-netcat libguestfs edk2-ovmf swtpm
systemctl start libvirtd
systemctl enable libvirtd
```

## Qemu VS Virt

QEMU和KVM（virt）都是虚拟化技术，但它们的设计目标和特点有所不同。QEMU更注重灵活性和跨平台支持，适用于需要模拟不同架构的情况。KVM（virt）则更专注于在基于Linux的环境中实现高性能的硬件加速虚拟化，适用于需要高性能虚拟机的情况。

### QEMU 创建并启动虚拟机

下载ubuntu镜像并重命名为 `ubuntu.iso` 。

有 `qemu` 已经足够让我们启动虚拟机：

```sh
# 创建存储的介质
qemu-img create -f qcow2 ubuntu.qcow2 20G

# 指定镜像去安装
qemu-system-x86_64 \
    -machine type=q35,accel=hvf \
    -smp 2 \
    -cpu host \
    -hda ubuntu.qcow2 \
    -cdrom ./ubuntu.iso \
    -m 4G

# 启动虚拟机
# 由于使用了MacOS的Hypervisor.framework
# 需要sudo命令
sudo qemu-system-x86_64 \
  -machine type=q35,accel=hvf \
  -M accel=hvf \
  -cpu host \
  -smp 6 \
  -m 16G \
  -hda ~/vm/ubuntu.qcow2 \
  -vga virtio \
  -usb \
  -device usb-tablet \
  -display default,show-cursor=on \
  -nic vmnet-bridged,ifname=en0
```

### VIRT 创建并启动虚拟机

virt相比qemu更简单，同时提供暂停（suspend）和恢复（resume）的等其他功能。

参考[Ubuntu VM on macoS with libvirt + QEMU](https://www.naut.ca/blog/2020/08/26/ubuntu-vm-on-macos-with-libvirt-qemu/)

首先创建`ubuntu.xml`文件：

```xml
<domain type='hvf' xmlns:qemu='http://libvirt.org/schemas/domain/qemu/1.0'>
	<name>ubuntu</name>
	<uuid>2005CB24-522A-4485-9B9A-E60A61D9F8CF</uuid>
	<memory unit='GB'>4</memory>
	<cpu mode='custom'>
		<model>Westmere</model>
	</cpu>
	<vcpu>4</vcpu>
	<features>
		<acpi />
		<apic />
	</features>
	<os>
		<type arch='x86_64' machine='q35'>hvm</type>
		<bootmenu enable='yes' />
	</os>
	<clock offset='localtime' />
	<on_poweroff>destroy</on_poweroff>
	<on_reboot>restart</on_reboot>
	<on_crash>destroy</on_crash>
	<pm>
		<suspend-to-mem enabled='no' />
		<suspend-to-disk enabled='no' />
	</pm>
	<devices>
		<emulator>/usr/local/bin/qemu-system-x86_64</emulator>
		<controller type='usb' model='ehci' />
		<disk type='file' device='disk'>
			<driver name='qemu' type='qcow2' />
			<source file='/Users/ming/vms/ubuntu.qcow2' />
			<target dev='vda' bus='virtio' />
		</disk>
		<disk type='file' device='cdrom'>
			<source file='/Users/ming/vms/ubuntu.iso' />
			<target dev='sdb' bus='sata' />
		</disk>
		<console type='pty'>
			<target type='serial' />
		</console>
		<input type='tablet' bus='usb' />
		<input type='keyboard' bus='usb' />
		<graphics type='vnc' port='5900' listen='127.0.0.1' />
		<video>
			<model type='virtio' vram='16384' />
		</video>
	</devices>
	<seclabel type='none' />
	<qemu:commandline>
		<qemu:arg value='-machine' />
		<qemu:arg value='type=q35' />
	</qemu:commandline>
</domain>
```

libvirt无法配置网络，原因不明，网上参考也比较少。

然后使用下述命令定义一个虚拟机：

```sh
virtsh define ubuntu.xml
```

然后启动该虚拟机：

```sh
virsh start ubuntu
```

这里的`ubuntu`为`ubuntu.xml`文件里的`name`标签内容。

当你启动虚拟机时你会发现，虚拟机没有像 `qemu` 一样弹出窗口，如果你仔细查看配置文件，你为其配置了

```xml
		<graphics type='vnc' port='5900' listen='127.0.0.1' />
```

所以请使用VNC工具连接查看，这里推荐安装`tigervnc-viewer`开源工具：

```sh
brew install tigervnc-viewer
```

当你想退出，你可以使用

```sh
virsh shutdown ubuntu
virsh destroy ubuntu
# 保存，下次可以用start继续运行
virsh managedsave ubuntu
```

`qemu`和`libvirt`可配置参数有很多，因此可玩很高，我会慢慢整理一些相关参考放在这里：

- [QEMU官方文档](https://www.qemu.org/docs/master/)
- [QEMU WiKi](https://wiki.qemu.org)：我建议作为官方文档的补充
- [QEMU - Arch WiKi](https://wiki.archlinux.org/title/QEMU)
- [Domain XML format](https://libvirt.org/formatdomain.html)
- [QEMU command-line passthrough](https://libvirt.org/kbase/qemu-passthrough-security.html)
- [Libvirt Hypervisor](https://libvirt.org/drvqemu.html)：众所周知 Hypervisor 是运行和管理多个虚拟机的程序
- [QEMU Switch To Libvirt](https://wiki.libvirt.org/page/QEMUSwitchToLibvirt)：将QEMU转换成Libvirt

## Virt Manger

virt-manger 具有可视化图形界面，更方便使用。

[参考文章](https://www.arthurkoziel.com/running-virt-manager-and-libvirt-on-macos/)

`Virt Manger` is powered by `libvirt`.

## Q&A

- 关于在macos上创建网络桥接

  [qemu在MacOS的桥接](https://taoshu.in/unix/qemu-bridge-on-macos.html)

  如果想让外界直接访问虚拟机，最简单的办法是使用桥接。目前网上多数是利用tap模式。macos不支持tap设备需要依赖第三方tuntap，因为新的macos已经启用的内核拓展，tuntap不再继续开发。

  macos 从 10.10 Yosemite 开始提供 Hypervisor.framework，这是 BSD 内核原生的虚拟化框架，有点类似 Linux 的 KVM 模块。Hypervisor.framework 支持为虚拟机创建桥接网络。qeum 大约在 2021 年年底开始支持 Hypervisor.framework。

    ```sh
    sudo qemu-system-x86_64 path/to/disk \
        -M accel=hvf \
        -cpu host -smp cpus=8 -m 256 \
        -nic vmnet-bridged,ifname=en0
    ```

## 总结

综上qemu和libvirt在mac下体验不好，还是要linux下使用。
