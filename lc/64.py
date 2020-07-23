# -*- encoding: utf-8 -*-
# @File:   64.py    
# @Time: 2020-07-23 14:41
# @Author: ZHANG
# @Description: 64[动态规划]


class Solution:
    def minPathSum(self, grid):
        col_num = len(grid[0])
        row_num = len(grid)
        dp = [[0 for _ in range(col_num)] for _ in range(row_num)]
        for i in range(row_num):
            for j in range(col_num):
                if i == 0 and j > 0:
                    dp[i][j] = dp[0][j - 1] + grid[0][j]
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][0] + grid[i][0]
                elif i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
                else:
                    dp[i][j] = grid[0][0]
        return dp[-1][-1]


if __name__ == "__main__":
    a = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    s = Solution()
    print(s.minPathSum(a))


























"""
由于路径的方向只能是向下或向右，因此网格的第一行的每个元素只能从左上角元素开始向右移动到达，网格的第一列的每个元素只能从左上角元素开始向下移动到达，
此时的路径是唯一的，因此每个元素对应的最小路径和即为对应的路径上的数字总和。

对于不在第一行和第一列的元素，可以从其上方相邻元素向下移动一步到达，或者从其左方相邻元素向右移动一步到达，
元素对应的最小路径和等于其上方相邻元素与其左方相邻元素两者对应的最小路径和中的最小值加上当前元素的值。
由于每个元素对应的最小路径和与其相邻元素对应的最小路径和有关，因此可以使用动态规划求解。

创建二维数组dp，与原始网格的大小相同，dp[i][j] 表示从左上角出发到 (i,j) 位置的最小路径和。
显然，dp[0][0]=grid[0][0]。对于 dp 中的其余元素，通过以下状态转移方程计算元素值。

当 i>0 且 j=0 时，dp[i][0]=dp[i−1][0]+grid[i][0]。

当 i=0 且 j>0 时，dp[0][j]=dp[0][j−1]+grid[0][j]。

当 i>0 且 j>0 时，dp[i][j]=min(dp[i−1][j],dp[i][j−1])+grid[i][j]。

最后得到 dp[m−1][n−1] 的值即为从网格左上角到网格右下角的最小路径和。
"""


