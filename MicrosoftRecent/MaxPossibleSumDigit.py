# You are given a string S made of N digits that represents a positive integer.
# Among all positive integers smaller than S, find the one with the maximum possible sum of digits. If there is more than one such integer, return any of them. The returned string can only consist of digits and may not contain leading zeros.
# Examples:
#
# Given S = "899", one of the possible correct answers is "898".
# Given S = 10", the only possible correct answer is "9".
# Given S = "98", the only possible correct answer is "89".
# Write an efficient algorithm for the following assumptions:
# • N is an integer within the range [2., 100,000];
# • string S is made only of digits (0-9);
# • S does not contain leading zeros.
# I have tried but coudn't get better solution than brute force. Is there any optimal way to do this?





class Solution:

    def maxPossibleSumDigit(self, s):
        res = ""
        if s[0] != '1':
            res += str(int(s[0]) - 1)
        for ii in range(1, len(s)):
            res += '9'
        return res

# Example usage
sol = Solution()
print(sol.maxPossibleSumDigit("899"))  # Output: "899"
print(sol.maxPossibleSumDigit("10"))   # Output: "9"
print(sol.maxPossibleSumDigit("98"))   # Output: "89"
