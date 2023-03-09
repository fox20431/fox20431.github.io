# HttpURLConnection 明文传输问题

## 起因

> Starting with Android 9 (API level 28), cleartext support is disabled by default.

[Android developers官方原文](https://developer.android.com/training/articles/security-config#CleartextTrafficPermitted)

## 现象

如果采用明文传输将出现如下报错：

```
08-29 12:03:11.246 11285-11285/ E/: [12:03:11.245, main]: Exception: IOException java.io.IOException: Cleartext HTTP traffic to * not permitted
at com.android.okhttp.HttpHandler$CleartextURLFilter.checkURLPermitted(HttpHandler.java:115)
at com.android.okhttp.internal.huc.HttpURLConnectionImpl.execute(HttpURLConnectionImpl.java:458)
at com.android.okhttp.internal.huc.HttpURLConnectionImpl.connect(HttpURLConnectionImpl.java:127)
at com.deiw.android.generic.tasks.AbstractHttpAsyncTask.doConnection(AbstractHttpAsyncTask.java:207)
at com.deiw.android.generic.tasks.AbstractHttpAsyncTask.extendedDoInBackground(AbstractHttpAsyncTask.java:102)
at com.deiw.android.generic.tasks.AbstractAsyncTask.doInBackground(AbstractAsyncTask.java:88)
at android.os.AsyncTask$2.call(AsyncTask.java:333)
at java.util.concurrent.FutureTask.run(FutureTask.java:266)
at android.os.AsyncTask$SerialExecutor$1.run(AsyncTask.java:245)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1162)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:636)
at java.lang.Thread.run(Thread.java:764)
```

## 解决

提示：
网络传输需要获取网络权限，添加`uses-permission android:name="android.permission.INTERNET" />`到`AndroidManifest.xml`中：

```xml

<manifest ...>
  ...
	<uses-permission android:name="android.permission.INTERNET" />
  ...
</manifest>
```

方案一

不使用文明，将`http://`改为`https://`

方案二

Create file `res/xml/network_security_config.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <domain-config cleartextTrafficPermitted="true">
        <domain includeSubdomains="true">api.example.com(to be adjusted)</domain>
    </domain-config>
</network-security-config>
```

`AndroidManifest.xml`

```
<?xml version="1.0" encoding="utf-8"?>
<manifest ...>
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        ...
        android:networkSecurityConfig="@xml/network_security_config"
        ...>
        ...
    </application>
</manifest>
```

方案三

如果仅仅是允许明文传输，你可以用更简单的方法

`AndroidManifest.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest ...>
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        ...
        android:usesCleartextTraffic="true"
        ...>
        ...
    </application>
</manifest>
```

