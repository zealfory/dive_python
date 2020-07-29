# -*- encoding: utf-8 -*-
# @File:   14.py    
# @Time: 2020-07-29 13:44
# @Author: ZHANG
# @Description: 14

import sys


class TrieTree:
    def __init__(self):
        self.root = {}
        self.word_end = -1

    def insert(self, word):
        curNode = self.root
        for char in word:
            if not char in curNode:
                curNode[char] = {}
            curNode = curNode[char]
        curNode[self.word_end] = True

    def search(self, word):
        curNode = self.root
        for char in word:
            if not char in curNode:
                return False
            curNode = curNode[char]
        if self.word_end not in curNode:
            return False
        return True

    def startsWith(self, prefix):

        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]

        return True

    def largestCommonPrefix(self, word):
        curNode = self.root
        count = 0
        for char in word:
            if char in curNode and len(curNode) == 1:
                curNode = curNode[char]
                count += 1
            else:
                break
        return count


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # 方法一
        # common = ""
        # longest_len = min(len(s) for s in strs) if len(strs) > 0 else 0
        #
        # for i in range(longest_len):
        #     for j in range(len(strs)):
        #         if j == 0:
        #             common = strs[j][:i + 1]
        #         elif strs[j][:i + 1] == common:
        #             continue
        #         else:
        #             return common[:-1]
        # return common

        # 方法二
        # if not strs:
        #     return ""
        #
        # prefix, count = strs[0], len(strs)
        # for i in range(1, count):
        #     prefix = self.lcp(prefix, strs[i])
        #     if not prefix:
        #         break
        #
        # return prefix

    # def lcp(self, str1, str2):
    #     length, index = min(len(str1), len(str2)), 0
    #     while index < length and str1[index] == str2[index]:
    #         index += 1
    #     return str1[:index]

        # 方法三
        tree = TrieTree()
        for s in strs:
            tree.insert(s)
        print(tree.root)
        longest_length = sys.maxsize
        for s in strs:
            longest_length = int(min(int(longest_length), int(tree.largestCommonPrefix(s))))
        return strs[0][:longest_length]


if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    s = Solution()
    print(s.longestCommonPrefix(strs))



"""
对所有串建立字典树，对于两个串的最长公共前缀的长度即他们所在的节点的公共祖先个数，于是，问题就转化为最近公共祖先问题。
"""