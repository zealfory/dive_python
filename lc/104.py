# -*- encoding: utf-8 -*-
# @File:   104.py    
# @Time: 2020-07-28 10:04
# @Author: ZHANG
# @Description: 104


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # 时间O(n) 空间O(height)
        if root.val is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# TODO
# class BiTree:
#     """class BiTree provide interface to set up a BiTree and to interact"""
#     def __init__(self, tree_node=None):
#         """set up BiTree from BiNode and empty BiTree when nothing is passed"""
#         self.root = tree_node


if __name__ == "__main__":
    s = Solution()
    # TODO
    # tree = [3, 9, 20, None, None, 15, 7]
    # tree = TreeNode(3)
    # tree.left =
    # print(s.maxDepth(tree))
