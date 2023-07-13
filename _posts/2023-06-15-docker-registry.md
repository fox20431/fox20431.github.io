---
title: Docker Registry 
---

# Docker Registry

Why do you need `Docker Registry`?

`Docker Hub` hosts many images, hence it incurs significant traffic and storage charges.

So `Docker Hub` limits the user's private image number. If you want to host your images privately, either pay for it to `Docker` or deploy the `Docker Registry`.

More information can be found in:

- [The official documentation](https://docs.docker.com/registry/)

- [Docker Registry Image Home](https://hub.docker.com/_/registry)

## Run

We will deploy the `Docker Registry` next; I adopt the nginx proxy to make it can use TSL.

Config the Docker Registry.

Create the `./config/config.yml`

```yaml
version: 0.1
log:
  fields:
    service: registry
storage:
  cache:
    blobdescriptor: inmemory
  filesystem:
    rootdirectory: /var/lib/registry
http:
  addr: :5000
  # prefix: /registry/
  headers:
    X-Content-Type-Options: [nosniff]

auth:
  htpasswd:
    realm: basic-realm
    path: /auth/htpasswd

health:
  storagedriver:
    enabled: true
    interval: 10s
    threshold: 3
```

More detail to see [the documentation](https://docs.docker.com/registry/configuration/).

Then we also need to create the `htpasswd` file to support docker registry auth.

To `htpasswd` file, you need to install the `htpasswd` tool.

```sh
# for debain/ubunut
sudo apt-get install apache2-utils
```

Then generate the file:

```sh
htpasswd -Bbn admin admin > ./data/htpasswd
```

Then run the docker:

```sh
docker run -d -p 5000:5000 \
    -v $HOME/docker/registry/registry/:/var/lib/registry/ \
    -v $HOME/docker/registry/auth/:/auth/ \
    -v $HOME/docker/registry/config/config.yml:/etc/docker/registry/config.yml \
    --restart=always \
    --name=registry \
    registry
```

Config nginx.

```nginx
http {
    # ...
    
    upstream registry {
        server 127.0.0.1:5000;
    }
    
    server {
        listen  443 ssl;
        server_name localhost;

        client_max_body_size 2048M;     # for docker registry, avoid the 413 http status code

        ssl_certificate_key /path/key;
        ssl_certificate /path/cer_or_pem;

        # ...
            
        location /v2/ {
            proxy_pass          http://registry;
            proxy_set_header    Host              $http_host;   # required for docker client's sake
            proxy_set_header    X-Real-IP         $remote_addr; # pass on real client's IP
            proxy_set_header    X-Forwarded-For   $proxy_add_x_forwarded_for;
            proxy_set_header    X-Forwarded-Proto $scheme;
        }
    }
}
```

Start nginx

```sh
docker run --restart always -itd \
  -v ./data/nginx:/etc/nginx \
  --net=host \
  --name=nginx \
  nginx
```

**THERE BE DRAGONS**

Due to `/v2/`being a common URL, I have tried to change the URL, like `/registry/v2/`.

Unfortunately, `Docker Registry` jumps to other URLs according to the host. For example, It will jump to `/v2/` when I access `/registry/v2`.

It can be fixed by modifying the `Docker Registry` config file, you just need add the following field:

```yaml
http:
  addr: :5000
  prefix: /registry/
```

But when I push the image to the server, no matter how to tag the repository, it always tells me `404`.

This is missing on the Internet, so I don't think that's what I need to care about at the moment. At least in the time spent and the return is not worth it.

## Test

You can access the URL of the host to check the image, but you need to log in with basic auth, so please use the following cmd:

```
curl ip:port/v2/_catalog -u admin
```

If you use the docker client, you can use the following command:

```
docker login ip:port
```

Then you can push and pull image.

