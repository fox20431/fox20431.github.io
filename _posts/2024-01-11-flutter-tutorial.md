---
title: flutter tutorial
date: 2024-01-11
---

# Flutter 教程

Flutter 跨端开发

## 开发环境配置

### Arch Linux

安装 `flutter`

```sh
yay -S flutter
```

#### For Android

1. 安装 `Android SDK` 工具

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

2. 选择性暴露命令

    ```sh
    export ANDROID_HOME=$HOME/Android/Sdk
    export PATH=$PATH:$ANDROID_HOME/platform-tools
    export PATH=$PATH:$ANDROID_HOME/cmdline-tools/latest/bin
    ```

3. 接受 Android 协议

    ```sh
    flutter doctor --android-licenses
    ```

## Flutter 项目运行

推荐 VSCode `flutter` 插件进行开发，可以免去手动设置和操作。

1. 创建 `flutter` 项目

    ```sh
    flutter create <flutter_project_name>
    ```

2. 启动项目

    ```sh
    flutter run
    # default use the android emulator
    # specify the device id or name
    flutter run -d <device_id/name>
    ```

### For Android

将Flutter项目运行在Android需要Android的运行环境。

使用模拟器：

   ```sh
   # show emulators
   flutter emulators
   # launch emulators
   flutter emulators --launch <emulator_name>
   ```

## Flutter 项目结构

1. 不同平台原生代码目录：`android/`, `ios/`, `linux/`, `macos/`, `windows/`, `web/`
   - `android/` 目录包含了用于Android应用的原生代码，通常使用Java或Kotlin编写。
   - `ios/` 目录包含了用于iOS应用的原生代码，通常使用Objective-C或Swift编写。
2. **lib/ 目录：**
   - `lib/` 目录是Flutter应用的主要代码目录，包含Dart语言编写的Flutter应用代码。这里通常包含主屏幕、小部件、业务逻辑等。
3. **test/ 目录：**
   - `test/` 目录包含Flutter应用的测试代码。这些测试可以是单元测试、集成测试或小部件测试，用于确保应用的质量和稳定性。
4. **assets/ 目录：**
   - `assets/` 目录用于存储应用程序使用的静态资源，如图像、字体文件等。这些资源可以通过`pubspec.yaml`文件进行配置。
5. **pubspec.yaml 文件：**
   - `pubspec.yaml` 是Flutter项目的配置文件，其中包含了项目的依赖关系、版本信息以及其他配置项。在这个文件中，你还可以指定应用程序的名称、描述、作者等信息。
6. **build/ 目录：**
   - `build/` 目录通常包含与构建过程相关的临时文件和输出。这个目录可以被忽略，因为它们是由Flutter框架自动生成的。
