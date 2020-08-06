# -*- encoding: utf-8 -*-
# @File:   98.py    
# @Time: 2020-08-05 10:18
# @Author: ZHANG
# @Description: 98


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """递归"""
    # def isValidBST(self, root: TreeNode) -> bool:
    #     def helper(node, lower=float('-inf'), upper=float('inf')):
    #         if node:
    #             if node.val <= lower or node.val >= upper:
    #                 return False
    #             is_leftValid = helper(node.left, lower, node.val)
    #             is_rightValid = helper(node.right, node.val, upper)
    #             return is_leftValid and is_rightValid
    #         return True
    #     return helper(root)

    """迭代"""
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        lower = float('-inf')
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            if root.val <= lower:
                return False
            lower = root.val
            root = root.right
        return True

