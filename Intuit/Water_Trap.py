class Solution:
    def trap(self, height: List[int]) -> int:
        #In brute force, we iterate over the left and right parts again and again
        # just to find the highest bar size #upto that index. But, this could be stored. Voila, dynamic programming.

       # Find maximum height of bar from the left end upto an index i in the array left_max.
        #Find maximum height of bar from the right end upto an index i in the array right_max.
        #Iterate over the height array and update ans:
        #Add min(left_max[i],right_max[i])−height[i] to ans

        # Case of empty height list
        if len(height) == 0:
            return 0
        ans = 0
        size = len(height)
        # Create left and right max arrays
        left_max, right_max = [0] * size, [0] * size
        # Initialize first height into left max
        left_max[0] = height[0]
        for i in range(1, size):
            # update left max with current max
            left_max[i] = max(height[i], left_max[i - 1])
        # Initialize last height into right max
        right_max[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            # update right max with current max
            right_max[i] = max(height[i], right_max[i + 1])
        # Calculate the trapped water
        for i in range(1, size - 1):
            ans += min(left_max[i], right_max[i]) - height[i]
        # Return amount of trapped water
        return ans