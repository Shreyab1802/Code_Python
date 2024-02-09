def total_horizontal_strikes(heights):
    n = len(heights)
    ans = heights[0]
    for i in range(1, n):
        diff = heights[i] - heights[i - 1]
        if diff > 0:
            ans += diff
    return ans

assert total_horizontal_strikes([1, 3, 2, 1, 2, 1, 5, 3, 3, 4, 2]) == 9