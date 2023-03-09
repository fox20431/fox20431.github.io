# Encrypt File

最近有些敏感信息需要加密...

是一个移动硬盘，由于需要多平台的兼容，所以移动硬盘的文件系统是 `exfat` ，但是很糟糕的是 `exfat` 不原生支持加密。

所以比较麻烦的方案是通过第三方进行加密。

这次我尝试使用自带 `tar` 命令配合 `openssl` 对文件加密，等后面考虑再换。

加密压缩：

```sh
tar -czvf - files | openssl des3 -salt -k password -out files.tar.gz
```

解密解压：

```sh
openssl des3 -d -k password -salt -in files.tar.gz | tar xzvf -
```

ref: https://blog.csdn.net/qq_32599479/article/details/100065494