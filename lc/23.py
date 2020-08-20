# -*- encoding: utf-8 -*-
# @File:   23.py    
# @Time: 2020-08-19 17:57
# @Author: ZHANG
# @Description: 23


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        return self._merge_helper(lists, 0, len(lists) - 1)

    def _merge_helper(self, lists, left, right):
        if left > right:
            return
        if left == right:
            return lists[left]
        if left + 1 == right:  # 这行不需要
            return self.mergeTwoLists(lists[left], lists[right])
        mid = left + ((right - left) >> 1)
        left_res = self._merge_helper(lists, left, mid)
        right_res = self._merge_helper(lists, mid + 1, right)
        return self.mergeTwoLists(left_res, right_res)

    def mergeTwoLists(self, l1, l2):
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
