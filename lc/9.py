# -*- encoding: utf-8 -*-
# @File:   9.py    
# @Time: 2020-07-31 13:03
# @Author: ZHANG
# @Description: 9


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """对折"""
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        suffix = x % 10
        x //= 10
        while x > suffix:
            suffix = suffix * 10 + x % 10
            x //= 10
        else:
            return suffix // 10 == x or x == suffix


if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome(9))

