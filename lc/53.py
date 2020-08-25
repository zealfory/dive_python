# -*- encoding: utf-8 -*-
# @File:   53.py    
# @Time: 2020-08-24 16:32
# @Author: ZHANG
# @Description: 53


class Solution:
    def maxSubArray(self, nums):
        """贪心 O(n) O(1)"""
        n = len(nums)
        cur = max_sum = nums[0]
        for i in range(1, n):
            cur = max(cur + nums[i], nums[i])
            max_sum = max(max_sum, cur)
        return max_sum

    def maxSubArray(self, nums):
        """动态规划 O(n) O(1)"""
        n = len(nums)
        for i in range(1, n):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    s = Solution()
    print(s.maxSubArray(nums))

