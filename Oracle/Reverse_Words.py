class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()[::-1]
        reverseString = " "

        for each in words:
            print(each)
            reverseString += each + " "

        print(words)
        return reverseString.strip()