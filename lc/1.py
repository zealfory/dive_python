# -*- encoding: utf-8 -*-
# @File:   1.py    
# @Time: 2020-08-26 15:12
# @Author: ZHANG
# @Description: 1

 
class Solution:
    def twoSum(self, nums, target: int):
        nums_dict = dict()
        for i, n in enumerate(nums):
            remain = target - n
            if remain in nums_dict:
                return [i, nums_dict[remain]]
            else:
                nums_dict[n] = i
