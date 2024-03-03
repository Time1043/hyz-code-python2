# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/2/2 17:02
# @File    ：dp8.py
# @Function:


def longest_valid_parentheses1(s):
    """ 尝试策略：f(...i)有效的最大得数，前面的值推后面 """
    dp = [0] * len(s)

    for i in range(len(s)):
        if s[i] == '(':  # ...(
            dp[i] = 0
        else:  # 借助前面已求的值  ...)
            cur = i - dp[i - 1] - 1  # 跳 前面信息
            if cur >= 0:  # 特例：')(' python -1
                if s[cur] == ')':  # ...)()()) 与尾不配对
                    dp[i] = 0
                else:  # ...(()())  【嵌套：前面信息】 与尾配对
                    res = dp[i - 1] + 2
                    cur = cur - 1
                    if dp[cur] != 0:  # ...()()(()())  【并列：前面信息】
                        res += dp[cur]
                    dp[i] = res
            else:
                dp[i] = 0

    print(dp)
    return max(dp)


def longest_valid_parentheses2(s):
    """ 精简代码 """
    dp = [0] * len(s)
    ans = 0

    for i in range(len(s)):
        if s[i] == ')':  # ...)
            if s[i - 1] == '(':  # ...()()  【并列：与尾配对】 前面信息
                dp[i] = dp[i - 2] + 2
            elif i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':  # ...()()(()()) 【嵌套：与尾配对】 前面信息
                dp[i] = dp[i - 1] + 2 + (dp[i - dp[i - 1] - 2] if (i - dp[i - 1] >= 2) else 0)  # 可能的并列 并列是尽头
            ans = max(ans, dp[i])

    print(dp)
    return ans


def longest_valid_parentheses3(s):
    """ 精简代码 """
    dp = [0] * len(s)
    ans = 0

    for i in range(len(s)):
        if s[i] == ')':  # ...)
            pre = i - dp[i - 1] - 1
            if pre >= 0 and s[pre] == '(':
                dp[i] = dp[i - 1] + 2 + (dp[pre - 1] if pre > 0 else 0)
            ans = max(ans, dp[i])

    print(dp)
    return ans


if __name__ == '__main__':
    print('start...')

    s = '(()())())()()()(())'
    print(longest_valid_parentheses1(s))
    print(longest_valid_parentheses2(s))
    print(longest_valid_parentheses3(s))

    print('end...')
