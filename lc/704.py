# -*- encoding: utf-8 -*-
# @File:   704.py    
# @Time: 2021/7/23 12:18 上午
# @Author: ZHANG
# @Description: 704
from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

Solution.search([-1,0,3,5,9,12], 2)