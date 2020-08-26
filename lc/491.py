# -*- encoding: utf-8 -*-
# @File:   491.py    
# @Time: 2020-08-25 15:54
# @Author: ZHANG
# @Description: 491


class Solution:
    def findSubsequences(self, nums):
        n = len(nums)
        res = []
        path = []
        used = [False] * n
        cur_index = 0
        self.dfs(nums, n, 0, path, used, res, cur_index)
        return res

    def dfs(self, nums, n, depth, path, used, res, cur_index):
        # TODO 判断符合条件
        # res.append()
        if depth > 1 and path not in res:
            print(path[:])
            res.append(path[:])

        for i in range(n):
            if used[i] or (len(path) > 0 and nums[i] < path[-1]) or i < cur_index:
                continue
            path.append(nums[i])
            used[i] = True
            cur_index = i
            self.dfs(nums, n, depth + 1, path, used, res, cur_index)
            path.pop()
            used[i] = False


if __name__ == "__main__":
    a = [4, 6, 7, 7]
    s = Solution()
    print(s.findSubsequences(a))