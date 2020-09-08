# -*- encoding: utf-8 -*-
# @File:   34.py    
# @Time: 2020-07-22 13:55
# @Author: ZHANG
# @Description: 34[二分法]


class Solution:
    def searchRange(self, nums, target):
        left = self._bin_search_left(nums, target)
        right = self._bin_search_right(nums, target)
        if left < len(nums) and right >= 0 and (nums[left] == nums[right] == target):
            return [left, right]
        return [-1, -1]

    def _bin_search_left(self, nums, target):
        low = 0
        high = len(nums)

        while low < high:
            mid = low + ((high - low) >> 1)
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        return low

    def _bin_search_right(self, nums, target):
        low = 0
        high = len(nums)

        while low < high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid
            else:
                low = mid + 1

        return high - 1


class Solution:
    def searchRange(self, nums, target):
        res = [idx for idx, i in enumerate(nums) if i == target]
        if len(res) > 0:
            return [res[0], res[-1]]
        return [-1, -1]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    s = Solution()
    print(s.searchRange(nums, target))
# [3, 4]


    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    s = Solution()
    print(s.searchRange(nums, target))
# [-1, -1]

