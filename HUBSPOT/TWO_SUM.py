from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums and i != nums.index(complement):
                return [i, nums.index(complement)]




solution = Solution()
arr = [3, 6, 4, 5, 9, 1, 8, 11]
target = 9

print(solution.twoSum(arr,target))