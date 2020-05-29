# -*- encoding: utf-8 -*-
# @File:   replace_space.py    
# @Time: 2020-05-22 22:19
# @Author: ZHANG
# @Description: replace_space

"""
4.
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy
"""

import re


class Solution(object):

    def replace_space(self, s):
        """my solution"""
        return re.sub(" ", "%20", s)

    def replaceSpaceByAppend(self, s):
        """ append - O(n)"""
        string = list(s)
        stringReplace = []
        for item in string:
            if item == ' ':
                stringReplace.append('%')
                stringReplace.append('2')
                stringReplace.append('0')
            else:
                stringReplace.append(item)
        return ''.join(stringReplace)

    def replaceSpace1(self, s):
        """new string"""
        tempstr = ''
        if type(s) != str:
            return
        for c in s:
            if c == ' ':
                tempstr += '%20'
            else:
                tempstr += c
        return tempstr

    def replaceSpace2(self, s):
        """str.replace"""
        if type(s) != str:
            return
        return s.replace(' ', '%20')

s = 'we are happy'
test = Solution()
print(test.replace_space(s))
print(test.replaceSpace1(s))
print(test.replaceSpace2(s))
