# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/31 20:46
# @File    ：dp3.py
# @Function:


import numpy as np


def fib1(n):
    """ 暴力递归，硬展开 """
    return f1(n)


def f1(i):
    if i == 0:  # 废掉
        return 0
    if i == 1:  # 规定
        return 1
    return f1(i - 1) + f1(i - 2)


def fib2(n):
    """ 从顶到底的动态规划，算出结果记录 (复杂的展开) """
    dp = [-1] * (n + 1)
    return f2(n, dp)


def f2(i, dp):
    if i == 0:
        return 0
    if i == 1:
        return 1
    if dp[i] != -1:  # 有记载的不计算
        return dp[i]
    ans = f2(i - 1, dp) + f2(i - 2, dp)  # 计算
    dp[i] = ans  # 记载
    return ans


def fib3(n):
    """ 从底到顶的动态规划，算出结果记录 (先算简单的) """
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


def fib4(n):
    """ 优化空间：三个变量的滑动窗口 """
    if n == 0:
        return 0
    if n == 1:
        return 1
    last_last, last = 0, 1
    for i in range(2, n + 1):
        cur = last_last + last
        last_last, last = last, cur
    return last


def fib5(n):
    """ 用矩阵快速幂求解，达到O(logN) """
    if n == 0:
        return 0
    matrix = np.array([[1, 1], [1, 0]])
    result = matrix_power(matrix, n - 1)
    return result[0, 0]


def matrix_power(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        half_power = matrix_power(matrix, n // 2)
        return np.dot(half_power, half_power)
    else:
        half_power = matrix_power(matrix, (n - 1) // 2)
        return np.dot(np.dot(half_power, half_power), matrix)


if __name__ == '__main__':
    print('start...')

    print(fib1(8))
    print(fib2(8))
    print(fib3(8))
    print(fib4(8))
    print(fib5(8))

    print('end...')
