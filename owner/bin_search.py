# -*- encoding: utf-8 -*-
# @File:   bin_search.py    
# @Time: 2020-08-17 17:34
# @Author: ZHANG
# @Description: bin_search


def binary_search(lis, num):
    """non-recursion binary search"""
    left = 0
    right = len(lis) - 1
    while left <= right:
        # mid = (left + right) // 2
        mid = left + ((right - left) >> 1)
        print(mid)
        if num < lis[mid]:
            right = mid - 1
        elif num > lis[mid]:
            left = mid + 1
        else:
            return mid
    return -1


lis = [11, 32, 51, 21, 42, 9, 5, 6, 7, 8]
print(lis)
lis.sort()
print(lis)
num = 8
print(binary_search(lis, num))


def binary_search2(lis, left, right, num):
    if left > right:  # 递归终止条件
        return -1
    mid = (left + right) // 2
    if num < lis[mid]:
        right = mid - 1
    elif num > lis[mid]:
        left = mid + 1
    else:
        return mid
    return binary_search2(lis, left, right, num)


print(binary_search2(lis, 0, len(lis) - 1, num))
