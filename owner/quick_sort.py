# -*- encoding: utf-8 -*-
# @File:   quick_sort.py    
# @Time: 2020-09-03 17:05
# @Author: ZHANG
# @Description: quick_sort

"""
快速排序
1. 先从数列中取出一个数作为基准数；
2. 分区过程，将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边；
3. 在对左右区间重复第二步，直到各区间只有一个数
"""


def adjust_array(s, l, r):
    pivot = s[l]
    while l < r:
        while l < r and s[r] >= pivot:
            r -= 1
        if l < r:
            s[l] = s[r]
            l += 1

        while l < r and s[l] <= pivot:
            l += 1
        if l < r:
            s[r] = s[l]
            r -= 1
    s[l] = pivot
    return l


def quick_sort(s, l, r):
    if l < r:
        i = adjust_array(s, l, r)
        quick_sort(s, l, i - 1)
        quick_sort(s, i + 1, r)


if __name__ == "__main__":
    s = [72, 6, 57, 88, 60, 42, 83, 73, 48, 85]
    quick_sort(s, 0, len(s))