# Postgre SQL

数据库

## Getting Start

安装

```sh
pkg-mgr install postgresql
```

启动服务

```sh
# systemctl
systemctl start postgresql
systemctl enable postgresql
# brew
brew services restart postgresql
```

postgresql 默认创建 postgres 数据库，同时安装客户端命令行工具`qsql`：

```shell
# 查看帮助
psql --help
```

进入进入 postgres 数据库，不指明用户的情况下默认当前系统用户（也是最大权限）。

```sh
# if you don't specify the username
# it will get in database using current system username
psql [-U <USERNAME>] <DATABASE>
```

建议创建新的用户：

```sh
CREATE ROLE <username> WITH LOGIN PASSWORD '<password>';
# 给用户创建数据库的权限
ALTER ROLE <username> CREATEDB;
```

用新角色登录

```sh
psql postgres <username>
# or
psql postgres --username=<username> --pasword
```

查看当前连接信息（可用来查看当前用户）

```sql
\conninfo
```

查看配置信息：

```sql
show all;
```

通过配置信息我们能看到所有配置参数，这里列出一些**重要参数**：

- 端口：5432（默认端口）

## Operation

以下所有操作均在`psql`命令行中执行：

### Although Simple, Useful

```sql
# backslash command help
\?
# sql help
\h
```

多看帮助和文档，postgresql的帮助和文档写的还是蛮好。

### Common Backslash Command

```sql
# 显示数据库
\l
# 切换数据库
\c <db_name>
```

### SQL

PostgreSQL的SQL和标准SQL差不多，但有以下区别：

- 自增选择用`serial`关键字；
- 表和字段等不能加引号（区别其他数据库）；
- 表依附于模式（schema）；

表操作

```sql
# 正常sql创建
# 显示表 describe table
\dt
\dt+

# 创建表
CREATE TABLE IF NOT EXISTS public.article
(
    id bigint NOT NULL DEFAULT nextval('article_id_seq'::regclass),
    title "char"[] NOT NULL,
    content text[] COLLATE pg_catalog."default",
    CONSTRAINT article_pkey PRIMARY KEY (id)
)
# 修改表属性
# operation: add drop alter modify
alter table <table_name> <operation>
# 像这样
alter table public.user alter column "id" type bigint;
alter table public.user add constraint user_username_key unique(username);
```

约束

```sql
# 添加序列，自增
create sequence <tablename_colname_seq> sa <type>
alter table <table_name> alter <column> set default nextval('<tablename_colname_seq>')
# 设置自增的下一个数
select setval('my_schema.users_id_seq', 10000000);
```

## Q&A

How to scroll up in long output?

```bash
export PAGER = less
```

ref: https://stackoverflow.com/questions/48938202/postgresql-how-to-scroll-up-in-long-output

