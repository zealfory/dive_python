# -*- encoding: utf-8 -*-
# @File:   107.py    
# @Time: 2020-09-08 15:41
# @Author: ZHANG
# @Description: 107

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        stack = []
        stack.append(root)
        tmp = []
        res = []
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                tmp.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            res.append(tmp[:])
            tmp = []

        return res[::-1]

 
