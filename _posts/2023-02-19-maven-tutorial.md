---
title: Maven Tutorial
---

# Maven Tutorial

安装配置路径

**settings.xml配置文件优先级**

1. 位于Maven安装目录下的conf文件夹中的settings.xml文件是全局配置文件。
2. 位于用户的主目录下（例如：C:\Users\YourUsername\.m2\settings.xml）的settings.xml文件是用户级别的配置文件。
3. 指定项目自定义的settings.xml文件路径，例如：`--settings /path/to/custom/settings.xml`

Maven的settings.xml文件的优先级别是从高到低：项目配置 > 用户配置 > 全局配置。

**代理配置** 

1. 运行命令时向VM传参

   ```sh
   -DproxySet=true -DproxyHost=127.0.0.1 -DproxyPort=7890
   ```

   对于idea可以在`Setting > Maven > Importing > VM options for importer` 位置中指定。

2. 配置`settings.xml`文件

   ```xml
   <settings xmlns="http://maven.apache.org/SETTINGS/1.2.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.2.0 https://maven.apache.org/xsd/settings-1.2.0.xsd">
       ...
   	<proxies>
           <proxy>
                 <id>default</id>
                 <active>true</active>
                 <protocol>http</protocol>
                 <username></username>
                 <password></password>
                 <host>127.0.0.1</host>
                 <port>7890</port>
                 <nonProxyHosts></nonProxyHosts>
           </proxy>
     	</proxies>
       ...
   </settings>
   ```

   

**常见命令**

```sh
# maven warpper
mvn wrapper:wrapper
# 创建项目，创建src目录结构及相关文件
mvn build
# 下载依赖
mvn install
# 编译项目，编译到target目录
mvn compile
# 清除编译内容
mvn clean
# 先清理后编译
mvn clean compile
# 编译并测试
mvn compile test
```



下载源码
为了下载源码，首先我们需要进入pom.xml所在的目录然后执行下面命令：
To download just the sources, first, we should navigate to the directory containing the pom.xml and then execute the command:
mvn dependency:sources
下载javadocs文档
下载源码可能会花费一段时间。类似的，为了只下载javadocs，我们可以发出下面命令：
It may take a while to download the sources. Similarly, to download just the Javadocs, we can issue the command:
mvn dependency:resolve -Dclassifier=javadoc
当然，我们也可以下载他们两者用一个命令：
Of course, we can download both of them in one command, too:
mvn dependency:sources dependency:resolve -Dclassifier=javadocmaven

更改本地Maven的镜像源

以Linux系统为例，使用 `mvn -v` 可以查看 maven home目录。

在 maven home 目录中会发现 `{MVN_HOME}/conf/settings.xml`

在mirrors中添加新的`mirror`在其他mirror之前：

```xml
  <mirrors>
    <mirror>
      <id>alimaven</id>
      <mirrorOf>central</mirrorOf>
      <name>Aliyun Maven</name>
      <url>http://maven.aliyun.com/nexus/content/groups/public/</url>
    </mirror>
  </mirrors>
```

