# Github Action

github actions

```yaml
name: Main
on: 
  push:
    branches:
      - "main"

jobs:
  first_job: # Setting a custom job id
    name: My First Job
    runs-on: ubuntu-latest
    steps:
      - name: test
        run: |
          export HELLO="Nice to meet you!"
          echo $HELLO
  second_job: 
    name: My Second Job
    runs-on: ubuntu-latest
    steps:
      - name: test2
        run: |
          cat hello
```

## Job

每个Job需要制定一次操作系统，不同Job之间环境不相通！

## What do you need to know?

[actions/checkout](https://github.com/actions/checkout)

actions/checkout 把 github 的仓库的内容 copy 到当前 job 的环境中。

[actions/cache](https://github.com/actions/cache)

关于 actions/cache ，请把 actions/cache 操作放在使用缓存之前。

## Notice⚠️

ssh 过程中 private key 不能开放太多权限

```sh
chmod 0600 <primary_key>
```

ssh 连接会有一个需要确认的选项，需要输入 yes 和 no，但脚本不支持这么操作，所以可以写为：

```sh
ssh -o StrictHostKeyChecking=no -i ./id_rsa root@warrior.hihusky.com "rm -rf /var/www/wingv/*"
```

scp同理