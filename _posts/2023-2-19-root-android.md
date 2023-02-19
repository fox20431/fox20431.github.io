---
title:  "Root Android"
excerpt: "为 Android 获取 Root 权限"
---

# Root Android

## 获取Root

前提条件：

- 已解`Bootloader`锁的`Android`手机
- 安装`android-platform-tools`
- 开发者模式开启`USB debugging`

### 方案一

1. 进入`fastboot`

方法一：开机+音量下键

方法二：

开机的情况下

```shell
adb reboot fastboot
```

2. 刷入`recovery`

一般情况下第三方`recovery`使用`twrp`，不同机型`twrp.img`不同

```shell
fastboot flash recovery <twrp.img> 
```

3. 进入第三方`recovery`

方法一：开机+音量上键

方法二：fastboot模式下

```shell
fastboot reboot recovery
```

开机情况下

```shell
adb reboot recovery
```

4. 刷入`magisk.zip`

```
adb push <computer-file> <android-file-path>
```

比如：

```
adb push ./xiaomi.eu_multi_MI10Pro_V12.5.7.0.RJACNXM_v12-11.zip /sdcard/
```

5. 开机重启

### 方案二

1. 安装`magisk.app`
2. 下载当前版本的完整包
3. 提取出包的`boot.img`
4. 用`magisk`给`boot`打补丁，并将补丁后`patched_boot.img`发送给电脑
5. 电脑执行下面命令

```shell
fastboot flash boot <patched_boot.img>
```

6. 重启手机
7. 进入`magisk`应用，直接`root`

### 方案三

MIUI 开发版 `Setting -> Permissions -> Root access`

## 注意事项

我使用方案二进行root出现了一些状况，比如`adb root`提示`adbd cannot run as root in production builds`，这个原因未知。导致了我无法通过`adb`修改文件。

因为这个root是受限制的root，具体可见：

https://blog.mythsman.com/post/6093946a0527a03be7e559ca/

同时magisk的root无法挂载读写的解释：

https://android.stackexchange.com/questions/220892/system-partition-locked-to-read-only-in-android-10

方案三没有问题，如果需要adb操作文件需要执行下面操作

```shell
adb root
adb disable-verity
adb shell
# -o option rw premission and remount it
mount -o rw,remount /system
```

## 小技巧

`/system/media/bootanimation.zip`通过更改这个可以修改开机动画

将`ro.secure=0`写入`/system/build.prop`可以默认为adb为root权限

`ro.debuggable=1`允许你执行`adb root`