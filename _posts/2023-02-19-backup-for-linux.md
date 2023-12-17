---
title: back up for linux
date: 2023-12-23
---



# Backup for Linux

我想知道linux下是否存在类似mac平台下的time-machine的工具，mac下的time-machine的特性是可以记录不同时间点的文件状态，且是增量更新的。

通过询问群友发现解决方案为有以下几种：

- timeshift 应用程序
- btrfs(依云姐姐)/btrfs-assistant
- btrbk+btrfs

## 具体实践

1. First, you need to create a Btrfs partition on your backup device. You can use a tool like parted or fdisk to create a new partition and format it as Btrfs.

    以下为常用命令

    ```sh
    # 格式分区为btrfs文件系统
    sudo mkfs.btrfs /dev/partition
    # 更改btrfs文件的label
        sudo btrfs filesystem label /path/to/mounted/btrfs_volume new_label
    ```

    

2. Once you have the Btrfs partition, you can use the btrfs subvolume create command to create a new subvolume on the partition, which will be used to store the backup.

    ```sh
    sudo 	btrfs subvolume create /path/to/backup/partition/backup
    ```

3. To backup the ext4 file system, you can use the rsync command to copy the entire file system to the new Btrfs subvolume.

    ```sh
    # a archive 
    # v verbose
    # x cross file bo
    sudo rsync -av	xHAX --numeric-ids --delete --checksum / /path/to/backup/partition/backup
    ```

    此外我推荐我编辑的脚本，根据需要自己改动

    ```sh
    #!/bin/bash
    
    # 默认排除的文件和目录
    exclude_list=(
      "/proc/*"
      "/sys/*"
      "/dev/*"
      "/tmp/*"
      "/run/*"
      "/mnt/*"
      "/media/*"
      "/lost+found"
    )
    
    # 不建议排除用户的所有cache，因为它可能保存重要内容
    exclude_user_list+=(
      ".cache/httpdirfs"
    )
    
    # 函数显示帮助信息
    show_help() {
      echo "Usage: $0 [OPTIONS] BACKUP_PATH"
      echo "Backup the Linux system using rsync."
      echo
      echo "Options:"
      echo "  -h, --help    Display this help and exit."
      echo
      echo "Arguments:"
      echo "  BACKUP_PATH    Specify the backup destination path."
      exit 0
    }
    
    # 函数显示错误信息并退出
    show_error() {
      echo -e "\e[91mError: $1\e[0m"
      exit 1
    }
    
    # 解析命令行选项
    while [[ $# -gt 0 ]]; do
      case $1 in
        -h | --help )
          show_help
          ;;
        * )
          backup_path="$1"
          shift
          ;;
      esac
    done
    
    # 检查是否提供了备份路径
    if [ -z "$backup_path" ]; then
      echo "Error: Please provide a backup path."
      show_help
    fi
    
    # 构建排除选项字符串
    exclude_options=""
    for exclude_item in "${exclude_list[@]}"; do
      exclude_options+=" --exclude=$exclude_item"
    done
    
    # 构建用户排除选项字符串
    for exclude_user_item in "${exclude_user_list[@]}"; do
      exclude_options+=" --exclude=/home/*/$exclude_user_item"
    done
    
    # 显示将要执行的排除选项，并获取用户确认
    echo "\"sudo rsync -avxHAX --numeric-ids $exclude_options / "$backup_path"\" will be executed!"
    read -p "Do you want to continue? (y/N) " confirm
    if [[ ! $confirm =~ ^[Yy]$ ]]; then
      show_error "Backup operation canceled by user."
    fi
    
    # 执行备份命令
    if sudo rsync -avxHAX --numeric-ids --delete --checksum $exclude_options / "$backup_path"; then
      echo "Backup completed successfully to $backup_path"
    else
      show_error "Backup failed. Please check the error message above."
    fi
    ```

4. Once the backup is complete, you can take a snapshot of the subvolume with the btrfs subvolume snapshot command.

    ```sh
    sudo btrfs subvolume snapshot -r /path/to/backup/partition/backup /path/to/backup/partition/snapshot
    ```

    delete the snapshot:

    ```sh
    sudo btrfs subvolume delete <snapshot>
    ```

5. 恢复系统。进入Live镜像（要求该镜像支持btrfs以及用用rsync工具），挂载要恢复的分区，逆向的备份方法在拷贝回去，详情间下述命令：

    ```sh
    sudo rsync -avxHAX --numeric-ids --delete --checksum /path/to/backup/partition/backup  /path/to/backup/partition/restore
    ```

    使用 `arch-chroot <mount point>` 进入到构建的系统，重新生成`fstab`以及重建grub引导。