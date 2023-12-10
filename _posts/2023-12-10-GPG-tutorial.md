---
title: GPG tutorial
date: 2023-12-10
---

# GPG tutorial

GPG（GNU隐私卫士）是一个用于加密、签名和认证数据的工具。它是由GNU计划开发的，是OpenPGP(Pretty Good Privacy)标准的一部分。

## 非对称加密（AKA. 公钥加密）

非对称加密是GPG采用的加密方式，了解该加密方式有助于我们了解GPG。

此外SSH、HTTPS（PKI）等也是适用的该加密方式。

### 使用方法

非对称密钥中私钥需要个人保管，公钥用于公开。

*私钥包含了公钥的信息，可以从私钥中提取出公钥。*

**加密**

公钥加密，只有私钥持有者能够解密。

**签名**

用私钥加密的部分，称为签名。因为私钥无法伪造，所以用私钥加密过的签名也无法伪造，公钥用于解密校验。

## 常见应用应用

APT包，要求我们用`.gpg`的公钥验证私钥加密的签名，从而确保包是否被篡改。

## 用法

虽然GPG与SSH的密钥对都是使用公钥加密算法得出，但由应用场景不同，其应用生成的密钥对不通用。

1. GPG生成密钥对：

    ```sh
    gpg --gen-key
    ```

    这个命令执行过程中会要求输入名字和邮箱，同时要求输入一个passphrase。

    输出：

    ```
    pub   ed25519 2023-12-10 [SC] [expires: 2026-12-09]
          16651313F10CC15C7B6A5E2FE65AE788837E2A89
    uid                      Your Name <test@email.com>
    sub   cv25519 2023-12-10 [E] [expires: 2026-12-09]
    ```

    - pub ed25519 表示这个公钥使用的是 Ed25519 加密算法。
    - 2023-12-10 是这个公钥创建的日期。
    - [SC] 表示这是一个签名密钥（Signatures Capable），可以用来给文件或消息签名。
    - [expires: 2026-12-09] 表示这个公钥的有效期截止到 2026 年 12 月 9 日。
    - 16651313F10CC15C7B6A5E2FE65AE788837E2A89 是这个公钥的 ID，用于在公钥服务器上查找和验证公钥。
    - uid Your Name [test@email.com](mailto:test@email.com) 是这个公钥的所有者的标识信息，包括姓名和电子邮件地址。
    - sub cv25519 表示这个公钥同时也支持 Curve25519 密钥交换算法。
    - [E] 表示这个公钥可以用于加密（Encryption）。
    - [expires: 2026-12-09] 表示这个公钥的有效期截止到 2026 年 12 月 9 日。

2. 查看 GPG 密钥列表：

    ```sh
    gpg --list-keys
    ```

3. 加密文件

   ```sh
   echo "this is a test ascii message" > test.asc
   gpg -e -r 'Your Name' .\test.asc
   ```

   会生成 `test.asc.gpg` 加密文件，其内容无法识别内容。

4. 解密文件

   ```sh
   gpg -d .\test.asc.gpg
   ```

   由于时要使用私钥，需要输入passphrase，命令输出：

   ```
   gpg: encrypted with cv25519 key, ID 6768773254A18EA2, created 2023-12-10
         "Your Name <test@email.com>"
   this is a test ascii message
   ```

5. 公钥分享

   到此你就可以分享你的公钥给朋友们，来进行加密交流。导出公钥：

   ```sh
   gpg --export --armor 6768773254A18EA2 > gpgkey.pub.asc
   ```

**指纹**

指纹是通过将密钥的公钥部分进行哈希计算而生成的，用于判断公钥的身份，比如你可以告诉别人自己的GPG指纹，别人可以通过该指纹验证公钥是否是你的。

获取指纹：

```sh
gpg --fingerprint $GPG_PUB_KEY_ID
```

输出：

```
pub   ed25519 2023-12-10 [SC] [expires: 2026-12-09]
      1665 1313 F10C C15C 7B6A  5E2F E65A E788 837E 2A89
uid           [ultimate] Ming Li <fox20431@gmail.com>
sub   cv25519 2023-12-10 [E] [expires: 2026-12-09]
```

`1665 1313 F10C C15C 7B6A  5E2F E65A E788 837E 2A89` 为指纹。

**密钥备份**

```sh
gpg -a -o gpgkey.asc --export-secret-keys $GPG_PUB_KEY_ID
```



