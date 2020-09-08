# -*- encoding: utf-8 -*-
# @File:   72.py    
# @Time: 2020-08-21 10:48
# @Author: ZHANG
# @Description: 72

 
class Solution:
    def minDistance(self, word1: str, word2: str):
        m = len(word1)
        n = len(word2)
        dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        # 初始化
        for i in range(m + 1):
            dp[i][0] = i
        for i in range(n + 1):
            dp[0][i] = i
        # 状态转移
        # i , j 代表 word1, word2 对应位置的 index
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 如果word1[:i][-1]==word2[:j][-1]
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                # 否则从三种状态中选一个最小的然后 +1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]

        # m = len(word1)
        # n = len(word2)
        # dp = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        # for i in range(m + 1):
        #     dp[i][0] = i
        # for i in range(n + 1):
        #     dp[0][i] = i
        # for i in range(1, m + 1):
        #     for j in range(1, n + 1):
        #         if word1[i - 1] == word2[j - 1]:
        #             dp[i][j] = dp[i - 1][j - 1]
        #         else:
        #             dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        # return dp[-1][-1]
