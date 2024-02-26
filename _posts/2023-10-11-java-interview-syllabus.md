---
title: Java Interview Syllabus
date: 2023-10-11
---

# Java面试大纲

Q

StringBuilder 和 StringBuffer

A

StringBuilder 和 StringBuffer 均继承 AbstractStringBuilder ，所以实现相似，构建字符串。

其中重要差别在于 StringBuffer 主旨是线程安全，从 `append(...)` 方法声明的关键字可以看出，StringBuffer 使用了 `synchronized `关键字。

> 使用 `synchronized` 关键字创建同步代码块，指定对象为全局锁，只有持有锁的线程才能执行改代码，从而实现线程安全。`synchronized` 线程安全的代价是是的代码性能降低。

---

Q

HashMap 和 ConcurrentHashMap

A

Q

volatile

A

可见性、操作是否原子、重排序

---

Q

双亲委派

A



---