---
title: linux kernel conception
date: 2024-02-24
---

# Linux 内核相关概念

## 系统启动流程

BIOS/UEFI加载阶段：

MBR (Master Boot Record)：在BIOS系统中，GRUB通常被安装在硬盘的MBR上。在UEFI系统中，会有一个特殊的分区（通常是EFI分区），其中包含引导加载程序。

GRUB加载阶段：

core.img：这是GRUB的核心镜像文件，通常位于/boot/grub/目录下。它包含有关GRUB的基本信息和代码，用于加载后续的阶段。
grub.cfg：配置文件，包含启动菜单和相关设置。通常位于/boot/grub/目录下。

内核加载阶段：

vmlinuz：Linux内核的可执行文件。通常位于/boot/目录下。
initramfs：一个临时的根文件系统，用于加载必要的驱动程序和模块，以便在实际的根文件系统加载之前完成引导过程。通常位于/boot/目录下。

根文件系统加载阶段：

根文件系统：通常是一个包含完整Linux系统的文件系统。可以是ext4、btrfs等。GRUB会将控制权交给内核，并指定根文件系统的位置。

用户空间初始化阶段：

/sbin/init（或者类似的进程）：是用户空间的第一个进程，负责初始化系统。在一些现代系统中，可能会使用systemd或其他替代初始化系统。

## 内核编译流程

1. 编译前的配置

    选择被编译进内核的部分(*)，作为模块化载入内核的部分(M)，既不编译进内核也不作为模块化的部分()

    ```sh
    make menuconfig
    ```

2. 编译内核

    ```sh
    #  可以指定 '-j<number>' 来加快编译速度
    make
    ```

    生成内核映像（通常是vmlinuz，位于内核源代码目录下的arch/<架构>/boot/目录中），同时产生 System.map 映射文件以及其他一些必要的文件。

    如果 `make menuconfig` 的更改不需要内核编译，则不会进行内核的编译，比如增加模块(M)。


3. 安装模块

    ```sh
    #  可以指定 '-j<number>' 来加快编译速度
    make modules_install
    ```

    编译并安装内核模块（kernel modules）。安装的模块文件通常被放置在系统的 `/lib/modules/<kernel_version>/` 目录中。
    
    内核模块是一种动态加载到内核中的二进制代码，用于支持设备驱动、文件系统、网络协议等功能。

4. 安装内核

    ```sh
    make install
    ```

    复制 `vmlinuz` 、 `System.map` 到 `/boot` 中。

5. 生成 initramfs

    `initramfs` 是一个用于在Linux系统引导过程中提供额外功能和支持的机制，确保系统能够成功启动并进入实际的根文件系统。
    
    提供的特性如下：

    - 用于创建临时的文件系统
    - 负责加载驱动和模块
    - 支持特殊文件系统和加密 
    - 启动临时服务和工具
    - 紧急修复和故障排查
    - 支持复杂的引导场景等

    内核安装并不负责生成和配置 `initramfs`，可以通过 `dracut` 和 `mkinitramfs` 生成。

    `dracut` 名字来源于两个单词的组合："drastic" 和 "cutting"。

6. 设置引导

    一般使用 `grub` 引导。
    
    第一次使用 grub 引导需要使用 `grub-install` 将 `grub` 安装到引导区域。之后的更新仅需要 `grub-mkconfig` 来更新 grub 引导的内容以及菜单的内容。

## 模块概念

### 内核的加载

- 系统启动时自动加载： 在系统启动时，由启动脚本（如 /etc/rc.d 或 /etc/init.d 中的脚本）或者 systemd 服务来加载一些内核模块。这些脚本通常位于系统的启动过程中，以确保在引导时加载必要的模块。
- 手动加载： 使用 modprobe 命令可以手动加载指定的内核模块。

### kmod

对于 Linux 模块的管理离不开 `kmod` 。

**Command**

- modprobe： 用于加载、卸载和管理内核模块。它会自动解析模块之间的依赖关系，并加载所需的模块。例如，modprobe <module_name> 可以加载指定的模块。
- lsmod： 显示当前加载的内核模块列表。可以使用 lsmod 命令查看已加载的模块及其使用情况。
- rmmod： 用于从内核中卸载已加载的模块。例如，rmmod <module_name> 可以卸载指定的模块。
- insmod： 用于将指定的模块加载到内核中。与 modprobe 不同，insmod 不会解析模块依赖关系，因此需要手动处理任何依赖关系。
- depmod： 生成模块依赖关系文件。这个工具会扫描已安装的模块，并生成一个 modules.dep 文件，其中包含模块之间的依赖关系。
- modinfo： 显示有关指定模块的信息，如模块的作者、版本、描述等。例如，modinfo <module_name> 可以获取有关指定模块的详细信息。

