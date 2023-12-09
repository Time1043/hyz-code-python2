# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/9 10:25
# @File    ：HanoiV2.py
# @Function: 返回所走步骤数

def hanoi(n, source, auxiliary, target):
    """
    n个盘子，从a经过b来到c
    :param n: n个盘子
    :param source: 柱子a，源
    :param auxiliary: 柱子b，辅助
    :param target: 柱子c，目标
    :return: 所需的步骤数step
    """

    if n == 0:
        return 0

    # 递归终止条件：n=0
    if n > 0:
        # n-1个盘子，从a经过c来到b —— 递归(相同模式、输入规模更小的)
        step = hanoi(n - 1, source, target, auxiliary)
        # 把第n个盘子，从a移动到c —— 移动一个
        print(f'moving from {source} to {target}')
        step += 1
        # n-1个盘子，从b经过a来到c —— 递归(相同模式、输入规模更小的)
        step += hanoi(n - 1, auxiliary, source, target)

    return step


if __name__ == '__main__':
    print(hanoi(64, 'a', 'b', 'c'))
