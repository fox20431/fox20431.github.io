---
title: rclone tutorial
date: 2024-02-12
---

# RClone 教程

环境：Linux

平台：OneDrive

参考文献：

- [Linux使用RClone挂载OneDrive王盘](https://333rd.net/posts/tech/linux%E4%BD%BF%E7%94%A8rclone%E6%8C%82%E8%BD%BDonedrive%)E7%BD%91%E7%9B%98/

使用该云盘方案从文件操作感受上类似挂载了一个物理硬盘，可以选择性挂载位置，也可以解挂载。

1. 安装 rclone

2. 配置rclone配置，如下是进入具有引导的交互界面命令，具体交互省略

   ```
   rclone config
   ```

   需要体型的是对于 OneDrive 需要进入 [Azure](https://portal.azure.com/#blade/Microsoft_AAD_IAM/ActiveDirectoryMenuBlade/RegisteredApps) 中配置客户ID 然后 配置 Secret 。

3. 配置完成后，可以使用下述命令测试是否具有访问权限

   ```sh
   rclone ls <name>
   # 比如，冒号不能省去
   rclone ls OneDrive:
   ```

4. 挂载操作

   ```sh
   rclone mount OneDrive:Documents/KeePass ~/Documents/KeePass/  --daemon 
   ```

其他帮助参数 `-vv` 可以查看更详细的 debug 信息，更外该命令提供了很好的命令行补全功能。