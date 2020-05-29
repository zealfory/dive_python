# -*- encoding: utf-8 -*-
# @File:   invert_link_list.py    
# @Time: 2020-05-29 10:35
# @Author: ZHANG
# @Description: invert_link_list

"""
输入一个链表，从尾到头打印链表每个节点的值。
从头到尾遍历链表，并用一个栈存储每个结点的值，之后出栈输出值即可。
"""


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None


class Solution:
    def print_list_tail2head(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.print_list_tail2head(node1))
print(S.print_list_tail2head(test))
print(S.print_list_tail2head(singleNode))

