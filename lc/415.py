# -*- encoding: utf-8 -*-
# @File:   415.py    
# @Time: 2020-08-03 18:24
# @Author: ZHANG
# @Description: 415


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # pass
        # len1 = len(num1)
        # len2 = len(num2)
        # if len1 > len2:
        #     length = len1
        # else:
        #     length = len2
        # sum = 0
        # for i in range(length):
        #     if i > len1:
        #
        #     if i < len1 and i < len2:
        #         sum += (int(num1[i]) + int(num2[i])) * pow(10, length - 1 - i)
        #     elif i < len1:
        #         sum += int(num1[i]) * pow(10, length - 1 - i)
        #     else:
        #         sum += int(num2[i]) * pow(10, length - 1 - i)
        # return str(sum)
        res = ""
        i, j, carry = len(num1) - 1, len(num2) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res


if __name__ == "__main__":
    s = Solution()
    print(s.addStrings('123', '12'))
