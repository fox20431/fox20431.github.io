---
title: python docstring
date: 2023-08-07
---

# Python Docstring



1. **模块级别文档字符串：** 在模块开头，你可以使用三重引号 `"""` 来编写模块级别的文档字符串，描述模块的功能、用法等信息。

   ```python
   """This module provides utility functions for working with strings."""
   ```

2. **函数和方法文档字符串：** 在函数或方法的定义之后，用三重引号 `"""` 编写文档字符串，描述函数的作用、参数、返回值等信息。

   ```python
   pythonCopy codedef calculate_average(numbers):
       """
       Calculate the average of a list of numbers.
       
       Args:
           numbers (list): A list of numerical values.
       
       Returns:
           float: The calculated average.
       """
       # 实际函数实现在这里
   ```

3. **类文档字符串：** 在类的定义之后，使用三重引号 `"""`  或 `'''` 编写文档字符串，描述类的作用、属性、方法等信息。

   ```python
   pythonCopy codeclass Person:
       """
       A class representing a person.
       
       Attributes:
           name (str): The name of the person.
           age (int): The age of the person.
       """
       
       def __init__(self, name, age):
           self.name = name
           self.age = age
       
       def say_hello(self):
           """Print a greeting message."""
           print(f"Hello, my name is {self.name}!")
   ```

4. **docstring 格式：** docstring 应该是一段清晰、简明的描述，通常包括描述、参数、返回值等信息。可以使用标准的 reStructuredText 或 Google 风格的格式。

   ```python
   pythonCopy codedef function_name(param1, param2):
       """
       Brief description of the function.
       
       Args:
           param1 (type): Description of parameter 1.
           param2 (type): Description of parameter 2.
       
       Returns:
           type: Description of the return value.
       """
       # 实际函数实现在这里
   ```