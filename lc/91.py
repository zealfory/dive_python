# -*- encoding: utf-8 -*-
# @File:   91.py    
# @Time: 2020-09-04 18:20
# @Author: ZHANG
# @Description: 91


class Solution:
    def numDecodings(self, s: str) -> int:
        # # 动态规划：时间复杂度O(n),空间复杂度O(n)
        # size = len(s)
        # # 特判
        # if size == 0:
        #     return 0
        # dp = [0] * (size + 1)
        # dp[0] = 1
        # for i in range(1, size + 1):
        #     t = int(s[i - 1])
        #     if t >= 1 and t <= 9:
        #         dp[i] += dp[i - 1]  # 最后一个数字解密成一个字母
        #     if i >= 2:  # 下面这种情况至少要有两个字符
        #         t = int(s[i - 2]) * 10 + int(s[i - 1])
        #         if t >= 10 and t <= 26:
        #             dp[i] += dp[i - 2]  # 最后两个数字解密成一个一个字母
        # return dp[-1]

        n = len(s)
        if n == 0 or s[0] == '0':
            return 0
        if n == 1:
            return 1
        nums = [0] * (n + 1)
        nums[0] = nums[1] = 1

        for i in range(2, n + 1):
            if s[i - 2] == '1' or (s[i - 2] == '2' and '0' <= s[i - 1] <= '6'):
                if s[i - 1] == '0':
                    nums[i] = nums[i - 2]
                else:
                    nums[i] = nums[i - 1] + nums[i - 2]
            elif (s[i-2] == '2' and s[i-1] > '6') or (s[i - 2] not in "12" and s[i - 1] != '0'):
                nums[i] = nums[i - 1]
            else:
                return 0
        return nums[-1]


if __name__ == "__main__":
    t = "100"
    s = Solution()
    print(s.numDecodings(t))
