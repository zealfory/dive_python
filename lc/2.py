# -*- encoding: utf-8 -*-
# @File:   2.py    
# @Time: 2020-08-17 23:46
# @Author: ZHANG
# @Description: 2


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = p = ListNode(None)
        s = 0
        while l1 or l2 or s:
            s += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            p.next = ListNode(s % 10)
            p = p.next
            s //= 10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next
