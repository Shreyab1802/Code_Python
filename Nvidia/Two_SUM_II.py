from typing import List, Tuple

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        value_index_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in value_index_map:
                result.append([value_index_map[complement],i])
            value_index_map[nums[i]] = i
        return result

# Example usage
solution = Solution()
arr = [3, 6, 4, 5, 9, 1, 8, 11]
target = 9
print(solution.twoSum(arr, target))  # Output: [[0, 1], [2, 3], [5, 6]]
