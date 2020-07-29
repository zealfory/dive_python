# -*- encoding: utf-8 -*-
# @File:   14.py    
# @Time: 2020-07-29 13:44
# @Author: ZHANG
# @Description: 14


class Solution:
    def longestCommonPrefix(self, strs) -> str:
        common = ""
        longest_len = min(len(s) for s in strs) if len(strs) > 0 else 0

        for i in range(longest_len):
            for j in range(len(strs)):
                if j == 0:
                    common = strs[j][:i + 1]
                elif strs[j][:i + 1] == common:
                    continue
                else:
                    return common[:-1]
        return common


if __name__ == "__main__":
    # strs = ["flower", "flow", "flight"]
    strs = ["dog", "racecar", "car"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
