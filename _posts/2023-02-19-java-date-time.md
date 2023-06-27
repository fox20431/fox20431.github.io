# Java 的时间

java.util.Date

子类

java.sql.Date

java.sql.Time

java.sql.Timestamp





java.util.Date包含了年月日时分秒

java.sql.Date包含年月日

java.sql.Time包含时分秒

java.sql.Timestamp包含年月日时分秒

从限定名来看可以看出，后三个子类是针对数据库设计的。



mysql关于时间的类型

| 类型名称  | 日期格式            | 日期范围                                          | 存储需求 |
| --------- | ------------------- | ------------------------------------------------- | -------- |
| YEAR      | YYYY                | 1901 ~ 2155                                       | 1 个字节 |
| TIME      | HH:MM:SS            | -838:59:59 ~ 838:59:59                            | 3 个字节 |
| DATE      | YYYY-MM-DD          | 1000-01-01 ~ 9999-12-3                            | 3 个字节 |
| DATETIME  | YYYY-MM-DD HH:MM:SS | 1000-01-01 00:00:00 ~ 9999-12-31 23:59:59         | 8 个字节 |
| TIMESTAMP | YYYY-MM-DD HH:MM:SS | 1980-01-01 00:00:01 UTC ~ 2040-01-19 03:14:07 UTC | 4 个字节 |