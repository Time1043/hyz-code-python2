# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 17:12
# @File    ：demo2.py
# @Function: 主线程等待子线程

import threading  # 多进程多线程
import time


def target(second):
    print(f'方法：threading {threading.current_thread().name} is running')
    print(f'方法：threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'方法：threading {threading.current_thread().name} is ended')


print(f'main：threading {threading.current_thread().name} is running')
for i in [1, 5]:
    t = threading.Thread(target=target, args=[i])
    t.start()
    t.join()
print(f'main：threading {threading.current_thread().name} is ended')

'''
main：threading MainThread is running
方法：threading Thread-1 is running
方法：threading Thread-1 sleep 1s
方法：threading Thread-1 is ended
方法：threading Thread-2 is running
方法：threading Thread-2 sleep 5s
方法：threading Thread-2 is ended
main：threading MainThread is ended
'''
