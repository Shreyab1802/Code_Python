class Solution:
    def canJump(self, nums: List[int]) -> bool:
         # We will shift the goal from right to left
        goal = len(nums) -1

        #checking from reverse if we can reach the start position
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False