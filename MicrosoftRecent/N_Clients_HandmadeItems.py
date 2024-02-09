def solution(T):
    total_time = 0
    current_time = 0
    total_duration = sum(T)

    for t in T:
        current_time += t
        total_time += current_time

    return total_time % 1000000000

# Test cases
# print(solution([3, 1, 2]))  # Output: 13
print(solution([1, 2, 3, 4]))  # Output: 24
print(solution([7, 7, 7]))  # Output: 60
print(solution([10000]))  # Output: 10000