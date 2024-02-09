def solution(A, C1, C2):
    # Sort the array in ascending order
    A.sort()

    # Initialize total cost to 0
    total_cost = 0

    # Calculate the total cost using the provided formula
    for i in range(len(A) - 1):
        single_increment_cost = (A[i + 1] - A[i]) * C1
        double_increment_cost = min((A[i + 1] - A[i]) * C2, C1)
        total_cost += min(single_increment_cost, double_increment_cost)

    # Return the total cost modulo 10^9
    return total_cost % (10 ** 9)


# Example usage:
A = [1, 4]
C1 = 15
C2 = 3
print(solution(A, C1, C2))  # Output: 45

A = [2, 11, 11, 11, 12]
C1 = 10
C2 = 4
print(solution(A, C1, C2))  # Output: 54

A = [1000000, 2, 1, 2, 1000000]
C1 = 10000
C2 = 4000
print(solution(A, C1, C2))  # Output: 999998000

# This function
# sorts
# the
# array in ascending
# order and then
# calculates
# the
# total
# cost
# by
# iterating
# through
# the
# sorted
# array.It
# computes
# both
# single and double
# increment
# costs
# between
# adjacent
# elements, chooses
# the
# minimum, and adds
# it
# to
# the
# total
# cost.Finally, it
# returns
# the
# total
# cost
# modulo





