# -*- encoding: utf-8 -*-
# @File:   343.py    
# @Time: 2020-07-31 10:25
# @Author: ZHANG
# @Description: 343


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 0
        for i in range(2, n+1):
            for j in range(i):
                dp[i] = max(j * (i - j), j * dp[i - j], dp[i])
        return dp[n]
