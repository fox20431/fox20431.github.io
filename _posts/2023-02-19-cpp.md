# C++

## 基本类型

## 复合类型

除了基本类型还有其他复合类型，即从基本类型组合而来。

- 数组
- 结构体
- 共用体
- 枚举

### 数组

定长，同类型。

### 结构体 struct

**位段 bit field**

```cpp
struct CHAR 
{
    unsigned int ch   : 8;    //8位
    unsigned int font : 6;    //6位
    unsigned int size : 18;   //18位
};
struct CHAR ch1;
```

### 共用体 union

可以防止多个类型变量，但只存储成员中的一个，当存储新的内容时，上个内容丢失

### 枚举 enmu

## 变量在内存的存储

- 自动存储（LIFO）栈模型的先进后出
- 静态存储，整个进程都存在
- 动态存储，new delete
- 线程存储

## 初始化

链接：https://www.zhihu.com/question/403578855/answer/1306943217

默认初始化（default-initialization)，例如`T t;`）

直接（非列表）初始化（direct-(non-list-)initialization，例如`T t(args...);`）

复制（非列表）初始化（copy-(non-list-)initialization)，例如`T t = init;`）

直接列表初始化（direct-list-initialization)，例如`T t{ args... };`）

复制列表初始化（copy-list-initialization，例如`T t = { args... };`）

## 小知识

### 遍历

```c++
int main(int argc, const char * argv[]) {
    vector<int> vec{1,2,3};
    // 遍历 vector
    for(auto it : vec) {
        cout << it << endl;
    }
    return 0;
}
```

**命名空间**

c++ 的命名空间 namespace 目的是防止命名重复，可以看成 java 的全限定名称。

命名空间用法

```cpp
#include <iostream>
// 使用std命名空间下所有方法
using namespace std;
// 实用std命名空间下cout方法
using std::cout;

```

**缩窄转换 narrowing convertions**

- 浮点数 ->整数
- 范围大的浮点数 -> 范围小的浮点数
- 整数哦 -> 浮点数
- 范围大的整数 -> 范围小的整数





