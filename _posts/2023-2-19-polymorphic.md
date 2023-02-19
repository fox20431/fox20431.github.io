# 多态

不同类型的多态

## 重写(override)

运行、编译时多态
## 重载(overload)
编译时多态
## 向上转型

子类型转换成父类型

由于子类包含父类的所有内容，所以可以从子类中提取出父类来创建父类。

运行时多态

## 向下转型
子类型转换成父类型

向下转型是不安全的，有可能会报错。因为子类继承父类，那么子类的范围会大于等于父类，那么将父类转型为子类条件不能完全满足，从而产生错误。

运行时多态

## 示例

向上转型和向下转型

```java
public class Animail {
    private String name="Animail";
    public void eat(){
        System.out.println(name+" eate");
    }
}

class Human extends Animail{
    private String name="Human";
    public void eat(){
        System.out.println(name+" eate");
    }
}

class Main {
    public static void main(String[] args) {
        Animail a1=new Human();//向上转型
        Animail a2=new Animail();
        Human b1=(Human)a1;// 向下转型,编译和运行皆不会出错
        // Human c=(Human)a2;//不安全的向下转型,编译无错但会运行会出错
    }
}
```

