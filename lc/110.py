# -*- encoding: utf-8 -*-
# @File:   110.py    
# @Time: 2020-08-17 17:29
# @Author: ZHANG
# @Description: 110


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        flag = [True]

        def getHeight(root, flag):
            if not root or not flag[0]:
                return 0
            l = getHeight(root.left, flag)
            r = getHeight(root.right, flag)
            if abs(l - r) > 1:
                flag[0] = False
            return max(l, r) + 1
        getHeight(root, flag)
        return flag[0]


    # def isBalanced(self, root: TreeNode) -> bool:
    #     if not root:
    #         return True
    #     def getHeight(root):
    #         if not root:
    #             return 0
    #         l = getHeight(root.left)
    #         r = getHeight(root.right)
    #         return max(l, r) + 1
    #     return abs(getHeight(root.left) - getHeight(root.right)) <= 1 and self.isBalanced(root.left) \
    #            and self.isBalanced(root.right)

def T():
    global flag
    flag = True

    def t1():
        global flag
        flag = False
        print(flag)

    t1()
    return flag

print(T())
