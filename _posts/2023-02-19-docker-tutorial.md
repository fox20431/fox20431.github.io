---
title: Docker Tutorial
date: 2023-02-19
---



# Docker Tutorial

Docker作为轻量级容器工具，可以打包、传输以及运行应用。

## Preface

### 认识镜像

[镜像](https://zh.wikipedia.org/wiki/ISO%E6%98%A0%E5%83%8F)是[磁盘映像](https://zh.wikipedia.org/wiki/%E7%A3%81%E7%9B%98%E6%98%A0%E5%83%8F)，包含一个磁盘卷或数据存储设备的**内容和结构**。

Docker以及K8S等容器工具所使用的镜像都遵守OCI（[开放容器标准](https://opencontainers.org/)）。

## Docker环境准备

### For Arch User

1. 安装Docker

```sh
sudo pacman -S docker
```

2. 为了让当前用户能够有权限使用docker，将当前用户加入到`docker`组：

```sh
sudo usermod -a -G docker <USER_NAME>
```

3. 了解相关信息

```sh
# 查看版本
docker version
# 查看信息
docker info
# 查看帮助
docker <COMMAND> -h
```

### For Debian User

https://docs.docker.com/engine/install/debian/

**Set up the repository**

1. Update the `apt` package index and install packages to allow `apt` to use a repository over HTTPS:

    ```sh
    sudo apt-get update
    sudo apt-get install ca-certificates curl gnupg
    ```

2. Add Docker’s official GPG key:

    ```sh
    sudo install -m 0755 -d /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    sudo chmod a+r /etc/apt/keyrings/docker.gpg
    ```

3. Use the following command to set up the repository:

    ```sh
    echo \
      "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
      "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
      sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    ```

**Install Docker Engine**

1. Update the `apt` package index:

   ```sh
   sudo apt-get update
   ```

2. Install Docker Engine, containerd, and Docker Compose:

   ```sh
   sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
   ```

3. Verify that the Docker Engine installation is successful by running the `hello-world` image:

   

   ```sh
   sudo docker run hello-world
   ```

   This command downloads a test image and runs it in a container. When the container runs, it prints a confirmation message and exits.

## Docker快速上手

### 镜像管理

通过下述命令可以拉取镜像：

```sh
docker pull <IMAGE:TAG>
```

Docker也提供了镜像搜索功能：

```sh
docker search <KEY_NAME>
```

拉取完毕后，可以查看所有镜像确认本地是否存在该镜像：

```sh
docker image ls
# or
docker images
```

当然也可以删除镜像：

```sh
docker image rm <IMAGE:TAG>
# or
docker rm i <IMAGE:TAG>
```

### 容器管理

指定镜像可以生成容器：

```sh
docker run [OPTIONS] <IMAGE> [COMMAND] [ARG...]
# for example: docker run -d --rm --name my-nginx nginx:lastes
```

查看容器：

```sh
# 如果不加`-a`，只会显示正在运行的容器
docker container ls
# or
docker ps
```

停止/启动容器：

```sh
docker container stop/start <CONTAINER>
```

删除容器：

```sh
docker container rm <COTAINER_NAME/HASH>
docker rm <COTAINER_NAME/HASH>
```

### 容器维护

对于已经启动的容器，可以通过外部命令来让容器执行命令：

```sh
docker exec [OPTIONS] CONTAINER COMMAND [ARG...]
```

主机和容器可以相互拷贝文件（用法类似SCP）：

```sh
docker cp <SOURCE_FILE> <TARGET_LOCATION>
```

### 自定义镜像

通过Dockerfile构建镜像：

```sh
docker build -t <IMAGE:TAG> .
```

对容器进行打包成image：

```sh
docker commit
```

## 分享镜像

上传到 Docker Hub，镜像名有要求 <username>/<image_name>:<tag>：

```sh
docker push
```

如果不发布怎么传输自己的镜像。

1. 压缩：

```sh
docker save <IMAGE> -o <PKG>
# for exampe: docker save nginx:lastest -o nginx.tar
```

2. 载入：

```sh
docker load -i <PKG> 
```

### 更多

查看容器/镜像的详细信息：

```sh
docker inspect <iamge-id/container-id>
```

## Docker Compose

上面聊的都是命令行来运行docker容器，毫无疑问创建容器指定参数是一个令人费神的操作，容器是反复运行同一个或者同时运行多个容器。

Docker Compose 可以指定单机的容器编排，通过编写 `yml` 持久化创建方法，同时可以创建多个以及前后依赖。

编写好 `docker-compose.yml` 后，可以使用下述命令：

```sh
# start
docker-compose up 
# -d: Run containers in the background.
# --build: Build images before starting containers.
# --force-recreate: Recreate containers even if their configuration and image haven't changed.
# stop
docker-compose down
# --volumes: Remove named volumes declared in the Compose file and anonymous volumes attached to containers.
# --remove-orphans: Remove containers for services not defined in the Compose file.
```

## MAC Tips

我们知道 docker 基于 linux 的，所以 mac 和 windows 上不能够直接运行 docker 命令，但是 mac 通过 `docker info` 命令可以发现 其实你可以制定一个远程的守护进程，也就是服务端。通过这个方式我们可以不用下载 docker desktop，仅仅只需要一个虚拟机/服务器，然后在环境变量中指出

```sh
export DOCKER_HOST=ssh://root@warrior.hihusky.com
```

你也可以指出 docker 的 context， 表明 来历

```sh
docker context create lima-docker --docker "host=unix:///Users/ming/.lima/docker/sock/docker.sock"
```


## Q&A

### 无法启动容器

```sh
docker container start my-redis
```

错误信息：

Error response from daemon: failed to create endpoint my-redis on network bridge: failed to add the host (veth80ee17c) <=> sandbox (vethf5db9f9) pair interfaces: operation not supported

原因以及解决方案：

升级导致的，只需要重启即可解决