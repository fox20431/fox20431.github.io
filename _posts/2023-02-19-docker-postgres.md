# Docker Postgres

最近转战Windows，发现 Windows 的设计也很不错。图形界面相比命令行确实少了很多心智负担同时增加了便捷。

但是Windows的开发环境相比Linux还是有很多恼人的地方，我认为为了运行一堆开发所需要的环境（比如Postgres、Redis等等）而反复查找文件夹不是一件明智的事情。

我需要一个可以类似Linux下的Systemd的程序来帮我集中管理这些服务，很明显如今如日中天的Docker可以完成这个壮举，同时解决后面部署的问题。

越是了解Docker越是能体会到Docker的伟大之处。

## Occur Problem And Slove it

以Postgres为例，在用Docker作为开发环境遇到的问题有如下，遇到了时区问题。

找到了解决方案，将 `/var/lib/postgresql/data/postgres.conf` 中 `log_timezone` 设定为 `log_timezone = 'Asia/Shanghai'` 。

设想的最简单的方式是将配置文件使用 `docker cp` 拉取到本地，修改后再使用 `docker cp` 到容器内完成替换。

完成操作后，将这个容器打包成镜像，方便后续再生成容器。

这个操作有个很明显的劣势，比如Postgres的用户名密码和初始数据库在原始镜像容器初始化时就要指明，我在已经生成的容器再生成镜像导致在镜像启动的时候修改用户名和密码，通过参数的方式修改是一个复杂且不明智的选择。

然后我想到了基于上个原始的镜像写一个新的Dockerfile，比如RUN创建一个临时目录，再用COPY将配置文件放进去，再然后使用CMD在容器启动后执行配置文件覆盖操作。

但CMD只能存在一个，我添加的CMD会导致原镜像的CMD消失，从而无法初始化Postgres，这时候可以选择 `docker inspect` 尝试逆向，当然开源有更好的选择就是他的(仓库)[https://github.com/docker-library/postgres]。

后者显而易见就比较麻烦了，所以我最后还是采用了前者。

## How to quick start it

本想着用compose来快速启动项目的，但compose是为项目编排服务而生的，不适合构建开发环境。

比如每次 `docker compose down` 会删除容器和网络，这会导致每次启动还会再初始化镜像，浪费时间；还有 `docker compose up` 生成的网络和卷以及容器都会以该项目名作为前缀。

所以我还是认为正常的使用命令行启动一个容器，然后开关这个容器就足够了，成本很低。

