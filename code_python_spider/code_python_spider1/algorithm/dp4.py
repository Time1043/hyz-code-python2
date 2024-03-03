# -*- coding: utf-8 -*-
# @Author  : yingzhu
# @Time    : 2024/1/31 22:19
# @File    ：dp4.py
# @Function:

durations = [1, 7, 30]
dp = [float('inf')] * 366


def min_cost_tickets1(days, costs):
    """ 暴力递归 """
    return f1(days, costs, 0)


def f1(days, costs, i):
    """ 递归含义：days[i...]的最少花费 """

    if i == len(days):  # 后续无旅行
        return 0

    ans = float('inf')
    for k in range(0, 3):  # 选谁 k是方案012
        j = i
        while j < len(days) and days[i] + durations[k] > days[j]:  # 不越界  ij
            j += 1
        ans = min(ans, costs[k] + f1(days, costs, j))
    return ans


def min_cost_tickets2(days, costs):
    """ 从顶到底的动态规划 """
    dp = [float('inf')] * len(days)
    return f2(days, costs, 0, dp)


def f2(days, costs, i, dp):
    if i == len(days):  # 后续无旅行
        return 0

    if dp[i] != float('inf'):  # 之气展开过 有记录 不算
        return dp[i]

    ans = float('inf')  # 要计算要展开
    for k in range(0, 3):  # (for枚举三个 while最多30  常数时间)
        j = i
        while j < len(days) and days[i] + durations[k] > days[j]:
            j += 1
        ans = min(ans, costs[k] + f2(days, costs, j, dp))
    dp[i] = ans  # 计算完要记录
    return ans


def min_cost_tickets3(days, costs):
    """ 从底到顶的动态规划 <- """
    n = len(days)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        for k in range(0, 3):
            j = i
            while j < len(days) and days[i] + durations[k] > days[j]:
                j += 1
            dp[i] = min(dp[i], costs[k] + dp[j])
    print(dp)
    return dp[0]


if __name__ == '__main__':
    print('start...')

    days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    costs = [2, 7, 15]
    print(min_cost_tickets1(days, costs))
    print(min_cost_tickets2(days, costs))
    print(min_cost_tickets3(days, costs))

    print('end...')
