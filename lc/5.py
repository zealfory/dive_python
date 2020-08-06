# -*- encoding: utf-8 -*-
# @File:   5.py    
# @Time: 2020-08-06 15:41
# @Author: ZHANG
# @Description: 5


# TODO
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len == 0:
            return ""
        if s_len == 1:
            return s
        dp = [[0] * (s_len + 1)] * (s_len + 1)
        longest = 1
        start = 0
        for i in range(s_len):
            dp[i][i] = 1
            if i < s_len - 1:
                if s[i] == s[i + 1]:
                    dp[i][i + 1] = 1
                    start = i
                    longest = 2

        for l in range(3, s_len + 1):
            for i in range(s_len + 1 - l):
                j = l + i - 1
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    start = i
                    longest = l

        return s[start:start + longest]
