---
title: alogrithms and data structure note
date: 2024-03-12
---

# 数据结构与算法笔记



**如何评价一个算法的优劣**

- 时间复杂度
- 空间复杂度
- 可读性
- 可维护性
- 稳定性
- 可拓展性

展开讲讲时间复杂度

### 时间复杂度

#### O(1) - 常数时间复杂度

表示算法的运行时间是一个常数。不论输入规模的大小如何，算法的执行时间都相同。

```py
def example_algorithm(array):
    return array[0]
```

#### O(log n) - 对数时间复杂度

表示算法的运行时间与输入规模的对数成正比。通常出现在二分查找等分治算法中。

```py
def binary_search(array, target):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

#### O(n log n) - 线性对数时间复杂度

通常出现在一些高效的排序算法中，如归并排序和快速排序。

#### O(n) - 线性时间复杂度

```py
def linear_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1
```

#### O(n^2) - 平方时间复杂度

```python
def quadratic_algorithm(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Do something
```

#### O(2^n) - 指数时间复杂度

通常出现在递归算法中，其中每一步都分成两个可能的递归调用。

```python
def exponential_algorithm(n):
    if n <= 1:
        return n
    else:
        return exponential_algorithm(n-1) + exponential_algorithm(n-2)
```

## hash



## hashmap