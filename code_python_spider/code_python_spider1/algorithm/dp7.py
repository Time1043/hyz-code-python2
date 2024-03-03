# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/2 15:38
# @File    ：dp7.py
# @Function:

def is_ugly(n):
    """ 判断数字n是否为丑数 """
    if n <= 0:
        return False
    for i in [2, 3, 5]:
        while n % i == 0:
            n /= i
    return n == 1


def violence(n):
    """ 纯暴力求解第n个丑数 """
    count = 0  # 第几个丑数
    num = 1  # 1,2,3,... 遍历
    while count < n:
        if is_ugly(num):
            count += 1
        num += 1
    return num - 1


def nth_ugly_number1(n):
    """ 尝试策略：后面丑数是前面丑数*2*3*5，最小的and大于当前 """
    ugly_list = [1]  # 丑数列表 1,...
    for i in range(1, n):  # 一次会得到一个丑数
        # help = [x * 2 for x in ugly_list] + [x * 3 for x in ugly_list] + [x * 5 for x in ugly_list]
        factors = [2, 3, 5]
        help = [x * factor for x in ugly_list for factor in factors]
        ugly_list.append(min([x for x in help if x > ugly_list[i - 1]]))
    return ugly_list[n - 1]


def nth_ugly_number2(n):
    """ 改进尝试：定义三个指针 """
    ugly_list = [1]
    two, three, five = 0, 0, 0  # 开始都指向索引为0
    for i in range(1, n):  # 一次会得到一个丑数

        next_ugly = min(ugly_list[two] * 2, ugly_list[three] * 3, ugly_list[five] * 5)

        # if if if
        if next_ugly == ugly_list[two] * 2:
            two += 1
        if next_ugly == ugly_list[three] * 3:
            three += 1
        if next_ugly == ugly_list[five] * 5:
            five += 1

        ugly_list.append(next_ugly)

    return ugly_list[n - 1]


def nth_ugly_number3(n):
    """ 即动态规划 """
    dp = [0] * (n + 1)  # 0,,1,2,...  0不用
    dp[1] = 1
    two, three, five = 1, 1, 1  # 指针

    for i in range(2, n + 1):

        next_ugly = min(dp[two] * 2, dp[three] * 3, dp[five] * 5)
        if next_ugly == dp[two] * 2:
            two += 1
        if next_ugly == dp[three] * 3:
            three += 1
        if next_ugly == dp[five] * 5:
            five += 1

        dp[i] = next_ugly

    return dp[n]


if __name__ == '__main__':
    print('start...')

    print(violence(37))
    print(nth_ugly_number1(37))
    print(nth_ugly_number2(37))
    print(nth_ugly_number3(37))

    print('end...')
