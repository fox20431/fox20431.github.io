---
title: Eight-Bit Binary CPU Design
excerpt: Design an eight-bit binary CPU to explore how it works.
---

# Eight-Bit Binary CPU Design

[Video Reference in Bilibili](https://www.bilibili.com/video/BV1aP4y1s7Vf?p=2&vd_source=24924a2b6e399f6354bb051bd87d3bb1)

The video is too long... And I think it will not be long before I forget it even if I finish it.

So I summarize the important content and thought and descript the operating mechanism.

## Prerequisites

1. Understand the Vo Neumann architecture;
2. Install `LogicCircuit`;
3. Be familiar with digital circuits;
4. Be acquainted with the basic logic gate;

## Term

Half adder

Full adder

Subtract with complement 

Understand Digital Tube

R-S flip-flop

D flip-flop

T flip-flop

Traveling Wave Counter

Tri-state gate

Register

3-to-8 decoder

ALU

Microinstruction(AKA. microcode)

## Work Mechanism

To analy the mechanism, we can guess the purpose of the CPU.

CPU is aimed at computing.

How does the human use it to compute?

Program. Compile the high-level language to the assembler, and the assembler is compiled to machine instruction. Machine instruction is a sequence of 0 or 1 signals essentially; it will be loaded to IR(Instruction Register), and its address will be loaded to PC(Program Counter) by order.

I need to know if the CPU always does the fetch-decode-execute cycle.

The Fetch Operation of the CPU is simple; the CPU will fetch the instruction address from the PC and then find the instruction by it.

In general, the decoding process involves breaking down the instruction into its constituent parts, such as the opcode (which specifies the operation to be performed) and any operands (which specify the data to be operated on). The CPU uses the opcode to determine which circuitry within the CPU will be activated to execute the instruction.

After the instruction has been decoded, the CPU executes it by performing the requested operation. This may involve reading data from registers or memory, performing calculations, and storing the result back into a register or memory.

The PC is updated with the next instruction address.

## THERE BE DRAGONS

please distinguish between `microinstruction` and `machine instruction`

`microinstruction`, a part of the `Control Unit`, comprises the basic control signal to control the CPU to execute certain actions, such as `operating ALU`, `reading and writing registers`, etc, it is usually used with `microinstruction memory`.

`Machine instruction` is a basic computer instruction that a computer's CPU can directly execute. The `microinstruction` is called to finish the operation when it's executed.
