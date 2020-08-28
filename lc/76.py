# -*- encoding: utf-8 -*-
# @File:   76.py    
# @Time: 2020-08-26 18:38
# @Author: ZHANG
# @Description: 76

from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        left = right = 0
        cur = list()
        res = s + " "
        t_count = Counter(t)
        distance = 0
        cur_count = defaultdict(int)
        while right < n:
            if cur_count[s[right]] < t_count[s[right]]:
                distance += 1
            cur.append(s[right])
            cur_count[s[right]] += 1
            right += 1
            while distance == len(t) and left <= right:
                if right - left < len(res):
                    res = ''.join(cur)

                if cur_count[s[left]] == t_count[s[left]]:
                    distance -= 1
                cur = cur[1:]
                cur_count[s[left]] -= 1
                left += 1

        return "" if res == s + " " else res


    # def minWindow(self, s: str, t: str) -> str:
    #     n = len(s)
    #     left = right = 0
    #     cur = list()
    #     res = s + " "
    #     t_count = Counter(t)
    #     while right < n:
    #         cur.append(s[right])
    #         while self.is_included(cur, t_count):
    #             if len(cur) < len(res):
    #                 res = ''.join(cur)
    #             cur = cur[1:]
    #             left += 1
    #         else:
    #             right += 1
    #     return "" if res == s + " " else res
    #
    # def is_included(self, cur, t_count):
    #     cur_count = Counter(cur)
    #     for k, v in t_count.items():
    #         if k in cur_count and cur_count[k] >= v:
    #             continue
    #         else:
    #             return False
    #     return True


if __name__ == "__main__":
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    # s = "a"
    # t = "aa"
    print(solution.minWindow(s, t))


"""
sliding-window
左边界右移 --> 可行解到最优解
右边界和左边界交替向右移动的过程中，少考虑了很多子空间
由于基于之前判断的结果，这些区间一定不是要找的目标值
"""
