- 预处理器：将.c 文件转化成 .i文件，使用的gcc命令是：gcc –E，对应于预处理命令cpp；
- 编译器：将.c/.h文件转换成.s文件，使用的gcc命令是：gcc –S，对应于编译命令 cc –S；
- 汇编器：将.s 文件转化成 .o文件，使用的gcc 命令是：gcc –c，对应于汇编命令是 as；
- 链接器：将.o文件转化成可执行程序，使用的gcc 命令是： gcc，对应于链接命令是 ld；
- 加载器：将可执行程序加载到内存并进行执行，loader 和 [ld-linux.so](http://ld-linux.so/)。

