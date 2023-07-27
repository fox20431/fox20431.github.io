---
title: rust tutorial
date: 2023-07-27
---

# Rust Tutorial



## 安装

**For Windows**

安装Rust：

```powershell
winget install Rustlang.Rustup
```

`Rustup` 是一组套件，其中包含 `cargo`、`clippy`、`rust-docs`、`rust-std`、`rustc` 等工具。

检查：

```powershell
rustc --version
```

## Get Started

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

## Cargo

Cargo 是 Rust 的**构建工具**和**包管理工具**。

创建项目：

```sh
cargo new <your_project_name>
```

运行项目：

```sh
cargo run
```

