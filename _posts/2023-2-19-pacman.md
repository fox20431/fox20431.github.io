```sh
# find which package a specific
pacman -Qo cmd
```


```sh
pacman -S pkgfile
# 查看命令属于哪个包
pkgfile command
```


安装出现`exists in filesystem`

```sh
sudo pacman -S --overwrite \* <package_name>
```
