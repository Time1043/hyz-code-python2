# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/3/10 15:34
# @File    ：demo11_thread1.py
# @Function: 单线程 多线程

from threading import Thread


def func_task(name):  # 传参
    """ 任务函数 """
    for i in range(10):
        print(name, i)


class MyThread(Thread):  # 自定义类继承Thread
    def __init__(self, name):  # 传参
        super(MyThread, self).__init__()
        self.name = name

    def run(self):  # 重写run方法
        func_task(self.name)


if __name__ == '__main__':
    print('start...')

    """
    # 单线程
    func_task("zhou")
    func_task("wang")
    func_task("li")
    """

    """
    # 多线程方式1 (创建线程 指定任务 启动线程)
    t1 = Thread(target=func_task, args=("zhou",))
    t2 = Thread(target=func_task, args=("wang",))
    t3 = Thread(target=func_task, args=("li",))
    t1.start()
    t2.start()
    t3.start()
    """

    # 多线程方式2
    t1 = MyThread("zhou")
    t2 = MyThread("wang")
    t3 = MyThread("li")
    t1.start()
    t2.start()
    t3.start()

    print('end...')  # 主线程比t3早结束
