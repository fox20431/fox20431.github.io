# V2Ray 配置文件

测试配置文件：`v2ray -test -config=/usr/local/etc/v2ray/config.json`

## Preface

V2Ray是网络代理。

代理过程中加密解密会耗时并且消耗一定算力。

## 服务端

### VLESS

VLESS 无加密，很容易被GFW检测到。

```json
{
    "log": {
        "loglevel": "warning"
    },
    "inbounds": {
        "port": 10808,
        "protocol": "vmess",
        "settings": {
            "clients": [
                {
                    "id": "<uuid>",
                    "alterId": 4
                }
            ]
        }
    },
    "outbounds": [
        {
            "protocol": "freedom"
        }
    ]
}
```

### 基于TLS的VLESS加密传输

TLS本质上就是利用HTTPS的加密安全传输。

#### 配合NIGNX的VLESS方案

```json
{
	"log": {
		"loglevel": "warning",
		"access": "/usr/local/var/v2ray/access.log",
		"error": "/usr/local/var/v2ray/error.log"
	},
	"inbounds": [
		{
			"port": 20809,
			"listen": "127.0.0.1",
			"protocol": "vless",
			"settings": {
				"clients": [
					{
						"id": "<uuid>"
					}
				],
				"decryption": "none"
			},
			"streamSettings": {
				"network": "ws",
				"security": "none",
				"wsSettings": {
					"path": "/websocket"
				}
			}
		}
	],
	"outbounds": [
		{
			"protocol": "freedom"
		}
	]
}
```

#### 基于V2Ray的TLS的VLESS

```json
{
	"log": {
		"loglevel": "warning",
		"access": "/usr/local/var/v2ray/access.log",
		"error": "/usr/local/var/v2ray/error.log"
	},
	"inbounds": {
		"port": 20808,
		"protocol": "vless",
		"settings": {
			"clients": [
				{
					"id": "<uuid>"
				}
			],
			"decryption": "none",
			"fallbacks": [
				{
					"dest": 80
				},
				{
					"path": "/websocket",
					"dest": 20809,
					"xver": 1
				}
			]
		},
		"streamSettings": {
			"network": "tcp",
			"security": "tls",
			"tlsSettings": {
				"alpn": [
					"http/1.1"
				],
				"certificates": [
					{
						"certificateFile": "/etc/nginx/cert/www.hihusky.com.pem", 
						"keyFile": "/etc/nginx/cert/www.hihusky.com.key" 
					}
				]
			}
		}
	},
	"outbounds": [
		{
			"protocol": "freedom"
		}
	]
}
```

### VMESS

VMESS 自带加密

```json
{
	"log": {
		"loglevel": "warning",
		"access": "/usr/local/var/v2ray/access.log",
		"error": "/usr/local/var/v2ray/error.log"
	},
	"inbounds": {
		"port": 20807,
		"protocol": "vmess",
		"settings": {
			"clients": [{ 
				"id": "090C2921-5814-44F6-976F-B56E5E7F3107",
				"alterId": 4
			}]
		}
	},
	"outbounds": [
		{
			"protocol": "freedom"
		}
	]
}
```

### 更多

你可以为服务端写多种入站方式，即为其开放多个端口。

## 客户端

```json
{
    "log": {
        "loglevel": "warning",
        "access": "/usr/local/var/v2ray/access.log",
        "error": "/usr/local/var/v2ray/error.log"
    },
    // 入站
    "inbounds": [
        // 开放socks端口
        {
            "port": 10808,
            "listen": "127.0.0.1",
            "protocol": "socks",
            "sniffing": {
                "enable": true,
                "destOverride": [
                    "http",
                    "tls"
                ]
            },
            "settings": {
                "auth": "noauth",
                "udp": true
            }
        },
        // 开放HTTP端口
        {
            "port": 8118,
            "listen": "127.0.0.1",
            "protocol": "http",
            "settings": {
                "timeout": 0
            }
        }
    ],
    // 出站规则
    "outbounds": [
        // 基于tls的vless
        {
            "protocol": "vless",
            "tag": "us-vless-proxy",
            "settings": {
                "vnext": [
                    {
                        "address": "www.hihusky.com",
                        "port": 443,
                        "users": [
                            {
                                "id": "uuid",
                                "encryption": "none"
                            }
                        ]
                    }
                ]
            },
            "streamSettings": {
                "network": "ws",
                "security": "tls",
                "tlsSettings": {
                    "serverName": "www.hihusky.com"
                },
                "wsSettings": {
                    "path": "/websocket"
                }
            }
        },
        // vmess
        {
            "protocol": "vmess",
            "tag": "us-proxy",
            "settings": {
                "vnext": [
                    {
                        "address": "www.hihusky.com",
                        "port": 20808,
                        "users": [
                            {
                                "id": "<uuid>",
                                "alterId": 0
                            }
                        ]
                    }
                ]
            }
        },
        // 不走代理的出口
        {
            "protocol": "freedom",
            "tag": "direct",
            "settings": {}
        }
    ],
    // 设置 dns
    "dns": {
        "servers": [
            "114.114.114.114",
            {
                "address": "1.1.1.1",
                "port": 53,
                "domains": [
                    "geosite:geolocation-!cn"
                ]
            }
        ]
    },
    // 设置路由
    "routing": {
        "domainStrategy": "IPOnDemand",
        "rules": [
            {
                "type": "field",
                "outboundTag": "direct",
                "ip": [
                    "geoip:private"
                ]
            },
            {
                "type": "field",
                "outboundTag": "direct",
                "domain": [
                    "geosite:cn"
                ]
            },
            {
                "type": "field",
                "outboundTag": "direct",
                "ip": [
                    "geoip:cn"
                ]
            },
            {
                "type": "field",
                "outboundTag": "jp-proxy",
                "network": "tcp,udp"
            }
        ]
    }
}
```

