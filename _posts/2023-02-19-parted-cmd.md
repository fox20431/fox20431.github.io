# parted命令


parted /dev/sda

mklabel
gpt

parted -l

单位s sectorc


机械硬盘 扇区为512k

固态硬盘常采用4K对齐，使物理扇区与文件系统每Cluster（4096B）对区，可以延长固态硬盘寿命


以机械硬盘为例，parted默认对齐方式使2048s，即2048*512K=1M