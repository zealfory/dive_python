# -*- encoding: utf-8 -*-
# @File:   70.py    
# @Time: 2020-07-23 15:59
# @Author: ZHANG
# @Description: 70[动态规划]

 
class Solution:
    def climbStairs(self, n: int) -> int:
        # dp = [0 for _ in range(n+1)]
        # dp[0] = 1
        # dp[1] = 1
        # for i in range(2, n+1):
        #     dp[i] = dp[i - 1] + dp[i - 2]
        # return dp[-1]

        # 递归
        # if n == 0:
        #     return 1
        # elif n == 1:
        #     return 1
        # else:
        #     return self.climbStairs(n-1) + self.climbStairs(n-2)
        #

        # 无递归
        if n == 1:
            return 1
        p, q = 1, 1
        for i in range(1, n):
            p, q = q, p + q
        return q


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))
