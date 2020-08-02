# -*- encoding: utf-8 -*-
# @File:   7.py    
# @Time: 2020-07-16 10:57
# @Author: ZHANG
# @Description: 7
import math


# class Solution:
#     def _reverse(self, x):
#         flag = False
#         if x < 0:
#             flag = True
#             x = -x
#         x = str(x)
#         x_reversed = int(x[::-1])
#         if flag:
#             x_reversed *= -1
#         return x_reversed
#
#     def reverse(self, x: int) -> int:
#         x_reversed = self._reverse(x)
#         if (-1) * math.pow(2, 31) <= x_reversed < math.pow(2, 31):
#             return x_reversed
#         else:
#             return 0

class Solution:
    def reverse(self, x):
        rev = 0
        x_new = abs(x)
        while x != 0:
            pop = x_new % 10
            # pop = int(math.fmod(x, 10))
            # print(pop)
            # x = int(x/10)
            x_new /= 10
            if rev > ((math.pow(2, 31) - 1) / 10) or (rev == (math.pow(2, 31) - 1) / 10 and pop > 7):
                return 0
            # if rev < ((-1) * math.pow(2, 31) / 10) or (rev == (-1) * math.pow(2, 31) / 10 and pop < -8):
            #     return 0
            rev = rev * 10 + pop
        return rev if x > 0 else -rev


if __name__ == "__main__":
    s = Solution()
    # res = s.reverse(123)
    # print(res)
    res = s.reverse(-123)
    print(res)
    # res = s.reverse(1534236469)
    # print(res)

"""
7. 整数反转
方法：弹出和推入数字 & 溢出前进行检查

思路
可以一次构建反转整数的一位数字。在这样做的时候，可以预先检查向原整数附加另一位数字是否会导致溢出。

算法
反转整数的方法可以与反转字符串进行类比。
想重复“弹出” x 的最后一位数字，并将它“推入”到 rev 的后面。最后，rev 将与 x 相反。

要在没有辅助堆栈 / 数组的帮助下 “弹出” 和 “推入” 数字，可以使用数学方法。


//pop operation:
pop = x % 10;
x /= 10;

//push operation:
temp = rev * 10 + pop;
rev = temp;

但是，这种方法很危险，因为当 temp=rev⋅10+pop 时会导致溢出。

幸运的是，事先检查这个语句是否会导致溢出很容易。

为了便于解释，我们假设 rev 是正数。

如果 temp=rev⋅10+pop 导致溢出，那么一定有 rev ≥ INTMAX/10。
如果 rev > INTMAX/10，那么 temp=rev⋅10+pop 一定会溢出。
如果 rev == INTMAX/10，那么只要 pop>7，temp=rev⋅10+pop 就会溢出。
当 rev 为负时可以应用类似的逻辑。


复杂度分析

时间复杂度：O(log(x))，x 中大约有log10(x)位数字。
空间复杂度：O(1)

"""