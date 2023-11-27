# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 18:25
# @File    ：demo6-multiprocessing.py
# @Function:

import multiprocessing


def process(index):
    print(f'方法：Process:{index}')


if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,))
        p.start()

        print(multiprocessing.cpu_count())  # 获取当前机器的cpu核数
        print(multiprocessing.active_children())  # 获取当前还在运行的所有进程
