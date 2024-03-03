# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/9 9:11
# @File    ：Complexity.py
# @Function: 时间复杂度、空间复杂度


from timeit import timeit


# O(1)
def f1():
    print('Hello World')


# O(N)
def f2(n):
    for i in range(n):
        print('Hello World')


# O(N^2)
def f3(n):
    for i in range(n):
        for j in range(n):
            print('Hello World')


# O(N^3)
def f4(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print('Hello World')


# O(logN)
def f5(n):
    while n > 1:
        print(n)
        n = n // 2  # 整除2


def testTime(n, function):
    """ 数据规模n、函数function """
    function_time = timeit(lambda: function(n), number=100000)
    print(f'{function.__name__}  执行时间：{function_time} 秒')


if __name__ == '__main__':
    f5(10)
