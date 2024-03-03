# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/1 11:21
# @File    ：dp5.py
# @Function:


def num_decodings1(s):
    """ 暴力递归 """
    return f1(s, 0)


def f1(s, i):
    """ 递归含义：s[i...]有多少种有效转化方案 """

    if i == len(s):  # 【越界】 能到最后 即是有效决策 rt1
        return 1

    if s[i] == '0':  # 【还没越界】 0开头不行 即是无效决策 rt0
        ans = 0
    else:  # 【还没越界 也不是0】 str[i]能够转化
        ans = f1(s, i + 1)
        if i + 1 < len(s) and int(s[i:i + 2]) <= 26:  # 越界 限制26
            ans += f1(s, i + 2)
    return ans


def num_decodings2(s):
    """ 自顶到底动态规划 """
    dp = [-1] * len(s)
    return f2(s, 0, dp)


def f2(s, i, dp):
    if i == len(s):
        return 1

    if dp[i] != -1:  # 有记录 不计算
        return dp[i]
    if s[i] == '0':
        ans = 0
    else:
        ans = f2(s, i + 1, dp)
        if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
            ans += f2(s, i + 2, dp)
    dp[i] = ans  # 当次算完要记录
    return ans


def num_decodings3(s):
    """ 严格位置依赖的动态规划 """
    n = len(s)
    dp = [-1] * (n + 1)
    dp[n] = 1
    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                dp[i] += dp[i + 2]
    return dp[0]


def num_decodings4(s):
    """ 优化空间：三个变量的滑动窗口 """
    nt_nt, nt = 0, 1  # dp[n+1]=0 不存在的
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            cur = 0
        else:
            cur = nt
            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                cur += nt_nt
        nt_nt, nt = nt, cur  # 迭代
    return nt


if __name__ == '__main__':
    print('start...')

    s = '11106'
    print(num_decodings1(s))
    print(num_decodings2(s))
    print(num_decodings3(s))
    print(num_decodings4(s))

    print('end...')
