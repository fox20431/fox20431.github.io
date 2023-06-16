---
title: Certificate
---



# Certificate

CA（Certification Authority）证书机构

## Workflow

1. 客户端向服务器发送 SSL 握手请求，请求建立 SSL/TLS 连接。

2. 服务器向客户端发送自己的证书，证书中包含了服务器的公钥和其他信息。

3. 客户端会对证书进行验证，验证的过程如下：

   - 首先，客户端会检查证书是否是由可信的证书颁发机构颁发的。客户端内置了一些可信的证书颁发机构的根证书，如果服务器的证书是由这些机构颁发的，则证书验证通过。

   - 如果服务器的证书不是由可信的证书颁发机构颁发的，则客户端会检查证书链中是否存在中间证书，如果存在，则会对中间证书进行验证，验证通过后再对服务器证书进行验证。

   - 如果证书链中不存在中间证书，则客户端会认为服务器证书不可信，验证失败。

   - 验证通过后，客户端会从证书中获取服务器的公钥，并使用该公钥对一个随机生成的对称密钥进行加密，然后将加密后的密钥发送给服务器。

4. 服务器使用自己的私钥对客户端发送的密钥进行解密，得到对称密钥。

5. 双方使用对称密钥来加密和解密数据，确保数据在传输过程中的安全性。

## Get certification

可以使用`ACME.SH`这类工具申请免费的证书。

申请后会得到后缀为`.pem/.cer/.crt`的文件，这个为网站的证书公开；还会有`.key`为后缀的私钥，这个作为解密用户使用公钥加密的信息，不能公开。

因此要想网站实现SSL，证书和对应的私钥要共同参与工作。

## How Certificate Chains Work

https://knowledge.digicert.com/solution/SO16297.html

证书分为：服务器证书、中间证书（Intermediate Certificate）、根证书（Root Intermediate Certificate）

服务器证书通常是由中间证书签发机构签发的，而中间证书签发机构证书则是由根证书签发的。因此，服务器证书签发链通常是：服务器证书 -> 中间证书签发机构证书 -> 根证书。

这个是`ACME.SH`自动申请到的`fullchain.cer`证书，从上到下分别是 服务器证书 -> ZeroSSL证书 -> The USERTRUST Network证书

