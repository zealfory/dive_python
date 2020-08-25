# -*- encoding: utf-8 -*-
# @File:   459.py    
# @Time: 2020-08-24 10:39
# @Author: ZHANG
# @Description: 459


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """Mine"""
        len_s = len(s)
        flags = []
        for i in range(len_s//2):
            if (len_s - i - 1) % (i + 1) != 0:
                continue
            target = s[0:i+1]
            flag = True
            j = i+1
            tmp = s[j:]
            while flag:
                if tmp[0: i+1] != target:
                    flag = False
                j += i + 1
                if j < len_s:
                    tmp = s[j:]
                else:
                    break
            flags.append(flag)
        return True in flags

    def repeatedSubstringPattern(self, s):
        """枚举"""
        n = len(s)
        for i in range(1, n//2+1):
            if n % i == 0:
                if all(s[j] == s[j - i] for j in range(i, n)):
                    return True
        return False


if __name__ == "__main__":
    s = Solution()
    s1 = 'aba'
    print(s.repeatedSubstringPattern(s1))
