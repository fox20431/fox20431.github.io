# 一、Git介绍、安装、配置及简单使用

## 介绍GIT

[Git简史 - 官方参考](https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-Git-%E7%AE%80%E5%8F%B2)

## 安装GIT

**类UNIX**

```sh
pkg-mgr install git
```

**Windows**

[官网安装](https://git-scm.com/)

## 配置Git

配置用户名和邮箱

```sh
git config --global user.name "username"
git config --global user.email "email"
```

## 简单命令使用

- git status [-s]
- git add [.]
- git rm
- git commit
- git diff
- git log [--oneline]
- man git-[command]

# 二、GitHub注册登录、配置以及代码托管

## 注册登录

## 配置

创建密钥对

```sh
# `id_rsa`和`id_rsa.pub`的权限应为`700`
ssh-keygen -t rsa
```

上传公钥到Github

测试连接

```ssh
ssh -T git@github.com
```

## 代码托管

```sh
git remote add <remote_repo_name> <remote_repo_url>
git remote remove <remote_repo_name>
```

# 三、分支介绍、操作和解决冲突

## 分支的创建和切换

单个分支操作

```sh
git reset [--mixed(default)/soft/hard] <COMMIT>
# mixed 会影响 commit 和 index
# soft 仅会影响 commit
# hard 会影响 commit index workspace
```

多个分支操作

```sh
git branch <branch_name>
git checkout [-b] <branch_name>
```

## 冲突

```sh
git merge
```


# 四、GitHub协同合作与经验之谈

## 提 ISSUE

## 提 PR

pull request

## 搜索技巧

## 更多