```
-----BEGIN CERTIFICATE-----
MIID/TCCA4OgAwIBAgIRAL/n9VhCsm3Kre9Ao0kN/CkwCgYIKoZIzj0EAwMwSzEL
MAkGA1UEBhMCQVQxEDAOBgNVBAoTB1plcm9TU0wxKjAoBgNVBAMTIVplcm9TU0wg
RUNDIERvbWFpbiBTZWN1cmUgU2l0ZSBDQTAeFw0yMzA2MTYwMDAwMDBaFw0yMzA5
MTQyMzU5NTlaMBgxFjAUBgNVBAMMDSouaGlodXNreS5jb20wWTATBgcqhkjOPQIB
BggqhkjOPQMBBwNCAATfbtLiEjjX25hhGiTnjI99ZhCfAqgzCC9Lq0HSippkz1ub
EcTYEiE8SfEKFq4H8E53Y8RnrK/BPpwIeJlYnMy6o4ICeTCCAnUwHwYDVR0jBBgw
FoAUD2vmS845R672fpAeefAwkZLIX6MwHQYDVR0OBBYEFAq0DAVpOV+vKL366CWy
tGqf5+mUMA4GA1UdDwEB/wQEAwIHgDAMBgNVHRMBAf8EAjAAMB0GA1UdJQQWMBQG
CCsGAQUFBwMBBggrBgEFBQcDAjBJBgNVHSAEQjBAMDQGCysGAQQBsjEBAgJOMCUw
IwYIKwYBBQUHAgEWF2h0dHBzOi8vc2VjdGlnby5jb20vQ1BTMAgGBmeBDAECATCB
iAYIKwYBBQUHAQEEfDB6MEsGCCsGAQUFBzAChj9odHRwOi8vemVyb3NzbC5jcnQu
c2VjdGlnby5jb20vWmVyb1NTTEVDQ0RvbWFpblNlY3VyZVNpdGVDQS5jcnQwKwYI
KwYBBQUHMAGGH2h0dHA6Ly96ZXJvc3NsLm9jc3Auc2VjdGlnby5jb20wggEEBgor
BgEEAdZ5AgQCBIH1BIHyAPAAdwCt9776fP8QyIudPZwePhhqtGcpXc+xDCTKhYY0
69yCigAAAYjDIf0JAAAEAwBIMEYCIQCOLYCmDyAclJvFJO2Ph6h3r8uO4q16BJpQ
kVp+DsCnLAIhAPxUrppqnOsmvSXeJbXQHDMM5k8kOkY4a5oHYPDzZW0BAHUAejKM
VNi3LbYg6jjgUh7phBZwMhOFTTvSK8E6V6NS61IAAAGIwyH9XAAABAMARjBEAiBL
JOMbMRTP8hze3eMVBSqvFra1ryZNgNnxEh4+MBqUAQIgeLdWFVzUaQaQ0jMWUcJo
I+2pZpO30S6qPkOtfApA4dQwGAYDVR0RBBEwD4INKi5oaWh1c2t5LmNvbTAKBggq
hkjOPQQDAwNoADBlAjEAhuWdB3LhHHw7N5UOrLWHc9sG+pWwMWmUS90BeP0+jzN0
B8lUEmqVw9Oqf/VPb2KOAjBFjwPNPPN9YkYhh2q4BfzJSApTIei3HNEcJVbe2iMI
SPQvljASR/YDsEvZKZhYvDE=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIDhTCCAwygAwIBAgIQI7dt48G7KxpRlh4I6rdk6DAKBggqhkjOPQQDAzCBiDEL
MAkGA1UEBhMCVVMxEzARBgNVBAgTCk5ldyBKZXJzZXkxFDASBgNVBAcTC0plcnNl
eSBDaXR5MR4wHAYDVQQKExVUaGUgVVNFUlRSVVNUIE5ldHdvcmsxLjAsBgNVBAMT
JVVTRVJUcnVzdCBFQ0MgQ2VydGlmaWNhdGlvbiBBdXRob3JpdHkwHhcNMjAwMTMw
MDAwMDAwWhcNMzAwMTI5MjM1OTU5WjBLMQswCQYDVQQGEwJBVDEQMA4GA1UEChMH
WmVyb1NTTDEqMCgGA1UEAxMhWmVyb1NTTCBFQ0MgRG9tYWluIFNlY3VyZSBTaXRl
IENBMHYwEAYHKoZIzj0CAQYFK4EEACIDYgAENkFhFytTJe2qypTk1tpIV+9QuoRk
gte7BRvWHwYk9qUznYzn8QtVaGOCMBBfjWXsqqivl8q1hs4wAYl03uNOXgFu7iZ7
zFP6I6T3RB0+TR5fZqathfby47yOCZiAJI4go4IBdTCCAXEwHwYDVR0jBBgwFoAU
OuEJhtTPGcKWdnRJdtzgNcZjY5owHQYDVR0OBBYEFA9r5kvOOUeu9n6QHnnwMJGS
yF+jMA4GA1UdDwEB/wQEAwIBhjASBgNVHRMBAf8ECDAGAQH/AgEAMB0GA1UdJQQW
MBQGCCsGAQUFBwMBBggrBgEFBQcDAjAiBgNVHSAEGzAZMA0GCysGAQQBsjEBAgJO
MAgGBmeBDAECATBQBgNVHR8ESTBHMEWgQ6BBhj9odHRwOi8vY3JsLnVzZXJ0cnVz
dC5jb20vVVNFUlRydXN0RUNDQ2VydGlmaWNhdGlvbkF1dGhvcml0eS5jcmwwdgYI
KwYBBQUHAQEEajBoMD8GCCsGAQUFBzAChjNodHRwOi8vY3J0LnVzZXJ0cnVzdC5j
b20vVVNFUlRydXN0RUNDQWRkVHJ1c3RDQS5jcnQwJQYIKwYBBQUHMAGGGWh0dHA6
Ly9vY3NwLnVzZXJ0cnVzdC5jb20wCgYIKoZIzj0EAwMDZwAwZAIwJHBUDwHJQN3I
VNltVMrICMqYQ3TYP/TXqV9t8mG5cAomG2MwqIsxnL937Gewf6WIAjAlrauksO6N
UuDdDXyd330druJcZJx0+H5j5cFOYBaGsKdeGW7sCMaR2PsDFKGllas=
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIID0zCCArugAwIBAgIQVmcdBOpPmUxvEIFHWdJ1lDANBgkqhkiG9w0BAQwFADB7
MQswCQYDVQQGEwJHQjEbMBkGA1UECAwSR3JlYXRlciBNYW5jaGVzdGVyMRAwDgYD
VQQHDAdTYWxmb3JkMRowGAYDVQQKDBFDb21vZG8gQ0EgTGltaXRlZDEhMB8GA1UE
AwwYQUFBIENlcnRpZmljYXRlIFNlcnZpY2VzMB4XDTE5MDMxMjAwMDAwMFoXDTI4
MTIzMTIzNTk1OVowgYgxCzAJBgNVBAYTAlVTMRMwEQYDVQQIEwpOZXcgSmVyc2V5
MRQwEgYDVQQHEwtKZXJzZXkgQ2l0eTEeMBwGA1UEChMVVGhlIFVTRVJUUlVTVCBO
ZXR3b3JrMS4wLAYDVQQDEyVVU0VSVHJ1c3QgRUNDIENlcnRpZmljYXRpb24gQXV0
aG9yaXR5MHYwEAYHKoZIzj0CAQYFK4EEACIDYgAEGqxUWqn5aCPnetUkb1PGWthL
q8bVttHmc3Gu3ZzWDGH926CJA7gFFOxXzu5dP+Ihs8731Ip54KODfi2X0GHE8Znc
JZFjq38wo7Rw4sehM5zzvy5cU7Ffs30yf4o043l5o4HyMIHvMB8GA1UdIwQYMBaA
FKARCiM+lvEH7OKvKe+CpX/QMKS0MB0GA1UdDgQWBBQ64QmG1M8ZwpZ2dEl23OA1
xmNjmjAOBgNVHQ8BAf8EBAMCAYYwDwYDVR0TAQH/BAUwAwEB/zARBgNVHSAECjAI
MAYGBFUdIAAwQwYDVR0fBDwwOjA4oDagNIYyaHR0cDovL2NybC5jb21vZG9jYS5j
b20vQUFBQ2VydGlmaWNhdGVTZXJ2aWNlcy5jcmwwNAYIKwYBBQUHAQEEKDAmMCQG
CCsGAQUFBzABhhhodHRwOi8vb2NzcC5jb21vZG9jYS5jb20wDQYJKoZIhvcNAQEM
BQADggEBABns652JLCALBIAdGN5CmXKZFjK9Dpx1WywV4ilAbe7/ctvbq5AfjJXy
ij0IckKJUAfiORVsAYfZFhr1wHUrxeZWEQff2Ji8fJ8ZOd+LygBkc7xGEJuTI42+
FsMuCIKchjN0djsoTI0DQoWz4rIjQtUfenVqGtF8qmchxDM6OW1TyaLtYiKou+JV
bJlsQ2uRl9EMC5MCHdK8aXdJ5htN978UeAOwproLtOGFfy/cQjutdAFI3tZs4RmY
CV4Ks2dH/hzg1cEo70qLRDEmBDeNiXQ2Lu+lIg+DdEmSx/cQwgwp+7e9un/jX9Wf
8qn0dNW44bOwgeThpWOjzOoEeJBuv/c=
-----END CERTIFICATE-----
```

