# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/9 12:09
# @File    ：cal_time.py
# @Function: 计算运行时间 装饰器

import time


def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'{func.__name__} running time: {t2 - t1}')
        return result

    return wrapper
