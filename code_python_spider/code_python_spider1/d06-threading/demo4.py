# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/10/30 17:22
# @File    ：demo4.py
# @Function: 明显小于1000

import threading
import time

count = 0


class MyTread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        global count
        temp = count + 1
        time.sleep(0.001)
        count = temp


threads = []
for _ in range(1000):
    thread = MyTread()
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print(f'最终得数：{count}')  # 最终得数：5
