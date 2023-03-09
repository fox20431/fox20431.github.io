# MySQL安装

版本答案：Docker

---

**下面是我自讨苦吃的过程，现在已经不建议使用了，Docker不香吗**

8版本

下载解压

进入mysql顶级目录

创建`my.ini`

```ini
[mysql]
# 设置mysql客户端默认字符集
default-character-set=utf8
[mysqld]
# 设置3306端口
port = 3306
# 设置mysql的安装目录
basedir= D:\mysql-8.0.19-winx64       (需要改）
# 设置mysql数据库的数据的存放目录
datadir= D:\mysql-8.0.19-winx64\data （需要改）
# 允许最大连接数
max_connections=20
# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8
# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
```

管理员身份运行命令行

执行

```shell
# 初始化，会创建相关信息，并将密码打印在控制台
mysqld --initialize --console
# 安装
mysqld --install
# 启动服务
net start mysql
# 使用MySQL，密码为控制台打印的莫玛
mysql -u root -p
```

修改密码

```sql
ALTER USER USER() IDENTIFIED BY 'NewPassword';
```

