# -*- encoding: utf-8 -*-
# @File:   offer19.py    
# @Time: 2020-09-05 14:08
# @Author: ZHANG
# @Description: offer19

"""
.^$只作为控制字符， 代表的含义如下
^表示匹配输入字符串的开头
$表示匹配输入字符串的结尾
.表示任意字符
*代表匹配0\任意个前面的字符
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in (".", s[0])
        if len(p) >= 2 and p[1] == "*":
            if first_match:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            return self.isMatch(s, p[2:])
        if len(p) >= 2 and p[0] == "^":
            if p[1] in (".", s[0]):
                return self.isMatch(s[1:], p[1:]) or self.isMatch(s, p[2:])
        if len(p) >= 2 and p[-1] == "$":
            if p[-2] in (".", s[-1]):
                return self.isMatch(s[:-1], p[:-1]) or self.isMatch(s, p[:-2])
        return first_match and self.isMatch(s[1:], p[1:])
