# -*- encoding: utf-8 -*-
# @File:   17.py    
# @Time: 2020-08-26 14:02
# @Author: ZHANG
# @Description: 17


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        digit_dic = {
                     '2': 'abc', '3': 'def', '4': 'ghi',
                     '5': 'jkl', '6': 'mno', '7': 'pqrs',
                     '8': 'tuv', '9': 'wxyz'
                     }

        def backtrack(index):
            if index == len(digits):
                res.append("".join(combination))
            else:
                for c in digit_dic[digits[index]]:
                    combination.append(c)
                    backtrack(index + 1)
                    combination.pop()

        res = list()
        combination = list()
        backtrack(0)
        return res


if __name__ == "__main__":
    s = Solution()
    d = '23'
    print(s.letterCombinations(d))

