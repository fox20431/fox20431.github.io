---
title: ACME.SH & DOCKER
excerpt: 
---

# ACME.SH & Docker

接下来用Docker来配置Nginx。

1. 将`acme.sh`以守护进程方式启动：

```sh
docker run --restart always -itd  \
  -v ~/docker-volumes/acme.sh:/acme.sh  \
  --net=host \
  --name=acme.sh \
  -v /var/run/docker.sock:/var/run/docker.sock \
  neilpang/acme.sh daemon
```

2. 获取证书

   ```sh
   docker exec \
     -e CF_Email=my@example.com \
     -e CF_Key=xxxxxxx \
     acme.sh --issue -d "*.hihusky.com" --dns dns_cf
   ```

3. 启动其他启动

   ```sh
   docker run --restart always -itd \
     --label sh.acme.autoload.domain=*.hihusky.com \
     -v ~/docker-volumes/nginx:/etc/nginx \
     --net=host \
     --name=nginx \
     nginx
   ```

   在这里设置了label，用于后续acme.sh钩子操作重启nginx。

4. 升级`acme.sh`

   如果不升级在接下来的步骤中不出现`can't work with curl 8.0.1`错误

   ```sh
   docker exec acme.sh --upgrade -b dev
   ```

5. 安装证书

   ```sh
   docker exec \
       -e DEPLOY_DOCKER_CONTAINER_LABEL=sh.acme.autoload.domain=*.hihusky.com \
       -e DEPLOY_DOCKER_CONTAINER_KEY_FILE=/etc/nginx/ssl/*.hihusky.com_ecc/*.hihusky.com.key \
       -e DEPLOY_DOCKER_CONTAINER_CERT_FILE="/etc/nginx/ssl/*.hihusky.com_ecc/*.hihusky.com.cer" \
       -e DEPLOY_DOCKER_CONTAINER_CA_FILE="/etc/nginx/ssl/*.hihusky.com_ecc/ca.cer" \
       -e DEPLOY_DOCKER_CONTAINER_FULLCHAIN_FILE="/etc/nginx/ssl/*.hihusky.com_ecc/fullchain.cer" \
       -e DEPLOY_DOCKER_CONTAINER_RELOAD_CMD="service nginx force-reload" \
       acme.sh --deploy -d *.hihusky.com  --deploy-hook docker --ecc
   ```

   该操作会将上述申请的证书，从`acme.sh`的容器中拷贝到`nginx`的容器中，同时会在`nginx`容器中执行`service nginx force-reload`，在证书路径没问题的情况下，就完成了nginx的证书的更新。