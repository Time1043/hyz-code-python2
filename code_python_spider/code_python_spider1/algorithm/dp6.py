# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/1 22:25
# @File    ：dp6.py
# @Function:

import random

MOD = 10 ** 9 + 7


def demo():
    s = '*'
    print(num_decodings1(s))
    print(num_decodings2(s))
    print(num_decodings3(s))
    print(num_decodings4(s))


def generate_str(max_len):
    """ 指定最大长度 max_len，生成一个字符串的编码 —— 由数字和*组成的字符串 """
    num = int(random.random() * max_len + 1)
    characters = '0123456789*'
    return ''.join(random.choice(characters) for _ in range(num))


def num_decodings1(s):
    """ 暴力递归 """
    return f1(s, 0)


"""
def f1(s, i):
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0

    # [i]
    if (s[i] == '*'):
        ans = 9 * f1(s, i + 1)
    else:
        ans = f1(s, i + 1)

    # [i][i+1]  检查[i+1]是否越界
    if i + 1 < len(s):
        # [][]
        if (s[i] != '*' and s[i + 1] != '*') and (10 <= int(s[i:i + 2]) <= 26):
            ans += f1(s, i + 2)
        # [][*]
        elif s[i] != '*' and s[i + 1] == '*':
            if s[i] == '1':
                ans += 9 * f1(s, i + 2)  # 11,12,...19
            elif s[i] == '2':
                ans += 6 * f1(s, i + 2)  # 21,22,...26
        # [*][]
        elif s[i] == '*' and s[i + 1] != '*':
            if s[i + 1] == '0':
                ans += 2 * f1(s, i + 2)
            elif s[i + 1] in '123456':
                ans += 2 * f1(s, i + 2)  # *为 1,2
            else:
                ans += f1(s, i + 2)  # *为 1
        # [*][*]
        elif s[i] == '*' and s[i + 1] == '*':
            ans += 15 * f1(s, i + 2)  # 11,..19,21,...26

    return ans % MOD
"""


def f1(s, i):
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0

    # [i]
    ans = f1(s, i + 1) * (9 if (s[i] == '*') else 1)

    # [i][i+1]  检查[i+1]是否越界
    if i + 1 < len(s):
        # [][]  (排除 04 40 )
        if (s[i] != '*' and s[i + 1] != '*') and (10 <= int(s[i:i + 2]) <= 26):
            ans += f1(s, i + 2)
        # [][*]
        elif s[i] != '*' and s[i + 1] == '*':
            multipliers = {'1': 9, '2': 6}  # 11,12,...19  # 21,22,...26
            ans += f1(s, i + 2) * (multipliers[s[i]] if (s[i] in multipliers) else 0)
        # [*][]
        elif s[i] == '*' and s[i + 1] != '*':
            ans += f1(s, i + 2) * (2 if s[i + 1] in '0123456' else 1)  # *为 1,2  # *为 1
        # [*][*]
        elif s[i] == '*' and s[i + 1] == '*':
            ans += 15 * f1(s, i + 2)  # 11,..19,21,...26

    return ans % MOD


def num_decodings2(s):
    """ 自顶到底动态规划 """
    dp = [-1] * len(s)
    return f2(s, 0, dp)


def f2(s, i, dp):
    if i == len(s):
        return 1
    if s[i] == '0':
        return 0

    if dp[i] != -1:  # 有记录 不计算
        return dp[i]

    # [i]
    ans = f2(s, i + 1, dp) * (9 if (s[i] == '*') else 1)

    # [i][i+1]  检查[i+1]是否越界
    if i + 1 < len(s):
        # [][]  (排除 04 40 )
        if (s[i] != '*' and s[i + 1] != '*') and (10 <= int(s[i:i + 2]) <= 26):
            ans += f2(s, i + 2, dp)
        # [][*]
        elif s[i] != '*' and s[i + 1] == '*':
            multipliers = {'1': 9, '2': 6}  # 11,12,...19  # 21,22,...26
            ans += f2(s, i + 2, dp) * (multipliers[s[i]] if (s[i] in multipliers) else 0)
        # [*][]
        elif s[i] == '*' and s[i + 1] != '*':
            ans += f2(s, i + 2, dp) * (2 if s[i + 1] in '0123456' else 1)  # *为 1,2  # *为 1
        # [*][*]
        elif s[i] == '*' and s[i + 1] == '*':
            ans += 15 * f2(s, i + 2, dp)  # 11,..19,21,...26

    ans %= MOD
    dp[i] = ans  # 计算完要记录

    return ans


def num_decodings3(s):
    """ 自底到顶动态规划 """
    dp = [-1] * (len(s) + 1)
    dp[len(s)] = 1

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            # [i]
            dp[i] = dp[i + 1] * (9 if (s[i] == '*') else 1)

            # [i][i+1]  检查[i+1]是否越界
            if i + 1 < len(s):
                # [][]  (排除 04 40 )
                if (s[i] != '*' and s[i + 1] != '*') and (10 <= int(s[i:i + 2]) <= 26):
                    dp[i] += dp[i + 2]
                # [][*]
                elif s[i] != '*' and s[i + 1] == '*':
                    multipliers = {'1': 9, '2': 6}
                    dp[i] += dp[i + 2] * (multipliers[s[i]] if (s[i] in multipliers) else 0)
                # [*][]
                elif s[i] == '*' and s[i + 1] != '*':
                    dp[i] += dp[i + 2] * (2 if s[i + 1] in '0123456' else 1)
                # [*][*]
                elif s[i] == '*' and s[i + 1] == '*':
                    dp[i] += 15 * dp[i + 2]

    return dp[0] % MOD


def num_decodings4(s):
    """ 优化空间：三个变量的滑动窗口 """
    nt, nt_nt = 1, 0  # dp[n+1]=0 不存在的

    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            cur = 0
        else:
            # [i]
            cur = nt * (9 if (s[i] == '*') else 1)

            # [i][i+1]  检查[i+1]是否越界
            if i + 1 < len(s):
                # [][]  (排除 04 40 )
                if (s[i] != '*' and s[i + 1] != '*') and (10 <= int(s[i:i + 2]) <= 26):
                    cur += nt_nt
                # [][*]
                elif s[i] != '*' and s[i + 1] == '*':
                    multipliers = {'1': 9, '2': 6}
                    cur += nt_nt * (multipliers[s[i]] if (s[i] in multipliers) else 0)
                # [*][]
                elif s[i] == '*' and s[i + 1] != '*':
                    cur += nt_nt * (2 if s[i + 1] in '0123456' else 1)
                # [*][*]
                elif s[i] == '*' and s[i + 1] == '*':
                    cur += nt_nt * 15

        nt_nt, nt = nt, cur

    return nt % MOD


if __name__ == '__main__':
    print('start...')

    test_time = 1000
    max_len = 50
    for i in range(test_time):
        s = generate_str(max_len)
        result1 = num_decodings1(s)
        result2 = num_decodings2(s)
        result3 = num_decodings3(s)
        result4 = num_decodings4(s)
        if (not (result1 == result2) and (result2 == result3) and (result3 == result4)):
            print(f'[error]  example: {s} \n  result: {result1}, {result2}, {result3}, {result4}')
    print('[success]  congratulations!!! ')

    print('end...')
