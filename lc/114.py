# -*- encoding: utf-8 -*-
# @File:   114.py    
# @Time: 2020-08-03 16:19
# @Author: ZHANG
# @Description: 114

 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        pre_list = []

        def _preorder(root):
            if root:
                pre_list.append(root)
                _preorder(root.left)
                _preorder(root.right)
        _preorder(root)
        for i in range(1, len(pre_list)):
            prev, curr = pre_list[i - 1], pre_list[i]
            prev.left = None
            prev.right = curr



