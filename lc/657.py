# -*- encoding: utf-8 -*-
# @File:   657.py    
# @Time: 2020-08-28 15:37
# @Author: ZHANG
# @Description: 657


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        moves_count = Counter(moves)
        if moves_count['U'] == moves_count['D'] and \
        moves_count['L'] == moves_count['R']:
            return True
        return False
