# C++ Vector

`push_back()` 与  `pop_back()` 是一对函数方法，分别对应压栈和出栈。

但是 `pop_back()` 只是从表面上删除了数组最后一个元素，实际上那个地址上的数字仍然存在。

你可以通过下面测试：

```cpp
#include <iostream>
#include <vector>

int main(int argc, const char * argv[]) {
    using namespace std;
    vector<int> obj;
    obj.push_back(1);
    obj.push_back(2);
    obj.push_back(3);
    obj.pop_back();
    cout << obj.size() << endl;
  	cout << obj[2] << endl;
    return 0;
}
```

你删除后数组大小发生了变化，但仍然能访问到数据。

