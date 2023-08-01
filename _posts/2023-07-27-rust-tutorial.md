---
title: rust tutorial
date: 2023-07-27
---

# Rust Tutorial

Rust 教程

## 安装

这里安装 `Rustup` ，`Rustup` 是一组套件，其中包含 `cargo`、`clippy`、`rust-docs`、`rust-std`、`rustc` 等工具，同时可以管理这些工具。

**for Linux**

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

**For Windows**

```powershell
winget install Rustlang.Rustup
```

检查：

```powershell
rustc --version
```

## Get Started

### Simple Example

创建 `main.rs` 文件，然后写入如下内容：

```rust
fn main() {
    println!("Hello, world!");
}
```

编译这个文件：

```powershell
rustc main.rs
```

运行编译后的文件

```
.\main.exe
```

### Manage Project by Cargo

Cargo 是 Rust 的**构建工具**和**包管理工具**。

创建项目：

```sh
cargo new <your_project_name>
```

运行项目：

```sh
cargo run
```

## 开发

### 开发环境配置

**for Windows**

推荐使用 VSCode + WSL 开发，具体与纳音

VSCode 插件推荐：

**WSL**

VSCode 使用 WSL 作为开发环境的工具，必备。 

**rust-analyzer**:

Rust 分析工具，必备。

**CodeLLDB**:

默认 `VSCode` 情况下使用 `gdb` 调试 `Rust`，但 Rust 默认使用 LLVM 作为编译器后端，使用 `gdb` 调试会出现 `Locals` 中的 `String` 类型变量的值无法显示，如下：

![image-20230801143838599](./assets/image-20230801143838599.png)

当安装该插件后，VSCode 默认会使用 LLDB 进行调试，效果如下：

![image-20230801144115864](./assets/image-20230801144115864.png)

### 预先引入

像其他语言一样，Rust 预先引入了常用类型、traints 以及常用宏，详情可见 [prelude官方文档](https://doc.rust-lang.org/std/prelude/index.html) 。

### 数据结构

clone
