# 用户处理
## 创建用户
指定ip地址连接
```sql
create user <$user_name>@<$ip_adress> identified by '<$passwd>';
```  
## 用户授权
```sql
grant <$privileges> on <$databses_name>.<$table_name> to <$user_name>@<$ip_adress> [identified by '<$passwd>'];
```  
privileges:
- all privileges
- select
- ...

## 回收权限

```sql
revoke <$privileges> on <$databses_name>.<$table_name> to <$user_name>@<$ip_adress> [identified by '<$passwd>'];
```

## 刷新权限
`flush privileges;`

## 删除用户
`drop user <$user_name>@<$ip_adress>;`


## 查看用户信息
登录mysql数据库：mysql -u root -p
　　mysql> use mysql;
　　查询host值：
mysql> select user,host from user;
