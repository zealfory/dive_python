# -*- encoding: utf-8 -*-
# @File:   226.py    
# @Time: 2020-08-03 00:22
# @Author: ZHANG
# @Description: 226


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    """Mine"""
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

    """Official"""
    # def invertTree(self, root):
    #     if not root:
    #         return None
    #     left = self.invertTree(root.left)
    #     right = self.invertTree(root.right)
    #     root.left = right
    #     root.right = left
    #     return root
