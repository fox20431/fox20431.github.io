---
title: pip tutorial
date: 2023-02-19
---

# pip tutorial

关于python模块使用，如果环境变量无法找到对应命令，可以使用 `python3 -m <command>` 来使用对应命令

pip默认全局安装，如果需要针对当前用户，需要使用 `--user` 命令，类似

```sh
pip3 install --user <package>
```

Mac下
pip全局下bin目录
/usr/local/opt/python@3.9/Frameworks/Python.framework/Versions/3.9/bin
pip用户安装模块目录
安装在`/Users/arvin/Library/Python/3.8/bin`

升级pip
python3 -m pip install --upgrade pip
列出过时包
pip list --outdated
安装升级包
pip install --upgrade 要升级的包名

查看可更新包：
pip list  --outdated
批量下载并更新：
pip install pip-review
pip-review --local --interactive

WARNING: Ignoring invalid distribution -ip
原因可能是之前下载库的时候没有成功或者中途退出。
解决方法：
到提示的目录site-packages下删除~ip开头的目录。
然后pip重新安装库即可。





## Q&A



- `This environment is externally managed`

You can use python `venv` like described [here](https://stackoverflow.com/a/75696359/10626495).

However if you really want to install packages that way, then there are couple solutions:

- remove file `/usr/lib/python3.x/EXTERNALLY-MANAGED`,
- use `pip`'s argument `--break-system-packages`,
- add following lines to `~/.config/pip/pip.conf`:

```py
[global]
break-system-packages = true
```

https://stackoverflow.com/questions/75608323/how-do-i-solve-error-externally-managed-environment-everytime-i-use-pip3