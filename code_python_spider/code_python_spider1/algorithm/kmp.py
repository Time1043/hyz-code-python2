# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/30 13:54
# @File    ：kmp.py
# @Function:


import string
import random
import time
import tqdm

time_violence = []
time_solution = []


def display_time_violence(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        # print('violence Time: {:.4} s'.format(t2 - t1))
        time_violence.append(round(t2 - t1, 4))
        return result

    return wrapper


def display_time_solution(func):
    def wrapper(*args):
        t1 = time.time()
        result = func(*args)
        t2 = time.time()
        # print('solution Time: {:.4} s'.format(t2 - t1))
        time_solution.append(round(t2 - t1, 4))
        return result

    return wrapper


def demo():
    str1 = 'aabaabcaabaaba'
    str2 = 'bca'

    print('violence...')
    result_violence = violence(str1, str2)
    print(result_violence)

    str2_next = get_next_array(str2, len(str2))
    print(str2_next)
    result = kmp(str1, str2)
    print(result)


def generate_two_str(max_len):
    """ 指定最大长度 max_len，生成两个字符串，且len(str1)>len(str2) """
    num1, num2 = int(random.random() * max_len + 1), int(random.random() * max_len + 1)
    str1_len, str2_len = max(num1, num2), min(num1, num2)

    chars = string.ascii_letters + string.digits  # 定义字符集
    str1 = ''.join(random.choice(chars) for _ in range(str1_len))
    str2 = ''.join(random.choice(chars) for _ in range(str2_len))
    return str1, str2


@display_time_violence
def violence(str1, str2):
    n1, n2 = len(str1), len(str2)

    if n1 < n2:
        return -1

    for i in range(n1):
        for j in range(n2):
            if (i + j) < n1:  # 边界
                if str1[i + j] != str2[j]:  # 一旦发现不匹配 终止内层循环
                    break
                if j == n2 - 1:  # 和str2的最后一个字符都匹配上 即成功
                    return i

    return -1


def get_next_array(str, str_len):
    if str_len == 1:
        return [-1]

    next_array = [-1] * str_len
    # 首项：-1,0,...
    next_array[0], next_array[1] = -1, 0
    # 递推：f(n-1) -> f(n)
    cur = 2
    back = next_array[cur - 1]
    while cur < str_len:
        if str[cur - 1] == str[back]:  # 情况1：不用跳 得数  (next_array[cur++] = ++back)
            back += 1
            next_array[cur] = back
            cur += 1
        elif back > 0:  # 情况2：回跳
            back = next_array[back]
        else:  # 情况3：跳到头 得数  (next_array[cur++] = 0)
            next_array[cur] = 0
            cur += 1

    return next_array


@display_time_solution
def kmp(str1, str2):
    n1, n2 = len(str1), len(str2)
    x, y = 0, 0  # 游标
    next_array = get_next_array(str2, n2)

    while x < n1 and y < n2:  # 结束条件 (str2到了n2即出结果了 str1到了n1即没材料了)
        if str1[x] == str2[y]:  # 情况1：能够对上 就向前推进
            x += 1
            y += 1
        elif y == 0:  # 情况2：跳到str2的0 str1拉新的
            x += 1
        else:  # 情况3：next匹配过程 回跳
            y = next_array[y]

    return (x - y) if (y == n2) else -1  # (str2到了n2即出结果了 str1到了n1即没材料了)


if __name__ == '__main__':
    print('start...')

    time_run = 1000
    max_len = 50000
    for i in tqdm.tqdm(range(time_run), desc='Processing'):
        str1, str2 = generate_two_str(max_len)
        result_violence = violence(str1, str2)
        result = kmp(str1, str2)
        if result_violence != result:
            print(f'[error]  example{i}: {str1}, {str2} \n  result: {result_violence}, {result}')
    print('[success]  congratulations!!! ')

    # print(time_violence)
    # print(time_solution)
    print(sum(time_violence))
    print(sum(time_solution))

    print('end...')
