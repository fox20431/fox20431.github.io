---
title: C program tutorial
---



# C

## Getting Start

### Syntax

- 控制语句

### Library

#### GNU Lib C

[GNU Libc Manual](https://www.gnu.org/software/libc/manual/)

Man Page

```shell
man <api>
# for example
man pthread_create
```

## Help

类型 * 表示声明地址

\* 指针 表示常量

## Convention

### Naming

1. All macros and constants in caps: `MAX_BUFFER_SIZE`, `TRACKING_ID_PREFIX`.
2. Struct names and typedef's in camelcase: `GtkWidget`, `TrackingOrder`.
3. Functions that operate on structs: classic C style: `gtk_widget_show()`, `tracking_order_process()`.
4. Pointers: nothing fancy here: `GtkWidget *foo`, `TrackingOrder *bar`.
5. Global variables: just don't use global variables. They are evil.
6. Functions that are there, but shouldn't be called directly, or have obscure uses, or whatever: one or more underscores at the beginning: `_refrobnicate_data_tables()`, `_destroy_cache()`.
