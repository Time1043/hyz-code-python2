# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/11/27 18:40
# @File    ：006efficiency1.py
# @Function:

from timeit import timeit


# 5行代码
def some_function(n):
    for i in range(2):
        n += 100
    return n


# 103行代码
def other_function(n):
    for i in range(100):
        n += 2
    return n


# 实验1：执行10w次
some_function_time = timeit('some_function(0)', globals=globals(), number=100000)
other_function_time = timeit('other_function(0)', globals=globals(), number=100000)
print(f'some_function 执行时间：{some_function_time} 秒')  # 0.020889700000000122
print(f'other_function 执行时间：{other_function_time} 秒')  # 0.18587670000000012

# 实验2
some_function_time1 = timeit('some_function(1)', globals=globals(), number=100000)
some_function_time2 = timeit('some_function(1000000)', globals=globals(), number=100000)
print(f'some_function1 执行时间：{some_function_time1} 秒')  # 0.01980019999999999
print(f'some_function2 执行时间：{some_function_time2} 秒')  # 0.021805500000000033
