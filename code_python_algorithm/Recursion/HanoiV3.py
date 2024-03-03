# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2023/12/9 10:58
# @File    ：HanoiV3.py
# @Function: 进度条

def hanoi(n, source, auxiliary, target, current_step, total_steps):
    if n == 0:
        return current_step

    if n > 0:
        current_step = hanoi(n - 1, source, target, auxiliary, current_step, total_steps)
        current_step += 1
        print_progress_bar(current_step, total_steps)
        print(f'moving from {source} to {target}')
        current_step = hanoi(n - 1, auxiliary, source, target, current_step, total_steps)

    return current_step


def print_progress_bar(current_step, total_steps):
    percent = (current_step / total_steps) * 100
    bar = '=' * int(percent / 2) + ' ' * (50 - int(percent / 2))
    print(f"\rProgress: [{bar}] {percent:.2f}%  ", end='')


if __name__ == '__main__':
    num = 20
    total_steps = 2 ** num - 1
    hanoi(num, 'a', 'b', 'c', 0, total_steps)
    print(f'total_steps: {total_steps}')
