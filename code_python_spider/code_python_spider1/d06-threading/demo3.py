# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 17:18
# @File    ：demo3.py
# @Function: 守护线程

import threading  # 多进程多线程
import time


def target(second):
    print(f'方法：threading {threading.current_thread().name} is running')
    print(f'方法：threading {threading.current_thread().name} sleep {second}s')
    time.sleep(second)
    print(f'方法：threading {threading.current_thread().name} is ended')


print(f'main：threading {threading.current_thread().name} is running')
t1 = threading.Thread(target=target, args=[2])
t1.start()
t2 = threading.Thread(target=target, args=[5])
t2.setDaemon(True)  # 设为守护线程 不跟随到最后
t2.start()
print(f'main：threading {threading.current_thread().name} is ended')

'''
main：threading MainThread is running
方法：threading Thread-1 is running
方法：threading Thread-1 sleep 2s
方法：threading Thread-2 is running
方法：threading Thread-2 sleep 5s
main：threading MainThread is ended
方法：threading Thread-1 is ended
'''