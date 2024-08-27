import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        sorted_list = []
        count = 0

        for i in nums:
            if i not in numsMap:
                numsMap[i] = count + 1
            else:
                numsMap[i] = numsMap[i] + 1

        print(numsMap)
        # sorted(numsMap.items(), key=lambda kv: (kv[1], kv[0]), reverse = True)
        sorted_d = dict(sorted(numsMap.items(), key=operator.itemgetter(1), reverse=True))
        print(sorted_d)
        for i in sorted_d:
            if len(sorted_list) < k:
                print(i)
                sorted_list.append(i)

        print(sorted_d)



######## Better solution of nlogk ##########

from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # O(1) time
        if k == len(nums):
            return nums

        # 1. Build hash map: character and how often it appears
        # O(N) time
        count = Counter(nums)
        # 2-3. Build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time
        return heapq.nlargest(k, count.keys(), key=count.get)