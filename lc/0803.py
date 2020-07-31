# -*- encoding: utf-8 -*-
# @File:   0803.py    
# @Time: 2020-07-31 11:20
# @Author: ZHANG
# @Description: 0803


class Solution:
    """暴力法"""
    # def findMagicIndex(self, nums) -> int:
    #     for ind, v in enumerate(nums):
    #         if ind == v:
    #             return ind
    #     return -1

    """二分剪枝：二分+分治"""
    def _binFind(self, nums, start, end):
        if start > end:
            return -1
        mid = (end - start) // 2 + start
        left_ans = self._binFind(nums, start, mid - 1)
        if left_ans != -1:
            return left_ans
        elif nums[mid] == mid:
            return mid
        return self._binFind(nums, mid + 1, end)

    def findMagicIndex(self, nums) -> int:
        return self._binFind(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    nums = [0, 2, 3, 4, 5]
    s = Solution()
    print(s.findMagicIndex(nums))
