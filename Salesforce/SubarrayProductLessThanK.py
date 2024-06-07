class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        product = 1
        left = 0
        result = 0

        for r in range(len(nums)):
            product *= nums[r]

            while product >= k and left <= r:
                product = product // nums[left]
                left += 1

            result += (r - left + 1)

        return result