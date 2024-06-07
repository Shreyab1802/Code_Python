class Solution:
    def breakPalindrome(self, palindrome: str) -> str:

        # WITHOUT EXTRA SPACE

        # instead of using extra space for 'st'
        # what was corner case was that 'aba'
        # when we changed b it became palindrome 'aaa'
        # so with using extra space we had to check if it was palindrom or not
        # but if we just check upto half of that string we could avoid that condition
        # as it will conclude either that if we traverse upto half and no change is there
        # it means either whole string is 'aaaa' or middle character is non-'a'
        # in both case we have to change then last character only

        # so we can ignore the condition with just taking loop upto n//2-1
        # and remove that st and its palindrome check

        n = len(palindrome)

        if n == 1: return ''

        for i in range(n // 2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i + 1:]

        # if conditions are 'aabaa' or 'aaaa' change last character with b
        return palindrome[:-1] + 'b'
