# -*- encoding: utf-8 -*-
# @File:   102.py    
# @Time: 2020-08-27 23:33
# @Author: ZHANG
# @Description: 102

 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        res = []

        def levelSearch(node, level):
            if not root:
                return
            if len(res) == level:
                res.append([])
            res[level].append(node.val)
            if node.left:
                levelSearch(node.left, level+1)
            if node.right:
                levelSearch(node.right, level+1)

        levelSearch(root, 0)
        return res
