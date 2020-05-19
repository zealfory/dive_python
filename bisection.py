# -*- encoding: utf-8 -*-
# @File:   bisection.py    
# @Time: 2020-05-19 15:31
# @Author: ZHANG
# @Description: bisection

import math


def bisection(function, a, b):
    """
    对于区间[a，b]上连续不断且f（a）·f（b）<0的函数y=f（x），
    通过不断地把函数f（x）的零点所在的区间一分为二，使区间的两个端点逐步逼近零点，进而得到零点近似值的方法叫二分法。
    """
    start = a
    end = b
    if function(a) == 0:
        return a
    elif function(b) == 0:
        return b
    elif function(a) * function(b) > 0:
        print("couldn't find root in [a, b]")
        return
    else:
        mid = start + (end - start) / 2.0
        while abs(start - mid) > 10 ** -7:
            if function(mid) == 0:
                return mid
            elif function(mid) * function(start) < 0:
                end = mid
            else:
                start = mid
            mid = start + (end - start) / 2.0
        return mid


def f(x):
    return math.pow(x, 3) - 2 * x - 5


if __name__ == "__main__":
    print(bisection(f, 1, 1000))
