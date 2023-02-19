pushd

pushd的 功能是创建一个目录栈

popd

popd，作用与pushd相反，将栈顶的目录弹出

举例

pushd $LFS/sources
  md5sum -c md5sums
popd