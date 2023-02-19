在Spring Security

角色和权限等价，千万不要犯一个错误就是说，角色拥有多个权限。

角色和权限在Spring Security中都只是字符串，区别角色与权限就是角色字符串前面多个`ROLE_`，在匹配过程中可以使用`hasRole`来匹配
