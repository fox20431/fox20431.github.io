# Transmission

磁力链接下载工具

## Download

MacOS

```sh
brew install transmission-cli
```

## Usage

refer from: https://cli-ck.io/transmission-cli-user-guide/

```sh
# add tasks
transmission-remote -a "magnet_uri or bt_file"
# list
transmission-remote -l
# remote tasks
transmission-remote -t <id> -r
# start
```

这个似乎和公网也有一定关系...

所以你可以尝试用服务器来下载，而不是用内网的下载...



电脑下载的话我建议使用qBittorrent和Aria2等，然后自己配置Tracker。