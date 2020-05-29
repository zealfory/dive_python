# -*- encoding: utf-8 -*-
# @File:   reconstruct_bt.py    
# @Time: 2020-05-29 10:47
# @Author: ZHANG
# @Description: reconstruct_bt

"""
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根结点
    def reconstruct_binary_tree(self, pre, tin):
        if not pre and not tin:
            return None
        if set(pre) != set(tin):
            return None
        root = TreeNode(pre[0])
        i = tin.index(pre[0])
        root.left = self.reconstruct_binary_tree(pre[1:i+1], tin[:i])
        root.right = self.reconstruct_binary_tree(pre[i+1:], tin[i+1:])
        return root


pre = [1, 2, 4, 7, 3, 5, 6, 8]
tin = [4, 7, 2, 1, 5, 3, 8, 6]
test = Solution()
newTree = test.reconstruct_binary_tree(pre, tin)


def print_node_at_level(root):
    """ 层序遍历 """
    if not root:
        return 0
    queue = ["r"]
    queue.append(root)
    while len(queue) > 0:
        node = queue.pop(0)
        if isinstance(node, TreeNode):
            print(node.val, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        else:
            if len(queue) > 0:
                queue.append("r")
                print()


print_node_at_level(newTree)