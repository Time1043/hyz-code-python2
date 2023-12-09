# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/9 9:56
# @File    ：Recursion.py
# @Function:


# 不是递归 没有结束条件 —— 无限调用
def f1(x):
    print(x)
    f1(x - 1)


# 不是递归，到不了结束条件 —— 无限调用
def f2(x):
    if x > 0:
        print(x)
        f2(x + 1)


# 是递归 9,8,7,……
def f3(x):
    if x > 0:
        print(x)
        f3(x - 1)


# 是递归 1,2,3,……
def f4(x):
    if x > 0:
        f4((x - 1))
        print(x)


if __name__ == '__main__':
    f4(9)
