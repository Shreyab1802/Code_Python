class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_Map = {i: 0 for i in s}

        start = 0
        max_frequency = 0

        for end in range(len(s)):
            freq_Map[s[end]] += 1

            max_frequency = max(max_frequency, max(freq_Map.values()))

            is_valid = end - start + 1 - max_frequency <= k

            if not is_valid:
                freq_Map[s[start]] -= 1
                start += 1

        return (end - start + 1)