# Given four digits, count how many valid times can be displayed on a digital clock (in 24-hour format) using those digits. The earliest time is 00:00 and the latest time is 23:59.
# Write a function:
# class Solution ( public int solution(int A, int B, int C, int D); } that, given four integers A, B, C and D
# (describing the four digits), returns the number of valid times that can be displayed on a digital clock.
# Examples:
# 1. Given A = 1, B = 8, C = 3, D = 2, the function should return 6. The valid times are: 12:38, 13:28,
# 18:23, 18:32, 21:38 and 23:18.
# 2. Given A = 2, B = 3, C = 3, D = 2, the function should return 3. The valid times are: 22:33, 23:23 and 23:32.
# 3. Given A = 6, B = 2, C = 4, D = 7, the function should return 0. It is not possible to display any valid
# time using the given digits.
# Assume that
# • A, B, C and D are integers within the range [0.9).
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
# Copyright 2009-2024 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.

from itertools import permutations

class Solution:
    def solution(self, A, B, C, D):
        digits = [A, B, C, D]
        valid_times = set()

        # Generate all permutations of the four digits
        for perm in permutations(digits):
            hour = perm[0] * 10 + perm[1]
            minute = perm[2] * 10 + perm[3]

            # Check if the permutation forms a valid time
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                valid_times.add((hour, minute))

        # Return the count of unique valid times
        return len(valid_times)


# Test examples
sol = Solution()
print(sol.solution(1, 8, 3, 2))  # Should return 6
print(sol.solution(2, 3, 3, 2))  # Should return 3
print(sol.solution(6, 2, 4, 7))  # Should return 0