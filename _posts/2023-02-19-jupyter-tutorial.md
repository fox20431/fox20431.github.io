---
title: jupyter tutorial
---





# Jupyter Tutorial



## Common

```sh
# install interpreted engine
pip install ipython
# install jupyter
pip install jupyter

# install python package
pip install numpy
pip install pandas
pip install matplotlib

pip install scipy
pip install sympy
```

## Jupyter On Local

```
python -m notebook
```

## Jupyter On Server

```
# 生成配置文件
jupyter notebook --generate-config
# 修改密码
jupyter notebook password

# 在当前目录启动jupyter服务
nohup jupyter notebook --ip=0.0.0.0 --no-browser --allow-root &
```