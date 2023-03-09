# keytool

https://jingyan.baidu.com/article/6079ad0eb284ad28ff86db18.html

alias指定生成密钥对的别名

keyalg指定生成密钥的算法

validity指定证书的有效期，单位为天

keystore指定密钥库的存储路径

storepass指定密钥库的密码



创建含有server_cert的keystore：

```sh
keytool -genkeypair -alias <cert-name> -keyalg RSA -keysize 2048 -storetype PKCS12 -keystore <filename>.p12 -validity 3650
```

查看证书文件详情：

```sh
keytool -list -v -keystore server.keystore -storepass <storepass>
```

导出证书：

```sh
keytool -export -alias server_cert -keystore server.keystore -file tomcat_server.cert
```

