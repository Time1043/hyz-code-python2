def num_decodings3(s):
    """ 自底到顶动态规划 """
    MOD = 10 ** 9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1

    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            dp[i] = 0
        else:
            # 单个字符的解码
            dp[i] = dp[i + 1] * (9 if s[i] == '*' else 1)
            # 两个字符的组合解码
            if i + 1 < n:
                # 当两个连续字符都不是 '*' 且可以形成有效编码时
                if s[i] != '*' and s[i + 1] != '*' and 10 <= int(s[i:i + 2]) <= 26:
                    dp[i] += dp[i + 2]
                # 当第一个字符不是 '*' 且第二个字符是 '*'
                elif s[i] != '*' and s[i + 1] == '*':
                    multipliers = {'1': 9, '2': 6}
                    dp[i] += dp[i + 2] * (multipliers[s[i]] if s[i] in multipliers else 0)
                # 当第一个字符是 '*' 且第二个字符不是 '*'
                elif s[i] == '*' and s[i + 1] != '*':
                    dp[i] += dp[i + 2] * (2 if s[i + 1] in '123456' else 1)
                # 当两个连续字符都是 '*'
                elif s[i] == '*' and s[i + 1] == '*':
                    dp[i] += 15 * dp[i + 2]

    return dp[0] % MOD

# 再次测试修改后的代码
test_string = '904'
print(num_decodings3(test_string))
