from collections import Counter


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counts = Counter(s).values()
        if len(s) % 2 == 0:
            return not any(count % 2 == 1 for count in counts)
        else:
            odds = [v for v in counts if v % 2 == 1]
            return len(odds) == 1