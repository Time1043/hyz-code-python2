# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/22 11:39
# @File    ：demo4_decorator.py
# @Function:

import time


def is_prime(num):
    """ 判断num是否质数 """
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


def prime_nums():
    """ 打印2到1w的所有质数 """
    t1 = time.time()  # 辅助代码 计时

    # 逻辑代码
    for i in range(2, 10000):
        if is_prime(i):
            print(i)

    t2 = time.time()  # 辅助代码 计时
    print(t2 - t1)


def display_time2(func):  # 装饰器函数  func为逻辑函数
    def wrapper():
        t1 = time.time()
        func()  # 逻辑函数
        t2 = time.time()
        print(t2 - t1)

    return wrapper


@display_time2
def prime_nums2():
    """ 打印2到1w的所有质数，只写逻辑代码，辅助代码交给装饰器 """
    for i in range(2, 10000):
        if is_prime(i):
            print(i)


def display_time3(func):  # 装饰器函数  func为逻辑函数
    def wrapper(*args):
        t1 = time.time()
        result = func()  # 逻辑函数有返回值
        t2 = time.time()
        print('Tocal Time: {:.4} s'.format(t2 - t1))
        return result  # 逻辑函数的返回值

    return wrapper


@display_time3
def count_prime_num3(max_num):
    """ 逻辑函数有返回值、有传入参数 """
    count = 0
    for i in range(2, max_num):
        if is_prime(i):
            count += 1
    return count


if __name__ == '__main__':
    # prime_nums()
    # prime_nums2()
    count = count_prime_num3(100)
    print(count)
