class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sum_list = []

        for i in range(len(nums) - 1):

            low = i + 1
            high = len(nums) - 1

            while low < high:
                if nums[i] + nums[low] + nums[high] == 0:
                    if (nums[i], nums[low], nums[high]) not in sum_list:
                        sum_list.append((nums[i], nums[low], nums[high]))

                    low += 1
                    high -= 1
                elif nums[i] + nums[low] + nums[high] > 0:
                    high -= 1
                else:
                    low += 1

        return sum_list



