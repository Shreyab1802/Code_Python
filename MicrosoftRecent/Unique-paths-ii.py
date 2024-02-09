from typing import List


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # calculate dp for first row
        dp = [1 if not grid[0][0] else 0]
        for j in range(1, len(grid[0])):
            dp.append(dp[j - 1] if not grid[0][j] else 0)
        # iteratively update it for remaining rows
        for i in range(1, len(grid)):
            dp[0] = dp[0] if not grid[i][0] else 0
            for j in range(1, len(grid[i])):
                dp[j] = dp[j] + dp[j - 1] if not grid[i][j] else 0
        return dp[-1]