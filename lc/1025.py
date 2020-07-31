# -*- encoding: utf-8 -*-
# @File:   1025.py    
# @Time: 2020-07-24 23:26
# @Author: ZHANG
# @Description: 1025


class Solution:
    def divisorGame(self, N: int) -> bool:
        # 怕不是傻X T.T
        #     选定除数
        #     while self._isDiv(N):
        #         x = self._chooseDiv(N)
        #         N -= x
        #     if N == 0:
        #         return True
        #     else:
        #         return False
        #
        # def _chooseDiv(self, N):
        #     l = [i for i in range(N)]
        #     x = ?
        #     return x
        #
        # def _isDiv(self, N):
        #     for i in range(1, N//2):
        #         if N % i == 0:
        #             return True
        #     return False
        return N % 2 == 0

    # 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
    #
    # 最初，黑板上有一个数字 N 。在每个玩家的回合，玩家需要执行以下操作：
    #
    # 选出任一 x，满足 0 < x < N
    # 且 N % x == 0 。
    # 用 N - x 替换黑板上的数字 N
    # 如果玩家无法执行这些操作，就会输掉游戏。
    #
    # 只有在爱丽丝在游戏中取得胜利时才返回 True，否则返回
    # false。假设两个玩家都以最佳状态参与游戏。

    # 大胆推理！
    # 当N=1, A输 ——> False
    #  N=2, A选1，B输 ——> True
    #  N=3, A选1，按照N=2 ——> False
    #  N=4, A选1或2√，按照N=3或2 ——> True
    #  ......
    #  所以只要是偶数，A就赢了


