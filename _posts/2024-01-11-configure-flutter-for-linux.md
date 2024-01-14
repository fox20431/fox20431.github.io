---
title: configure flutter for linux
date: 2024-01-11
---

# Flutter Linux配置教程

1. 安装 `flutter`

```sh
yay -S flutter android-sdk-cmdline-tools-latest
```

2. 安装 `Android SDK` 工具

   主要安装的内容有：

   - Android SDK
   - Android Build Tools
   - Android SDK Cmdline Tools
   - Android Platform
   - Android Platform Tools

   方式一：**推荐使用** `Android Studio` 自带的 SDK Manager，可以复用 `Android Stduio` 下载的 SDK；

   方式二：使用包管理

   ```sh
   yay -Sy android-sdk android-sdk-build-tools android-sdk-cmdline-tools-latest android-platform android-sdk-platform-tools
   ```

3. 选择性暴露命令

    ```sh
    export ANDROID_HOME=$HOME/Android/Sdk
    export PATH=$PATH:$ANDROID_HOME/platform-tools
    export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bi
    ```

4. 接受 Android 协议

    ```sh
    flutter doctor --android-licenses
    ```

5. 创建 flutter 项目

   ```sh
   flutter create flutter-demo
   ```

6. 运行

    ```
    flutter run
    ```

    

    
