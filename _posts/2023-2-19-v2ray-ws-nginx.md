证书申请绑定教程 acme.sh

https://www.youtube.com/watch?v=JQWaZp-UbIc

### DEFINE

- V2ray Server
  - Domain: `server.com`
  - id: `7e6d2332-880e-4814-82ab-587bbb852361`
  - path: `/path`
  - SSL path: `/ssl`
  - SSL file name: `pem.pem`, `key.key`
- Reverse Server
  - Domain: `reverse.com`
  - path: `/path`

> 注意：V2ray Server 的 nginx 站点配置应为 **default_server**, 反代服务器的 NGINX 配置文件没有要求为 **default_server**, 但是也 **不应该** 指定其他站点为 **default_server**。
> 推荐将其都设置为 **default_server**。

### 服务端

> TLS 服务由 NGINX 提供，无需再 config.json 定义

1. 安装必须项

   1. sudo apt install nginx -y 或者 yum install nginx -y
   2. bash <(curl -L -s https://install.direct/go.sh)

2. vim /etc/v2ray/config.json

   ```json
   {
       "inbounds": [
           {
               "port": 20809,
               "listen": "127.0.0.1",
               "protocol": "vmess",
               "settings": {
                   "clients": [
                       {
                           "id": "7e6d2332-880e-4814-82ab-587bbb852361",
                           "alterId": 64
                       }
                   ]
               },
               "streamSettings": {
                   "network": "ws",
                   "wsSettings": {
                       "path": "/websocks"
                   }
               }
           }
       ],
       "outbounds": [
           {
               "protocol": "freedom",
               "settings": {}
           }
       ]
   }
   ```

3. vim /etc/nginx/sites-enabled/default

   ```nginx
   server {
       listen 443 ssl default_server;
       ssl on;
       ssl_certificate       /ssl/pem.pem;
       ssl_certificate_key   /ssl/key.key;
       ssl_protocols         TLSv1 TLSv1.1 TLSv1.2;
       ssl_ciphers           HIGH:!aNULL:!MD5;
       server_name           server.com;
       location /path {
                   proxy_redirect off;
                   proxy_pass http://127.0.0.1:20809;
                   proxy_http_version 1.1;
                   proxy_set_header Upgrade $http_upgrade;
                   proxy_set_header Connection "upgrade";
                   proxy_set_header Host $host;
                    # Show real IP in v2ray access.log
                   proxy_set_header X-Real-IP $remote_addr;
                   proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
         }
     }
   ```

4. service v2ray restart && nginx -t && nginx -s reload

> 到此 TLS+WEB+WS 即可用了，但是个人的网（城域网）从各个意义上来说一般是不如国内服务器的，所以继续…

展示一下我自己配合wordpress写的nginx配置文件

```nginx
server {

	listen 443 ssl http2 default_server;
	listen [::]:443 ssl http2 default_server;

	server_name www.hihusky.com;

	ssl on;
	ssl_certificate /etc/nginx/cert/www.hihusky.com.pem;
	ssl_certificate_key /etc/nginx/cert/www.hihusky.com.key;
	ssl_session_cache shared:SSL:1m;
	ssl_session_timeout 4h;
	# Encryption algorithm
	ssl_ciphers EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH;

	ssl_stapling on;
	ssl_stapling_verify on;
	ssl_trusted_certificate /etc/nginx/cert/www.hihusky.com.pem;

	root /var/www/wordpress/;
	index index.php;

	location ~ \.php {
		fastcgi_pass   unix:/run/php/php7.4-fpm.sock;
		fastcgi_index  index.php;
        fastcgi_param  SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include        fastcgi_params;
	}

	location /websocket {
		proxy_redirect off;
        proxy_intercept_errors on;
        proxy_pass http://127.0.0.1:20809;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $http_host;
	}
}
```



### 客户端

> 如果设置了反代的话，服务器地址应修改为反代服务器地址, 所以 `outbounds` 里面的 `address` 应修改为 `reverse.com`

```json
{
  "inbounds": [
    {
      "port": 1080,
      "listen": "127.0.0.1",
      "protocol": "socks",
      "sniffing": {
        "enabled": true,
        "destOverride": ["http", "tls"]
      },
      "settings": {
        "auth": "noauth",
        "udp": false
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "vmess",
      "settings": {
        "vnext": [
          {
            "address": "server.com",
            "port": 443,
            "users": [
              {
                "id": "7e6d2332-880e-4814-82ab-587bbb852361",
                "alterId": 64
              }
            ]
          }
        ]
      },
      "streamSettings": {
        "network": "ws",
        "security": "tls",
        "wsSettings": {
          "path": "/path"
        }
      }
    }
  ]
}
```

延迟优化：https://segmentfault.com/a/1190000039073842



vless ws nginx https://www.rootfw.com/en/posts/93baa7dd.html



关于ssl证书延迟 http://www.ruanyifeng.com/blog/2014/09/ssl-latency.html