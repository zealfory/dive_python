# -*- encoding: utf-8 -*-
# @File:   1143.py    
# @Time: 2020-09-02 16:06
# @Author: ZHANG
# @Description: 1143


class Solution:
    def longestCommonSubsequence(self, text1, text2) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]

    # def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    #     t1 = len(text1)
    #     t2 = len(text2)
    #     dp = [[0] * t2] * t1
    #
    #     for i in range(0, t1):
    #         for j in range(0, t2):
    #             if i == j == 0:
    #                 if text1[0] == text2[0]:
    #                     dp[0][0] = 1
    #             elif i == 0 or j == 0:
    #                 dp[i][j] = dp[0][0]
    #             else:
    #                 if text1[i] == text2[j]:
    #                     dp[i][j] = dp[i - 1][j - 1] + 1
    #                 else:
    #                     dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    #     return dp[-1][-1]


if __name__ == "__main__":
    text1 = "abcbu"
    text2 = "abcbcbx"
    s = Solution()
    print(s.longestCommonSubsequence(text1, text2))


