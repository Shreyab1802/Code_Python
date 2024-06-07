# We will just pair it with the most possible greater element
# in it's permutation
# This can be achieved by sorting
# the array and then compare that index with each value on that index

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        i = 0
        for each in sorted_nums:
            if each > sorted_nums[i]:
                i += 1

        return i