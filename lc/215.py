# -*- encoding: utf-8 -*-
# @File:   215.py    
# @Time: 2020-07-30 16:36
# @Author: ZHANG
# @Description: 215

import heapq


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # heap = sorted(nums[:k], reverse=True)
        # for i in range(k, len(nums)):
        #     if nums[i] > heap[-1]:
        #         heap[-1] = nums[i]
        #     heap = sorted(heap, reverse=True)
        # return heap[-1]

        # heap = self._get_heap(nums)
        # while len(heap) > k:
        #     heap.pop(0)
        #     heap = self._get_heap(heap)
        #
        # return heap[0]
    #
    # def _get_heap(self, nums):
    #     heap = []
    #     for i in nums:
    #         heapq.heappush(heap, i)
    #     # print(heap)
    #     return heap

        # 替换nums[i]后维护最小堆：自顶向下调整新元素位置，直至该值满足(parent value < son value)
        def shift(i, k):
            flag = 0
            while (i * 2 + 1) < k and flag == 0:
                t = i
                if nums[i] > nums[2 * i + 1]:
                    t = 2 * i + 1
                if (i * 2 + 2) < k and nums[t] > nums[2 * i + 2]:
                    t = 2 * i + 2
                if t == i:
                    flag = 1
                else:
                    nums[i], nums[t] = nums[t], nums[i]
                    i = t

                    # O(k):建立大小为K的最小堆， k/2-1是最后一个非叶节点，因为shift是向下调整，所以倒序从最下面出发，
                    # 不然(4 32 1)->(2 34 1)->(2 14 3)->(2 14 3) 结果不对

        for i in range(k // 2, -1, -1):
            shift(i, k)

        # O((N-k)logK)，剩余元素依次比较替换
        for i in range(k, len(nums)):
            if nums[0] < nums[i]:
                nums[0] = nums[i]
                shift(0, k)
        return nums[0]
        # sum=O(Nlogk-k(logK-1))


if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    s = Solution()
    print(s.findKthLargest(nums, k))
