# -*- encoding: utf-8 -*-
# @File:   912.py    
# @Time: 2021/7/21 12:59 上午
# @Author: ZHANG
# @Description: 912
from typing import List
import random


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.quick_sort(nums, 0, len(nums)-1)

    def quick_sort(self, nums: List[int], low: int, high: int) -> List[int]:
        if low < high:
            pivot = self.partition(nums, low, high)
            self.quick_sort(nums, low, pivot - 1)
            self.quick_sort(nums, pivot + 1, high)
        return nums

    def partition(self, nums, low, high):
        """随机化分区"""
        pivot = random.randint(low, high)
        nums[low], nums[pivot] = nums[pivot], nums[low]
        index = low + 1
        i = index
        while i <= high:
            if nums[i] < nums[low]:
                nums[i], nums[index] = nums[index], nums[i]
                index += 1
            i += 1
        nums[low], nums[index-1] = nums[index-1], nums[low]
        return index - 1


s = Solution()
l = [5, 2, 3, 1]
print(s.sortArray(l))