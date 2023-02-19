# Backup for Linux

我想知道linux下收否存在类似mac平台下的time-machine的工具，mac下的time-machine的特性是可以记录不同时间点的文件状态，且是增量更新的。

通过询问群友发现解决方案为有以下几种：

- timeshift 应用程序
- btrfs(依云姐姐)/btrfs-assistant
- btrbk+btrfs

I asked the `ChatGPT`: how to use the btrfs device to backup the linux which is ext4 file system?

The fallow is the answer:

Btrfs (B-tree file system) is a modern file system that supports advanced features such as snapshots, subvolumes, and data duplication. It can be used to create backups of a Linux system that uses the ext4 file system, although it's not the most common choice for that, here's an overview of how you might use Btrfs to create backups of an ext4 file system:

1. First, you need to create a Btrfs partition on your backup device. You can use a tool like parted or fdisk to create a new partition and format it as Btrfs.

2. Once you have the Btrfs partition, you can use the btrfs subvolume create command to create a new subvolume on the partition, which will be used to store the backup.

```sh
sudo btrfs subvolume create /path/to/backup/partition/backup
```

3. To backup the ext4 file system, you can use the rsync command to copy the entire file system to the new Btrfs subvolume.

```sh
sudo rsync -avxHAX --numeric-ids --delete / /path/to/backup/partition/backup
```

a archive 
v verbose
x cross file bo

--delete

4. Once the backup is complete, you can take a snapshot of the subvolume with the btrfs subvolume snapshot command.

```sh
sudo btrfs subvolume snapshot -r /path/to/backup/partition/backup /path/to/backup/partition/snapshot
```

more:

delete the snapshot:


```sh
sudo btrfs subvolume delete <snapshot>
```

---

最近应为重做系统，我尝试在 Arch Linux Live 镜像中将之前拷贝的文件再拷贝回系统中，然后直接启动。

首先第一步就是用备份的方法，再将原先的备份还原到准备好的文件系统中，然后使用 `arch-chroot <mount point>` ，发现没问题。

然后就着手修改下面的 `/etc/fstab` ，新创建的系统支持 `lvm2` ，所以在 linux 初始化内存配置上做了修改。

最后就是重新构建内存和grub引导，由于之前 grub 引导为了支持休眠做了内核传参，我也是删除掉了，保持默认行为。

最后开机，和原先的状态一模一样，不得不是 Linux 是永远的神！