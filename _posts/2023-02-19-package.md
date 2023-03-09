# 包

## 包语句语法格式
包名必须与相应的字节码所在的目录结构相吻合  
`package pkg1[.pkg2[...]];`  
例如：  
```
package net.java.util;
public class HelloWorld{
	...
}
```
对应的路径是`net/java/util/HelloWorld.java`  

## 导入包
使用关键字**import**  
`import pkg1[.pkg2[...]].classname(.class method|member);`  
例如：  
`import java.lang.Math`，即引入java.lang.Math
