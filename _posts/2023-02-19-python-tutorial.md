---
title: python tutorial
date: 2023-02-19
---

# Python Tutorial



## Environment

Install

```sh
sudo pacman -S python python-pip
```

check the env

```
python --version
pip --version
```

### Install Package

```
# 安装包
pip install <package-name>
# 查看安装包的信息(requires, location)
pip show <installe-package-name>
```

## Config IDE

**for VSCode**

插件 Python Pylance

setting.json

```json
{
  "python.languageServer": "Pylance"
}
```

他不会检测虚拟环境，需要你全局环境有这个包，不然会报警告。



## Q&A

- PyCharm Matplotlib Backend Problem

在Pycharm中Matplotlib Backend绘图会存在问题，解决方案为使用`TkAgg`后端进行绘图。

安装tk依赖：

```shell
brew install python-tk
```

python代码

```python
import matplotlib
matplotlib.use('TkAgg')
```

全局设置对虚拟环境Pycharm不生效，但还是告诉大家如何全局设置：在`~/.matplotlib/matplotlibrc`文件新增一行`backend: TkAgg`。

同时配置运行选项（或运行模版配置），将`Run with Python Console`取消勾选。



- Check `site-package` Content

查看 `site-package` 的内容

```sh
 python -m site
 
 # output
 sys.path = [
    '/Users/ming/projects/fox20431',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python38.zip',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/lib-dynload',
    '/Users/ming/Library/Python/3.8/lib/python/site-packages',
    '/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.8/lib/python3.8/site-packages',
]
USER_BASE: '/Users/ming/Library/Python/3.8' (exists)
USER_SITE: '/Users/ming/Library/Python/3.8/lib/python/site-packages' (exists)
ENABLE_USER_SITE: True
```

使用 pip 时请确保代理问题， pip 的代理不允许使用 socks