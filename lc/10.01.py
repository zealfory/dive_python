# -*- encoding: utf-8 -*-
# @File:   10.01.py    
# @Time: 2021/7/24 1:11 上午
# @Author: ZHANG
# @Description: 10.01
from typing import List


class Solution:
    @staticmethod
    def merge(A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        p, q = m - 1, n - 1
        k = m + n - 1
        while B:
            if B[q] >= A[p]:
                A[k] = B.pop()
                q -= 1
                k -= 1
            else:
                A[k] = A[p]
                p -= 1
                k -= 1

A = [2,0]
m = 1
B = [1]
n = 1
print(Solution.merge(A, m, B, n))