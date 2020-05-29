# -*- encoding: utf-8 -*-
# @File:   two_dimensions_search.py    
# @Time: 2020-05-22 10:46
# @Author: ZHANG
# @Description: two_dimensions_search
"""
3.
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution:
    def Find(self, array, target):
        """是否存在"""
        if len(array) == 0:
            return False

        rownum = len(array)
        colnum = len(array[0])

        # 判断非法输入
        i = colnum - 1
        j = 0
        while i >= 0 and j < rownum:
            if array[j][i] < target:
                j += 1
            elif array[j][i] > target:
                i -= 1
            else:
                return True
        return False

    def searchMatrix(self, matrix, target):
        """输出个数"""
        if not matrix or len(matrix) == 0:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        row, col = 0, cols - 1
        count = 0
        while row <= rows - 1 and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                count += 1
                col -= 1
        return count


array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]

array2 = []
array3 = [['a', 'b', 'c'],
          ['b', 'c', 'd']]
array4 = [[62, 63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
          [63, 64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81],
          [64, 65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82],
          [65, 66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83],
          [66, 67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84],
          [67, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85]]

findtarget = Solution()
print(findtarget.Find(array, 10))
print(findtarget.Find(array, 30))
print(findtarget.Find(array, 13.0))
# print(findtarget.Find(array, ''))
print(findtarget.Find(array2, 10))
# print(findtarget.Find(array3, 'b'))
print(findtarget.searchMatrix(array4, 81))


