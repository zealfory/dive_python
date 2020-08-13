# -*- encoding: utf-8 -*-
# @File:   43.py    
# @Time: 2020-08-13 11:47
# @Author: ZHANG
# @Description: 43


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        if len1 > 0 and len2 > 0:
            sum = 0
            for i in range(len1-1, -1, -1):
                for j in range(len2-1, -1, -1):
                    sum += int(num1[i]) * pow(10, len1 - 1 - i) * int(num2[j]) * pow(10, len2 - 1 - j)
            return str(sum)


if __name__ == "__main__":
    s = Solution()
    print(s.multiply('123', '456'))
