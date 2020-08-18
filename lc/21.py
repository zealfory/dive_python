# -*- encoding: utf-8 -*-
# @File:   21.py    
# @Time: 2020-08-18 14:06
# @Author: ZHANG
# @Description: 21

 
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """暴力解法O(m+n)"""
        lis = ListNode(0)  # 哑节点
        l = lis
        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    l.next = l1
                    l1 = l1.next
                    l = l.next
                else:
                    l.next = l2
                    l2 = l2.next
                    l = l.next
            elif l1:
                l.next = l1
                l1 = l1.next
                l = l.next
            else:
                l.next = l2
                l2 = l2.next
                l = l.next
        return lis.next

    def mergeTwoLists(self, l1, l2):
        """递归解法O(m+n)"""
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2





