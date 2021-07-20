# -*- encoding: utf-8 -*-
# @File:   350.py
# @Time: 2021-05-19 23:11
# @Author: ZHANG
# @Description: 20210519

from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        nums1.sort()
        nums2.sort()
        p = q = 0
        while p < len(nums1) and q < len(nums2):
            if nums1[p] == nums2[q]:
                res.append(nums1[p])
                p += 1
                q += 1
            elif nums1[p] < nums2[q]:
                p += 1
            else:
                q += 1
        return res


if __name__ == "__main__":
    s = Solution()
    # nums1 = [1, 2, 2, 1]
    # nums2 = [2, 2]
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(s.intersect(nums1, nums2))
