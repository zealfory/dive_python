# -*- encoding: utf-8 -*-
# @File:   109.py    
# @Time: 2020-08-18 10:05
# @Author: ZHANG
# @Description: 109


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode):
        return self._create_tree(head, None)

    def _find_medium(self, left, right):
        p = q = left
        while q != right and q.next != right:
            p = p.next
            q = q.next.next
        return p

    def _create_tree(self, left, right):
        if left == right:
            return None
        mid = self._find_medium(left, right)
        root = TreeNode(mid.val)
        root.left = self._create_tree(left, mid)
        root.right = self._create_tree(mid.next, right)
        return root
