class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        currLength, maxLength = 0, 0
        chars = ''

        for i in range(len(s)):
            if s[i] in chars:
                chars = chars[chars.find(s[i]) + 1:]

            chars += s[i]
            currLength = len(chars)

            if currLength > maxLength:
                maxLength = currLength

        return maxLength