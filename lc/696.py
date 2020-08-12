# -*- encoding: utf-8 -*-
# @File:   696.py    
# @Time: 2020-08-11 22:19
# @Author: ZHANG
# @Description: 696


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pre_c = s[0]
        pre = 0
        cur = 1
        res = 0
        for c in s[1:]:
            if c == pre_c:
                cur += 1
            else:
                pre, cur = cur, 1
            if pre >= cur:
                res += 1
            pre_c = c
        return res
