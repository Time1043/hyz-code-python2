# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/10 15:54
# @File    ：demo11_thread2.py
# @Function: 线程池

import time
from concurrent.futures import ThreadPoolExecutor


def func_task(name, t):  # 传参
    """ 任务函数 """
    time.sleep(t)
    print("task: " + name)
    return name  # 有返回值


def fn(res):  # 拿到返回值
    print("return: " + res.result())


if __name__ == '__main__':
    print('start...')

    with ThreadPoolExecutor(10) as t:
        """
        # 返回的顺序是不确定的
        t.submit(func_task, "zhou", 5).add_done_callback(fn)  # 任务完成后回调
        t.submit(func_task, "wang", 1).add_done_callback(fn)  # 返回立即执行
        t.submit(func_task, "li", 6).add_done_callback(fn)
        t.submit(func_task, "lin", 2).add_done_callback(fn)
        """

        # 保证返回顺序 与 任务分发顺序 一致
        result = t.map(func_task, ["zhou", "wang", "li", "lin"], [5, 1, 6, 2])  # 生成器
        for i in result:
            print(i)

    print('end...')
