# -*- encoding: utf-8 -*-
# @File:   917.py    
# @Time: 2020-07-27 10:42
# @Author: ZHANG
# @Description: 917


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # TODO
        # tmp = list()
        # num_ind = dict()
        # for i in range(len(S)):
        #     if S[i].isalpha():
        #         tmp.append(S[i])
        #     else:
        #         num_ind[i] = S[i]
        # s_reversed = list(reversed(tmp))
        # # print(s_reversed)
        # for k, v in num_ind.items():
        #     s_reversed.insert(k, v)
        # # print(s_reversed)
        # return ''.join(s_reversed)

        """字母栈 O(N)"""
        s = ""
        tmp = [c for c in S if c.isalpha()]
        for char in S:
            if char.isalpha():
                s += tmp.pop()
            else:
                s += char
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.reverseOnlyLetters("ab1c"))
"""
S.length <= 100
33 <= S[i].ASCIIcode <= 122 
S 中不包含 \ or "
"""