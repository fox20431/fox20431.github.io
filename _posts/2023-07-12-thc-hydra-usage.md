---
title: thc hydra usage
date: 2023-07-12
---

# thc hydra usage

There is [the hydra repo on github](https://github.com/vanhauser-thc/thc-hydra).

## Install

**for debian**

Install `hydra`

```sh
sudo apt install hydra
```

If you want to make the hydra support specified protocal, install the specified library.

There are some recommended library

```sh
# libpq-dev: for postgres 
apt-get -y install libssl-dev libssh-dev libidn11-dev libpcre3-dev libpq-dev
```

## Usage

Hydra needs to be used with `dictionary`, there are common dictionaries:

- [rock you](https://github.com/praetorian-inc/Hob0Rules)

**Command Line**

```sh
hydra -L /path/username_dic -P /path/passwd_dic ip protocal
hydra -l username_string -p passwd_string ip protocal
```

examples:

```
hydra -l postgres -p postgres 127.0.0.1 postgres