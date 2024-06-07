class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]

        min_so_far = nums[0]

        result = max_product

        for i in range(1, len(nums)):
            curr = nums[i]

            temp_max = max(curr, max_product * curr, min_so_far * curr)
            min_so_far = min(curr, max_product * curr, min_so_far * curr)

            max_product = temp_max

            result = max(max_product, result)

        return result



