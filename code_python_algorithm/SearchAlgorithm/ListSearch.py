# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/9 11:15
# @File    ：ListSearch.py
# @Function: 列表查找

from cal_time import *


@cal_time
def linear_search(li, val):
    """
    线性查找 —— O(N)
    :param li: 要查找的列表
    :param val: 要查找的元素
    :return: 要查找元素在指定列表的索引
    """
    return next((index for index, value in enumerate(li) if value == val), -1)
    # for index, value in enumerate(arr):
    #     if value == val:
    #         return index
    # return -1


def binary_search(li, left, right, val):
    """
    已排序列表的二分查找 —— O(logN)
    :param li: 要查找的列表
    :param left: 指针left，标记列表有效区域
    :param right: 指针right，标记列表有效区域
    :param val: 要查找的元素
    :return: 要查找元素在指定列表的索引
    """
    # 边界处理
    if right >= left:
        mid = (left + right) // 2

        if li[mid] == val:  # 恰好找到
            return mid
        elif li[mid] > val:  # 大了 往小往左
            return binary_search(li, left, mid - 1, val)  # 递归调用
        else:  # 小了 往大往右
            return binary_search(li, mid + 1, right, val)  # 递归调用

    else:
        return -1


@cal_time
def binary_search2(li, val):
    """
    已排序列表的二分查找 —— O(logN)
    :param li: 要查找的列表
    :param val: 要查找的元素
    :return: 要查找元素在指定列表的索引
    """
    # 两个指针 初始化
    left = 0
    right = len(li) - 1

    # 边界情况 结束条件
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid  # 恰好找到
        elif li[mid] > val:
            right = mid - 1  # 大了 往小往左
        else:
            left = mid + 1  # 小了 往大往右
    else:
        return -1


if __name__ == '__main__':
    # li = [1, 2, 3, 6, 9, 13, 24, 42, 53, 55, 112]
    #
    # # python内置查找函数-----------------------------------
    # try:
    #     index = li.index(515)
    # except ValueError:
    #     index = -1
    # print(index)
    #
    # # python内置查找函数-----------------------------------
    # val = 513
    # index = li.index(val) if val in li else -1
    # print(index)
    #
    # # 自己实现的线性查找-----------------------------------
    # print(linear_search(li, 112))
    #
    # # 自己实现的二分查找-----------------------------------
    # print(binary_search(li, 0, len(li) - 1, 2))
    # print(binary_search2(li, 123))

    # 实际测试-----------------------------------
    li = list(range(1000000000))
    binary_search2(li, 100000001)  # 0.07150983810424805
    linear_search(li, 100000001)  # 19.26067090034485
