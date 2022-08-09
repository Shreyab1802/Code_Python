class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i, j in enumerate(nums):
            if j == target:
                return i
            else:
                continue
        return -1
