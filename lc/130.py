# -*- encoding: utf-8 -*-
# @File:   130.py    
# @Time: 2020-08-12 10:53
# @Author: ZHANG
# @Description: 130


class Solution:
    """深度优先遍历"""
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_num = len(board)
        if row_num == 0:
            return
        col_num = len(board[0])
        # 第一行和最后一行
        for i in [0, row_num - 1]:
            for j in range(col_num):
                if board[i][j] == "O":
                    self.dfs(board, i, j, row_num, col_num)
        # 第一列和最后一列
        for j in [0, col_num-1]:
            for i in range(row_num):
                if board[i][j] == "O":
                    self.dfs(board, i, j, row_num, col_num)

        for i in range(row_num):
            for j in range(col_num):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"

    def dfs(self, board, i, j, row_num, col_num):
        if board[i][j] == "O":
            board[i][j] = "#"
        if i - 1 > 0 and board[i-1][j] == "O":
            self.dfs(board, i-1, j, row_num, col_num)
        if j - 1 > 0 and board[i][j-1] == "O":
            self.dfs(board, i, j-1, row_num, col_num)
        if i + 1 < row_num and board[i+1][j] == "O":
            self.dfs(board, i+1, j, row_num, col_num)
        if j + 1 < col_num and board[i][j+1] == "O":
            self.dfs(board, i, j+1, row_num, col_num)


if __name__ == "__main__":
    board = [['X'] * 4,
             ['X', 'O', 'O', 'X'],
             ['X', 'X', 'O', 'X'],
             ['X', 'O', 'X', 'X']]
    print(board)
    s = Solution()
    s.solve(board)
    print(board)
