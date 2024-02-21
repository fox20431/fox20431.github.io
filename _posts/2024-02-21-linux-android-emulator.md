---
title: linux android emulator
date: 2024-02-21
---

# Linux 安卓模拟器


## ReDroid 容器化

容器化模拟器的好处就是不会污染到宿主环境。

参考内容：

- [ReDroid教学](https://ivonblog.com/posts/redroid-android-docker/)

### ReDroid 环境准备


1. 更换 Linux 内核类型为 `linux-zen` （针对性能优化的模块编译内核）

    ```sh
    sudo pacman -S linux-zen linux-zen-headers linux-zen-docs
    ```

2. 安装 docker ，用于容器化部署 ReDroid ：

    ```sh
    # 如果有Nvidia驅動，記得將其換成DKMS版本
    sudo pacman -R nvidia
    sudo pacman -S nvidia-dkms
    # 確認沒有安裝binder_linux-dkms
    yay -R binder_linux-dkms

    # 安裝linux-zen核心
    sudo pacman -S linux-zen linux-zen-headers
    sudo mkinitcpio -p linux-zen
    sudo grub-mkconfig -o /boot/grub/grub.cfg
    ```

3. 安装 adb 和 scrcpy ：

    ```sh
    # android-tools 可以使用 android studio 安装
    sudo pacman -S android-tools
    sudo pacman -S scrcpy
    ```

### 创建 ReDroid 容器

1. 在您喜欢的路径下创建 docker-compose.yml 文件，编辑写入如下内容：

    ```sh
    version: "3"
    services:
    redroid:
        image: redroid/redroid:11.0.0-latest
        stdin_open: true
        tty: true
        privileged: true
        ports:
        - "5555:5555"
        volumes:
        # 資料存放在目前目錄下
        - ./redroid-11-data:/data
        command:
        # 啟用GPU硬體加速
        - androidboot.redroid_gpu_mode=auto
        # 設定libndk相關
        - ro.product.cpu.abilist0=x86_64,arm64-v8a,x86,armeabi-v7a,armeabi
        - ro.product.cpu.abilist64=x86_64,arm64-v8a
        - ro.product.cpu.abilist32=x86,armeabi-v7a,armeabi
        - ro.dalvik.vm.isa.arm=x86
        - ro.dalvik.vm.isa.arm64=x86_64
        - ro.enable.native.bridge.exec=1
        - ro.dalvik.vm.native.bridge=libndk_translation.so
        - ro.ndk_translation.version=0.2.2
    ```

2. 启动容器

    ```sh
    sudo docker compose up -d
    ```

3. 建立连接

    ```sh
    adb connect localhost:5555

    # 如果連不上，用以下指令看一下容器內部發生什麼問題
    sudo docker exec <容器ID> logcat
    sudo docker logs <容器ID>
    ```

4. 远程连接桌面

    ```sh
    scrcpy -s localhost:5555 --audio-codec=raw
    ```

### 更多操作

关于宿主机的文件如何传递给 ReDroid 容器，以下是解决方案：

您无法直接通过上述 Docker 脚本挂载的目录中找到类似 `Download` 用户可用目录，原因不明，因此无法直接在宿主机操作 ReDroid 的文件。

可以使用 `adb shell` 进入 Android 系统中，使用 `echo $EXTERNAL_STORAGE/Download` 来获取 `Download` 的实际地址，为 `/sdcard/Download` ，然后通过 `adb push` 将宿主机上的文件传到 ReDroid 容器内。





