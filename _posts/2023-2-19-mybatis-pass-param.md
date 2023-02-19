## 直接传参

略

## 顺序传参

通过指定参数的序号

```java
public User selectUser(String name, int deptId);
```

```xml
<select id="selectUser" resultMap="UserResultMap">
    select * from user
    where user_name = #{0} and dept_id = #{1}
</select>
```

## @Param传参

```java
public User selectUser(@Param("userName") String name, int @Param("deptId") deptId);
```

```xml
<select id="selectUser" resultMap="UserResultMap">
    select * from user
    where user_name = #{userName} and dept_id = #{deptId}
</select>
```

## Map传参

```java
public User selectUser(Map<String, Object> params);
```

```xml
<select id="selectUser" parameterType="java.util.Map" resultMap="UserResultMap">
    select * from user
    where user_name = #{userName} and dept_id = #{deptId}
</select>
```

## Java Bean传参

```java
public User selectUser(Map<String, Object> params);
```

```xml
<select id="selectUser" parameterType="com.test.User" resultMap="UserResultMap">
    select * from user
    where user_name = #{userName} and dept_id = #{deptId}
</select>
```

