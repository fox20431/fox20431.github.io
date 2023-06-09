---
title: Android Root Tutorial
---

# Android Root Tutorial

## 前提条件

- 手机已解`Bootloader`锁；
- 电脑已经安装`android-platform-tools`；
- 手机开发者模式已经开启`USB debugging`。

## Root Phone

这里推荐使用Migisk方式Root手机，通用性强，不容易出错，有明确指引。

第二种和第三种又有局限性：二种需要MIUI开发版，资格比较难获得；第三种依赖Recovery，Recovery不同机型需要定制，其次magisk.zip如何获取，获取后的通用性和安全性不清楚。

### 以Magisk官方方式Root手机（推荐）

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

详情可见：https://topjohnwu.github.io/Magisk/install.html

### MIUI开发版Root手机

MIUI 开发版 `Setting -> Permissions -> Root access`

### 以Recovery模式Root手机

1. 进入`fastboot`

   方式一：手机自助进入fastboot模式，开机+音量下键

   方法二：手机在开机的情况下与电脑建立ADB

    ```shell
    adb reboot fastboot
    ```

2. 刷入`recovery`

   一般情况下第三方`recovery`使用`twrp`，不同机型`twrp.img`不同

    ```shell
    fastboot flash recovery <twrp.img> 
    ```

3. 进入第三方`recovery`

   方式一：手机自助，开机+音量上键

   方法二：电脑辅助，fastboot模式下

    ```shell
    fastboot reboot recovery
    ```

    开机情况下

    ```shell
    adb reboot recovery
    ```

4. 刷入`magisk.zip`

    这一步在`recovery`内部完成

    `magisk.zip`可以通过下述方式从电脑推送到手机：

    ```
    adb push <computer-file> <android-file-path>
    ```

    比如：

    ```
    adb push ./xiaomi.eu_multi_MI10Pro_V12.5.7.0.RJACNXM_v12-11.zip /sdcard/
    ```

5. 开机重启

## Magisk

了解Magisk的使用甚至了解机制，对我们DIY十分有帮助。

这是官方的帮助：https://topjohnwu.github.io/Magisk/guides.html