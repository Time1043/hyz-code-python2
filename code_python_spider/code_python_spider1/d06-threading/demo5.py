# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 18:07
# @File    ：demo5.py
# @Function: 加锁保护

import threading
import time

count = 0


class MyTread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        lock.acquire()
        temp = count + 1
        time.sleep(0.001)
        count = temp
        lock.release()


lock = threading.Lock()
threads = []
for _ in range(1000):
    thread = MyTread()
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(f'最终得数：{count}')  # 最终得数：1000
