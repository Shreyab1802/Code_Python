class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        totalSum = sum(range(0,len(nums)+1))
        inputSum = sum(nums)

        return totalSum - inputSum