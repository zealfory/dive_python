# -*- encoding: utf-8 -*-
# @File:   46.py    
# @Time: 2020-08-11 22:13
# @Author: ZHANG
# @Description: 46


class Solution:
    def permute(self, nums):
        n = len(nums)
        res = []
        if n == 0:
            return res
        path = []
        used = [False] * n
        self.dfs(nums, n, 0, path, used, res)
        return res

    def dfs(self, nums, n, depth, path, used, res):
        if depth == n:
            res.append(path[:])  # ps：要append list而不是引用
        for i in range(n):
            if used[i]:
                continue
            path.append(nums[i])
            used[i] = True
            self.dfs(nums, n, depth + 1, path, used, res)
            path.pop()
            used[i] = False


if __name__ == "__main__":
    a = [1, 2, 3]
    s = Solution()
    print(s.permute(a))


