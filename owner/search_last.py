# -*- encoding: utf-8 -*-
# @File:   search_last.py    
# @Time: 2020-09-05 13:55
# @Author: ZHANG
# @Description: search_last


class Solution:
    def search_last(self, nums, target):
        right = self._bin_search_right(nums, target)
        if right >= 0 and nums[right] == target:
            return right
        return -1

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


if __name__ == "__main__":
    nums = [5, 7, 7, 5, 4, 10]
    target = 8
    s = Solution()
    print(s.search_last(nums, target))

