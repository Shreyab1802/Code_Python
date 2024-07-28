# There are N holes arranged in a row in the top of an old table. We want to fix the table by covering the holes with two boards. For technical reasons, the boards need to be of the same length.
# The position of the K-th hole is A[K]. What is the shortest length of the boards required to cover all the holes? The length of the boards has to be a positive integer. A board of length L, set at position X, covers all the holes located between positions X and X+L (inclusive). The position of every hole is unique.
# Write a function:
# class Solution { public int solution(int[] A); }
# which, given an array A of integers of length N, representing the positions of the holes in the table, returns the shortest board length required to cover all the holes.
# Examples:
# 1. Given A = [11, 20, 15], your function should return 4. The first board
# would cover the holes in positions 11 and 15, and the second board the hole at position 20.
# 2. Given A = [15, 20, 9, 11], your function should return 5. The first board
# covers the holes at positions 9 and 11, and the second one the holes in positions 15 and 20.
# Task 3
# Programming Language
# Select language
# Java 8
# English
# which, given an array A of integers of length N, representing the positions of the holes in the table, returns the shortest board length required to cover all the holes.
# Examples:
# 1. Given A = [11, 20, 15), your function should return 4. The first board
# would cover the holes in positions 11 and 15, and the second board the hole at position 20.
# 2. Given A = [15, 20, 9, 11], your function should return 5. The first board
# covers the holes at positions 9 and 11, and the second one the holes in positions 15 and 20.
# 3. Given A = [0, 44, 32, 30, 42, 18, 34, 16, 35), your function should return
# 18. The first board would cover the holes in positions between 0 and 18, and the second the positions between 30 and 44.
# 4. Given A = [9], your function should return 1.
# Write an efficient algorithm for the following assumptions:
# • N is an integer within the range [1..100,000);
# • each element of array A is an integer within the range [0.. 1,000,000,000);


def solution(A):
    def can_cover_all_with_length(L):
        # Start with the first board
        count = 1
        first_hole = A[0]

        for position in A:
            if position > first_hole + L:
                # Need to use another board
                count += 1
                first_hole = position
                if count > 2:
                    return False
        return True

    if len(A) == 1:
        return 1

    # Sort the positions of the holes
    A.sort()

    # Define the binary search range
    left = 1
    right = A[-1] - A[0]

    while left < right:
        mid = (left + right) // 2
        if can_cover_all_with_length(mid):
            right = mid
        else:
            left = mid + 1

    return left


# Example test cases
print(solution([11, 20, 15]))  # Output: 4
print(solution([15, 20, 9, 11]))  # Output: 5
print(solution([0, 44, 32, 30, 42, 18, 34, 16, 35]))  # Output: 18
print(solution([9]))  # Output: 1
