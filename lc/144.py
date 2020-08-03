# -*- encoding: utf-8 -*-
# @File:   144.py    
# @Time: 2020-08-03 16:04
# @Author: ZHANG
# @Description: 144


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] +  self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

