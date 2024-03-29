了解进制

了解CPU结构

![image-20210709020623201](assets/image-20210709020623201.png)



# 处理器架构、指令集和汇编语言

1. 处理器架构就是处理器的硬件架构，称为微架构。是一堆硬件电路，去实现指令集所规定的操作运算。
2. 是的，指令集决定了处理器的架构，因为处理器架构就是用硬件电路实现指令集。但是具体用什么样的处理器架构，设计怎样的硬件电路，每个人设计的都可以不一样。
3. MIPS是一种采取[精简指令集](https://zh.wikipedia.org/wiki/精简指令集计算机)（RISC）的[处理器](https://zh.wikipedia.org/wiki/處理器)架构，既有指令集，也有相应的处理器架构。大名鼎鼎的龙芯就是MIPS的。
4. 汇编语言是用人类看得懂的语言来描述指令集。否则指令集的机器码都是一堆二进制数字，人类读起来非常麻烦，但汇编是用类似人类语言的方式描述指令集，读起来方便多了。

要设计处理器，首先就需要有指令集，规定处理器相应操作，通过指令集去控制处理器实现相应功能。但处理器是一堆硬件电路，只能识别二进制数据，所以指令集是由一堆二进制数据组成。而二进制数据对人类来说读起来很麻烦。为了方便人类操作指令集，发明了汇编语言来描述指令集。汇编语言类似人类语言，读起来方便多了。

虽然汇编语言读起来方便了，但也有缺陷。首先汇编语言操作起来还是挺麻烦的。其次汇编语言对应一条条指令集，所以当指令集改变时，就得修改相应汇编语言，导致其可移植性很差，不能跨平台使用，如ARM的汇编语言与Intel X86的就不同。这时人们就想开发一种更方便操作，超越指令集的语言，于是有了C，C++等**高级语言**。
但处理器只能识别二进制码，那怎么能识别高级语言呢？于是人们开发了**编译器**，依照如下顺序，将高级语言翻译成二进制码：高级语言 &rarr; 汇编语言 &rarr; 二进制机器码。
至此，人类可以很方便的利用高级语言编写程序，控制处理器完成相应功能。然后程序员这个红火的职业就此大规模诞生了。