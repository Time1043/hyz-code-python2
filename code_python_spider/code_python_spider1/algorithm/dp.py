# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/31 12:08
# @File    ：dp.py
# @Function:

import numpy
import numpy as np


def demo_optimization_limitation():
    arr = [1, 2, 4, 1, 7, 8, 3]
    opt1 = rec_opt(arr, len(arr) - 1)
    opt2 = dp_opt(arr)
    print(opt1)
    print(opt2)


def rec_opt(arr, i):
    """ 用递归的形式，求解arr数组中索引为i的最优解 (递归会产生重叠子问题的计算) """
    if i == 0:  # 出口
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        # 递推方程 选or不
        choose = arr[i] + rec_opt(arr, i - 2)
        no_choose = rec_opt(arr, i - 1)
        return max(choose, no_choose)


def dp_opt(arr):
    """ 用动态规划的形式，求解arr数组 """
    opt = np.zeros(len(arr))
    opt[0], opt[1] = arr[0], max(arr[0], arr[1])
    for i in range(2, len(arr)):
        choose = arr[i] + opt[i - 2]
        no_choose = opt[i - 1]
        opt[i] = max(choose, no_choose)
    return opt[len(arr) - 1]


if __name__ == '__main__':
    print('start...')

    demo_optimization_limitation()

    print('end...')
