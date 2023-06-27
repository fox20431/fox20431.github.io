# Spring Boot配置SSL

## 生成证书

详情参考：https://www.baeldung.com/spring-boot-https-self-signed-certificate

```sh
keytool -genkeypair -alias <cert-name> -keyalg RSA -keysize 2048 -storetype PKCS12 -keystore <filename>.p12 -validity 3650
```

`storetype`有两种类型，推荐使用`PKCS`：

- PKCS12: [Public Key Cryptographic Standards](https://en.wikipedia.org/wiki/PKCS_12) is a password-protected format that can contain multiple certificates and keys; it's an industry-wide used format
- JKS: [Java KeyStore](https://en.wikipedia.org/wiki/Keystore) is similar to PKCS12; it's a proprietary format and is limited to the Java environment.

## 配置Spring Boot项目

证书放入`resources`目录下，并配置文件：

```properties
server.ssl.enabled=true
server.ssl.key-store-type=PKCS12
server.ssl.key-store=classpath:<filename>.p12
server.ssl.key-store-password=<store-password>
server.ssl.keyAlias=<cert-name>
```

由于是个人创建证书的问题，访问`https:localhost`会提示证书问题。

同时postman和curl都会出现一些证书问题，但都能解决。curl通过添加参数`-k`。

## 题外话

不指定协议和端口的情况下，默认访问80端口。

端口：80
服务：HTTP说明：用于网页浏览。
端口：443
服务：Https
说明：网页浏览端口，能提供加密和通过安全端口传输的另一种HTTP。







