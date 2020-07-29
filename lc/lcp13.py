# -*- encoding: utf-8 -*-
# @File:   lcp13.py    
# @Time: 2020-07-29 11:18
# @Author: ZHANG
# @Description: lcp13


class Solution:
    def minimalSteps(self, maze) -> int:

        pass

























"""
输入： ["S#O", "M..", "M.T"]

输出：16

解释：最优路线为： S->O, cost = 4, 去搬石头 O->第二行的M, cost = 3, M机关触发 第二行的M->O, cost = 3, 
我们需要继续回去 O 搬石头。 O->第三行的M, cost = 4, 此时所有机关均触发 第三行的M->T, cost = 2，去T点拿宝藏。 总步数为16。

"""