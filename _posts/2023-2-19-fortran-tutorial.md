# Fortran tutorial

Fortran 是第一个广泛实用的语言，所以考古一下。

## Get startting

安装 `gcc-fortran` 

```sh
sudo pacman -S gcc-fortran
```

安装 [`fortls`](https://github.com/fortran-lang/fortls)

```sh
pip install fortls --upgrade
```

(Optional) VSCode 安装 `Modern Fortran` 插件。

开始编写第一个程序。

example.f90

```f90
program hello
    ! This is a comment line; it is ignored by the compiler
    print *, 'Hello, World!'
end program hello
```

编译

```sh
gfortran example.f90 -o example
```

运行

```sh
./example
# output
Hello, World!
```