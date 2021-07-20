# -*- encoding: utf-8 -*-
# @File:   07.py    
# @Time: 2021/7/8 12:18 上午
# @Author: ZHANG
# @Description: 07

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        t = None
        if preorder and inorder:
            root = preorder[0]
            root_index = inorder.index(root)
            inorder_left, inorder_right = inorder[:root_index], inorder[root_index + 1:]
            preorder_left, preorder_right = preorder[1:len(inorder_left)+1], preorder[len(inorder_left) + 1:]
            t = TreeNode(root)
            t.left = self.buildTree(preorder_left, inorder_left)
            t.right = self.buildTree(preorder_right, inorder_right)
        return t


if __name__ == "__main__":
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s.buildTree(preorder, inorder)
