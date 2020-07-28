# -*- encoding: utf-8 -*-
# @File:   67.py    
# @Time: 2020-07-27 10:42
# @Author: ZHANG
# @Description: 67


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # TODO
        a = int(a, 2)
        b = int(b, 2)
        return bin(a+b)[2:]


if __name__ == "__main__":
    s = Solution()
    a = "1010"
    b = "1011"
    print(s.addBinary(a, b))
