# -*- encoding: utf-8 -*-
# @File:   108.py    
# @Time: 2020-08-18 18:14
# @Author: ZHANG
# @Description: 108


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self._createBST(nums, 0, len(nums))

    def _createBST(self, nums, left, right):
        if left == right:
            return None
        mid = left + ((right - left) >> 1)
        root = TreeNode(nums[mid])
        root.left = self._createBST(nums, left, mid)
        root.right = self._createBST(nums, mid + 1, right)
        return root
