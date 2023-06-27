---

title: Throwable
---



# Throwable

The following class diagram is the inheritance diagram about the `Throwable`:

```mermaid
classDiagram
	Throwable <|-- Error
	Throwable <|-- Exception
	Exception <|-- RuntimeException
	class Throwable {
		+Long serialVersionID
		+Object backtrace
		+String detailMessage
	}
```





## Error vs Exception vs RuntimeException

在`Throwable`继承关系中，我们只需要关心`Error`，`Exception`和`RuntimeException`。

先说结论：

| 类名             | 编译是否需要被捕获 | try-catch捕获是否生效 |
| ---------------- | ------------------ | --------------------- |
| Error            | 是                 | 否                    |
| Exception        | 是                 | 是                    |
| RuntimeException | 否                 | 是                    |

**如果程序中有异常没有被捕获，会导致当前线程终止，从而出现异常之后的代码是运行不到的。**

### 对比试验

接下来代码均使用下述代码进行编译运行：

```sh
javac Class.java -d .
java main.Main
```

**代码1-1：**

```java
package main;

public class Main {
    public static void main(String[] args) {
        System.out.println("Before");
        try {
            throw new Error("Error.");
        } catch (Exception e) {
            System.out.println("Catch");
        }
        System.out.println("After");
    }
}
```

**编译通过，无输出**

**运行输出：**

```log
Before
Exception in thread "main" java.lang.Error: Error.
        at main.Main.main(Main.java:7)
```

**代码1-2：**

```java
package main;

public class Main {
    public static void main(String[] args) {
        System.out.println("Before");
        throw new Error("Error");
        System.out.println("After");
    }
}
```

**编译失败，输出：**

```log
.\Main.java:7: error: unreachable statement
        System.out.println("World!");
        ^
1 error
```



**代码2-1：**

```java
package main;

public class Main {
    public static void main(String[] args) {
        System.out.println("Before");
        try {
            throw new Exception("Exception.");
        } catch (Exception e) {
            System.out.println("Catch");
        }
        System.out.println("After");
    }
}
```

**编译通过，无输出**

**运行输出：**

```log
Before
Catch
After
```

**代码2-2：**

```java
package main;

public class Main {
    public static void main(String[] args) {
        System.out.println("Before");
        throw new Exception("Exception");
        System.out.println("After");
    }
}
```

**编译失败，输出：**

```log
Exception in thread "main" java.lang.Error: Unresolved compilation problems: 
        Unhandled exception type Exception
        Unreachable code

        at main.Main.main(Main.java:6)
```

**代码3-1：**

```java
package main;

public class Main {
    public static void main(String[] args) {
        System.out.println("Before");
        try {
        	throw new RuntimeException("Exception");
        } catch (Exception e) {
            System.out.println("Catch");
        }
        System.out.println("After");
    }
}
```

**编译通过，无输出**

**运行输出：**

```log
Before
Catch
After
```

**代码3-2：**

```java
package main;

public class Main {
    public static void main(String[] args) {
        System.out.println("Before");
        throw new RuntimeException("Exception");
        System.out.println("After");
    }
}
```

**编译通过，无输出**

**运行输出：**

```log
Exception in thread "main" java.lang.Error: Unresolved compilation problem: 
        Unreachable code

        at main.Main.main(Main.java:7)
```



## 异常类型

### RuntimeException

运行时异常：

此类异常为unchecked（非受查）

即编译不会检测出异常，运行时才会出现的异常  

常见的类型有：

- NullPointerException
- ArithmeticException
- ClassCastException
- IndexOutOfBoundsException
- IllegalArgumentException

### OtherException（编译时异常）

编译时异常：

此类异常为checked（受查）

即编译时会检测出异常

常见的类型有：

- FileNotFoundException
- ClassNotFoundException
- SQLException
- NoSuchFieldException
- NoSuchMethodException
- ParseException

## 错误与异常区别

- 异常可以是受查或非受查的，错误总是非受查的；
- 异常是由代码导致的，错误是由系统或者低层资源导致的；
- 异常在应用级被处理，能够识别的错误会在系统级被捕捉；

## 异常处理
### 捕获异常：try&catch&finally
``` java
try{...} 
// one or more catch statements
catch (<$EX_CLASS> <$VAR_NAME> [|<$EX_CLASS> <$VAR_NAME> [...]]){...}
finally{...}
```

- **try**：运行代码，若遇到异常则try内代码停止运行  
- **catch**：若前者出现异常，将捕获异常并运行catch代码  
	若前者为出现异常，则无法捕获异常，catch内代码也不会运行  
- **finally**：无论是否出现异常，无差别运行finally内代码  

**try内声明的变量只能在try内部使用**  

示例：  
``` java
public class DealException
{
    public static void main(String args[])
    {    
        try
        //要检查的程序语句
        {
            int a[] = new int[5];
            a[10] = 7;//出现异常
        }
        catch(ArrayIndexOutOfBoundsException e)
        //异常发生时的处理语句
        {
            System.out.println("超出数组范围！");
        }
        finally
        //这个代码块一定会被执行
        {
            System.out.println("*****");
        }
        System.out.println("异常处理结束！");
    }
}
```
Tips：  
1. 一个try语句可以对应多个catch语句
2. 若存在多个catch语句，按照java.lang.Object类从子到父排列  
3. 一个catch语句可以捕捉多个异常，不同异常之间用`|`隔开  
4. 异常类声明的对象默认被final修饰  

### 抛出异常：throw
`throw <$EX_OBJ>`  
其他异常抛出来自代码逻辑，throw是主观意愿的手动抛出异常  
两者最终结果的作用相同  
出现在函数体中，抛出异常后终止  

### 声明异常：throws
`func throws <$EX_OBJ>`  
将自身异常提交给上级（调用者/JVM）  
从而确保自身在编译过程中不出现异常  


## 自定义异常
1. 创建类
2. 继承Exception或Exception的子类
3. 重写构造方法
如何让自定义异常发挥作用？  
依靠throw来抛出自定义的异常  
```
public class NoMappingParamString extends Exception {
    //无参构造函数
    public NoMappingParamString(){
        super();
    }
    
    //用详细信息指定一个异常
    public NoMappingParamString(String message){
        super(message);
    }
    
    //用指定的详细信息和原因构造一个新的异常
    public NoMappingParamString(String message, Throwable cause){
        super(message,cause);
    }
    
    //用指定原因构造一个新的异常
    public NoMappingParamString(Throwable cause) {
        super(cause);
    }
}
```


## Q&A

### 捕获异常为什么不使用if&else，而是用try&catch&finally？

- 代码臃肿  
- 处理繁琐  
- 无法区分业务代码和异常代码  

### throw与throws的异同

相同：

- throw与throws单词类似
- 后均跟异常类
- 都是对异常的处理

不同：  

- throw是给自己创造困难从而磨炼自己，throws是甩锅给上级让自己过的安稳  
- throw写在结构体中，throws写在声明方法中  
