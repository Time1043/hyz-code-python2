# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 18:34
# @File    ：demo7.py
# @Function:

from multiprocessing import Process
import time


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print(f'pid: {self.pid}, loopcount: {count}')


if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.start()
