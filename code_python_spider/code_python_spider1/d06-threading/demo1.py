# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 16:12
# @File    ：demo1.py
# @Function: 主线程先结束了

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
print(f'main：threading {threading.current_thread().name} is ended')

'''
main：threading MainThread is running
方法：threading Thread-1 is running
方法：threading Thread-1 sleep 1s
方法：threading Thread-2 is running
方法：threading Thread-2 sleep 5s
main：threading MainThread is ended
方法：threading Thread-1 is ended
方法：threading Thread-2 is ended
'''
