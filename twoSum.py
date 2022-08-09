class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        output = {}
        for i, j in enumerate(nums):
            rem = target - j
            if rem in output:
                return [output[rem], i]
            else:
                output[j] = i