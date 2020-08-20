# -*- encoding: utf-8 -*-
# @File:   offer55.py    
# @Time: 2020-08-20 10:53
# @Author: ZHANG
# @Description: offer55


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """DFS后序遍历"""
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth(self, root):
        """BFS层序遍历"""
        if not root:
            return 0
        queue = [root]
        res = 0
        while queue:
            res += 1
            tmp = []
            for node in queue:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            queue = tmp
        return res


