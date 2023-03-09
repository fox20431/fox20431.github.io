# Virt Disk

有的磁盘是预先分配的，即分配多大就占用多少系统空间

有的磁盘是动态分配的，虽然有指定大小，但实际占用根据真正使用的大小来决定

前者省心但占用多，后者占用少但要考虑系统空间问题。


这好像叫做`sparse`，不太懂，顺便找到了一个命令可以将预先分配的转为动态分配的命令：

```sh
qemu-img convert -f qcow2 -O qcow2 -o preallocation=off vol.qcow2 newdisk.qcow2
```