之所以称之为证书签发链，是因为每个证书都包含 issuer 和 subject 信息。这个可以通过该命令查看：

```sh
openssl x509 -in /path/xxx.crt -noout -text
```

将上述三个证书分为三个文件，分别用上述命令解析得出：

```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            bf:e7:f5:58:42:b2:6d:ca:ad:ef:40:a3:49:0d:fc:29
        Signature Algorithm: ecdsa-with-SHA384
        Issuer: C = AT, O = ZeroSSL, CN = ZeroSSL ECC Domain Secure Site CA
        Validity
            Not Before: Jun 16 00:00:00 2023 GMT
            Not After : Sep 14 23:59:59 2023 GMT
        Subject: CN = *.hihusky.com
...

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            23:b7:6d:e3:c1:bb:2b:1a:51:96:1e:08:ea:b7:64:e8
        Signature Algorithm: ecdsa-with-SHA384
        Issuer: C = US, ST = New Jersey, L = Jersey City, O = The USERTRUST Network, CN = USERTrust ECC Certification A>
        Validity
            Not Before: Jan 30 00:00:00 2020 GMT
            Not After : Jan 29 23:59:59 2030 GMT
        Subject: C = AT, O = ZeroSSL, CN = ZeroSSL ECC Domain Secure Site CA
...

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            56:67:1d:04:ea:4f:99:4c:6f:10:81:47:59:d2:75:94
        Signature Algorithm: sha384WithRSAEncryption
        Issuer: C = GB, ST = Greater Manchester, L = Salford, O = Comodo CA Limited, CN = AAA Certificate Services
        Validity
            Not Before: Mar 12 00:00:00 2019 GMT
            Not After : Dec 31 23:59:59 2028 GMT
        Subject: C = US, ST = New Jersey, L = Jersey City, O = The USERTRUST Network, CN = USERTrust ECC Certification Authority

```

subject 为当前证书的主题（比如这个证书是给谁的证书），issuer则是谁签发的该证书。

所以证书可以通过issuer不断溯源（验证），根据网站提供的证书链直到证书链的最后一个证书，将最后一个证书与系统或者浏览器的支持的证书（这个证书可能是根证书、也可能中间证书）进行校验，如果正确则可以建立安全连接。

那我怎么知道系统（或者浏览器）支持的证书呢？

**Linux**

```sh
cat /etc/ca-certificates.conf
```

**Chrome**

Setting -> Privacy and Security -> Manage device certificates
