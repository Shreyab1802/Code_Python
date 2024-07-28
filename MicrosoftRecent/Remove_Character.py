# https://leetcode.com/discuss/interview-question/5322819/microsoft-online-assessment-sde-2/2462401

class Solution:
    def solution(self, S: str) -> str:
        smallest = S[1:]  # Initialize the smallest string with the first character removed
        for i in range(1, len(S)):
            current = S[:i] + S[i+1:]  # Create a new string with the ith character removed
            if current < smallest:
                smallest = current  # Update the smallest string if the current string is smaller
        return smallest

# Example usage:
solution_instance = Solution()

print(solution_instance.solution("abczd"))  # Expected Output: "abzd"
print(solution_instance.solution("acb"))    # Expected Output: "ab"
print(solution_instance.solution("abcdef")) # Expected Output: "abcde"
