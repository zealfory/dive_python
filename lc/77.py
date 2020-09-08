# -*- encoding: utf-8 -*-
# @File:   77.py    
# @Time: 2020-09-08 16:54
# @Author: ZHANG
# @Description: 77


class Solution:
    def combine(self, n: int, k: int):
        res = []
        path = []

        def back_track(n, k, path, cur):
            if len(path) == k:
                res.append(path[:])
            for i in range(cur+1, n+1):
                path.append(i)
                back_track(n, k, path, i)
                path.pop()
        back_track(n, k, path, 0)
        return res


if __name__ == "__main__":
    s = Solution()
    n = 4
    k = 2
    print(s.combine(n, k))
