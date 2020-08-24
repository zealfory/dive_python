# -*- encoding: utf-8 -*-
# @File:   829.py    
# @Time: 2020-08-20 14:56
# @Author: ZHANG
# @Description: 829

import math


class Solution:
    def consecutiveNumberSum(self, N):
        """枚举"""
        ans = 0
        for start in range(1, N + 1):
            target = N
            while target > 0:
                target -= start
                start += 1
            if target == 0:
                ans += 1
        return ans

    def consecutiveNumberSum(self, N):
        """简单数学"""
        # 2N = k(2x + k + 1)
        ans = 0
        for k in range(1, 2 * N + 1):
            if 2 * N % k == 0:
                y = 2 * N / k - k - 1
                if y % 2 == 0 and y >= 0:
                    ans += 1
        return ans

    def consecutiveNumberSum(self, N):  # TODO
        """进阶数学"""
        while N & 1 == 0:
            N >>= 1

        ans = 1
        d = 3
        while d * d <= N:
            e = 0
            while N % d == 0:
                N /= d
                e += 1
            ans *= e + 1
            d += 2

        if N > 1: ans *= 2
        return ans

    def consecutiveNumberSum(self, N):
        res, i = 0, 1
        while N > 0:
            res += N % i == 0
            N -= i
            i += 1

        return res
