# -*- encoding: utf-8 -*-
# @File:   101.py    
# @Time: 2020-08-17 23:45
# @Author: ZHANG
# @Description: 101


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self._helper(root.left, root.right)

    def _helper(self, left_node, right_node):
        if not left_node and not right_node:
            return True
        if not left_node or not right_node:
            return False
        if left_node.val == right_node.val:
            left_res = self._helper(left_node.left, right_node.right)
            right_res = self._helper(left_node.right, right_node.left)
            return left_res and right_res
        return False
