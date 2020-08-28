# -*- encoding: utf-8 -*-
# @File:   209.py    
# @Time: 2020-08-26 15:43
# @Author: ZHANG
# @Description: 209

import bisect


class Solution:
    # def minSubArrayLen(self, s: int, nums) -> int:
    #     if not nums:
    #         return 0
    #     n = len(nums)
    #     sums = [0]  # 注意这
    #     for i in range(n):
    #         sums.append(sums[-1] + nums[i])
    #
    #     res = n + 1
    #     for i in range(1, n + 1):
    #         bound = bisect.bisect_left(sums, sums[i - 1] + s)
    #         if bound != n + 1:
    #             res = min(res, bound - i + 1)
    #     return 0 if res == n + 1 else res

    def minSubArrayLen(self, s: int, nums) -> int:
        if not nums:
            return 0
        n = len(nums)
        total = 0
        left = right = 0
        res = n + 1
        while right < n:
            total += nums[right]
            while total >= s:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
            else:
                right += 1
        return 0 if res == n + 1 else res


if __name__ == "__main__":
    s = Solution()
    t = [1, 2, 3, 4, 5]
    target = 15
    print(s.minSubArrayLen(target, t))



