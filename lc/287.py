# -*- encoding: utf-8 -*-
# @File:   287.py    
# @Time: 2020-07-21 16:12
# @Author: ZHANG
# @Description: 287


class Solution:
    def findDuplicate(self, nums):
        # 方法0（暴力法）
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]

        # 方法1 时间O(n) 空间0
        # for i in nums:
        #     if nums.count(i) > 1:
        #         return i

        # 方法2（哈希）时间O(n) 空间O(n)
        # nums_set = set()
        # for i in nums:
        #     if nums_set.__contains__(i):
        #         return i
        #     nums_set.add(i)

        # 方法3 快慢指针 todo
        j = 2
        for i in range(len(nums)):
            if j < len(nums) and nums[i] == nums[j]:
                return nums[i]
            elif nums[i] == nums[j - len(nums)]:
                return nums[i]
            else:
                j += 2


if __name__ == "__main__":
    s = Solution()
    a = [14, 16, 12, 1, 16, 17, 6, 8, 5, 19, 16, 13, 16, 3, 11, 16, 4, 16, 9, 7]
    # a = [1, 3, 4, 2, 2]
    # a = [3, 1, 3, 4, 2]
    # a = '13422'
    a = [1,3,4,2,1]
    # print(a.count('2'))
    print(s.findDuplicate(a))
