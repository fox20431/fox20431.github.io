在项目部署的遇到这样的问题

```
Node Sass does not yet support your current environment: OS X 64-bit with Unsupported runtime (102)
```

这个问题的原因是本地升级了nodejs，版本不同从而导致的无法使用的问题。

解决方案就是安装符合版本的nodejs，这里也说明了选择一个长期支持版本的重要性，不然之后的项目可能因为版本的更新而无法使用。