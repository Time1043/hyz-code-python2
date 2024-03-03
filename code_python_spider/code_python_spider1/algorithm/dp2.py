# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/31 19:58
# @File    ：dp2.py
# @Function:

import numpy as np


def rec_subset(arr, i, s):
    """ 用递归实现 """
    if s == 0:  # 得数
        return True
    elif i == 0:  # 到数组的最后一个元素
        return arr[0] == s
    elif arr[i] > s:  # 数组中当前元素过大
        return rec_subset(arr, i - 1, s)
    else:  # 递归
        choose = rec_subset(arr, i - 1, s - arr[i])
        no_choose = rec_subset(arr, i - 1, s)
        return choose or no_choose


def dp_subset(arr, s):
    subset = np.zeros((len(arr), s + 1), dtype=bool)
    subset[:, 0] = True
    subset[0, :] = False
    subset[0, arr[0]] = True
    for i in range(1, len(arr)):
        for j in range(1, s + 1):
            if arr[i] > s:  # 数组当前元素过大 只考虑右支
                subset[i, j] = subset[i - 1, j]
            else:  # 选还是不选
                choose = subset[i - 1, j - arr[i]]
                no_choose = subset[i - 1, j]
                subset[i, j] = choose or no_choose
    r, c = subset.shape
    return subset[r - 1, c - 1]


if __name__ == '__main__':
    print('start...')

    arr = [3, 34, 4, 12, 5, 2]
    s = 9
    print(rec_subset(arr, len(arr) - 1, s))
    print(dp_subset(arr, s))

    print('end...')
