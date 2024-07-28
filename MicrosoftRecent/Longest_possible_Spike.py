# https://leetcode.com/discuss/interview-question/5213610/Microsoft-OA-May

class Solution:
    def solution(self, A):
        if not A:
            return 0

        max_val = max(A)
        element_count = {}

        for num in A:
            if num in element_count:
                if num != max_val and element_count[num] < 2:
                    element_count[num] += 1
            else:
                element_count[num] = 1

        res = 1  # Start with 1 for the maximum value

        for num, count in element_count.items():
            if num != max_val:
                res += count

        return res


# Example usage
solution_instance = Solution()
print(solution_instance.solution([1, 2, 2, 3, 4]))  # Output: 5
print(solution_instance.solution([5, 5, 5, 5]))  # Output: 1
print(solution_instance.solution([]))  # Output: 0
print(solution_instance.solution([1]))  # Output: 1
print(solution_instance.solution([1, 2, 3, 4, 5]))  # Output: 5
print(solution_instance.solution([1, 2]))  # Output: 2
print(solution_instance.solution([2,5,3,2,4,1]))  # Output: 6
