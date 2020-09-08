# -*- encoding: utf-8 -*-
# @File:   547.py    
# @Time: 2020-08-28 15:41
# @Author: ZHANG
# @Description: 547


class Solution:
    def findCircleNum(self, M) -> int:
        n = len(M)
        parent = [-1] * n
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j] == 1 and i != j:
                    self._union(parent, i, j)
        count = 0
        for i in range(n):
            if parent[i] == -1:
                count += 1
        return count

    def _union(self, parent, i, j):
        pi = self._find(parent, i)
        pj = self._find(parent, j)
        if pi != pj:
            parent[pi] = pj

    def _find(self, parent, i):
        if parent[i] == -1:
            return i
        return self._find(parent, parent[i])


if __name__ == "__main__":
    M = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ]
    s = Solution()
    print(s.findCircleNum(M))

