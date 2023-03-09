
## 用法

```sql
Alter table 表名 add constraint FK_ID foreign key(外键字段名) REFERENCES 外表表名(主键字段名)；
```

## 外键约束删除时和更新时各取值的含义

### 类型

RESTRICT（默认，限制），CASCADE（级联），NO ACTION，SET NULL属性

### 解释

当取值为No Action或者Restrict时，则当在父表（即外键的来源表）中删除对应记录时，首先检查该记录是否有对应外键，如果有则不允许删除。

当取值为Cascade时，则当在父表（即外键的来源表）中删除对应记录时，首先检查该记录是否有对应外键，如果有则也删除外键在子表（即包含外键的表）中的记录。


当取值为Set Null时，则当在父表（即外键的来源表）中删除对应记录时，首先检查该记录是否有对应外键，如果有则设置子表中该外键值为null（不过这就要求该外键允许取null）。

### Tips
RESTRICT，NO ACTION两者在数据库起到的效果等价