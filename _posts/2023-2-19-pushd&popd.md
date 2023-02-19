pushd&popd

堆栈

pushd到一个目录中

popd弹出目录

```shell
# 进入build目录执行三个命令，然后退出build目录
pushd build
  ../configure
  make -C include
  make -C progs tic
popd
```