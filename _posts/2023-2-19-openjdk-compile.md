# Compile JDK

首先不推荐使用 Windows 平台编译 JDK ！原因就是 OpenJDK 官方倾向 POSIX 的系统开发环境。

## Prepare

准备 JDK ，编译 JDK 需要系统已经存在的 JDK ，且版本有要求（看你编译的版本）。

准备源码，源码版本要稳定。

我编译的源码是 `jdk-17-ga` ，且我的宿主机环境使用的 `jdk17` 。

## Compile

### on Linux

我使用的 Arch Linux ，在编译 `java.desktop` 等一些包的时候，还是会有警告。

该编译的情况下，编译器会将警告认为错误，导致编译无法通过。

为了防止这个问题，我定位了 `Werror` 这个关键字。

```sh
grep 'Werror' -r *|less -S
```
并定位到这个参数的位置：

```
/home/ming/projects/jdk/make/autoconf/flags-cflags.m4
```

注释了两行相关的参数，重新 configure 和 make iamges 虽然有警告，但还是通过了！

### on Windows

ref: https://openjdk.org/groups/build/doc/building.html

```sh
./configure --with-boot-jdk="/mnt/c/Program Files/Microsoft/jdk-xxx.
8-hotspot"
```


```output
configure: (Your Boot JDK version must be one of: 19 20 21)
```