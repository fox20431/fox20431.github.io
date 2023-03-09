# Optional

Optional是对象容器，jdk1.8加入的特性。

## 目的

-    提示用户要注意该对象有可能为null
-    简化if else代码

## 方法介绍

1. 创建：

    Optional.empty()： 创建一个空的 Optional 实例

    Optional.of(T t)：创建一个 Optional 实例，当 t为null时抛出异常 

    Optional.ofNullable(T t)：创建一个 Optional 实例，但当 t为null时不会抛出异常，而是返回一个空的实例

2. 获取：

    get()：获取optional实例中的对象，当optional 容器为空时报错

3. 判断：

    isPresent()：判断optional是否为空，如果空则返回false，否则返回true

    ifPresent(Consumer c)：如果optional不为空，则将optional中的对象传给Comsumer函数

    orElse(T other)：如果optional不为空，则返回optional中的对象；如果为null，则返回 other 这个默认值

    orElseGet(Supplier<T> other)：如果optional不为空，则返回optional中的对象；如果为null，则使用Supplier函数生成默认值other

    orElseThrow(Supplier<X> exception)：如果optional不为空，则返回optional中的对象；如果为null，则抛出Supplier函数生成的异常

4. 过滤：

    filter(Predicate<T> p)：如果optional不为空，则执行断言函数p，如果p的结果为true，则返回原本的optional，否则返回空的optional  

5. 映射：

    map(Function<T, U> mapper)：如果optional不为空，则将optional中的对象 t 映射成另外一个对象 u，并将 u 存放到一个新的optional容器中。

    flatMap(Function< T,Optional<U>> mapper)：跟上面一样，在optional不为空的情况下，将对象t映射成另外一个optional

    区别：map会自动将u放到optional中，而flatMap则需要手动给u创建一个optional

## 演示

**需求：**

  学校想从一批学生中，选出年龄大于等于18，参加过考试并且成绩大于80的人去参加比赛。

**准备数据：**

```java
public class Student {
    private String name;
    private int age;
    private Integer score;
    //省略 construct get set
}

public List<Student> initData(){
    Student s1 = new Student("张三", 19, 80);
    Student s2 = new Student("李四", 19, 50);
    Student s3 = new Student("王五", 23, null);
    Student s4 = new Student("赵六", 16, 90);
    Student s5 = new Student("钱七", 18, 99);
    Student s6 = new Student("孙八", 20, 40);
    Student s7 = new Student("吴九", 21, 88);
    return Arrays.asList(s1, s2, s3, s4, s5, s6, s7);
}
```

**非Optional写法：**

```java
@Test
public void beforeJava8() {
    List<Student> studentList = initData();
 
    for (Student student : studentList) {
        if (student != null) {
            if (student.getAge() >= 18) {
                Integer score = student.getScore();
                if (score != null && score > 80) {
                    System.out.println("入选：" + student.getName());
                }
            }
        }
    }
}
```

**Optional写法：**

```java
@Test
public void useJava8() {
    List<Student> studentList = initData();
    for (Student student : studentList) {
        Optional<Student> studentOptional = Optional.of(student);
        Integer score = studentOptional.filter(s -> s.getAge() >= 18).map(Student::getScore).orElse(0);
 
        if (score > 80) {
            System.out.println("入选：" + student.getName());
        }
    }
}
```

