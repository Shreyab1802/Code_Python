# Nested Sliding Windows: Use nested sliding windows to extract substrings of every possible length from 1 to the length of the string.
# Hash Map: Use a hash map (dictionary) to keep track of the count of each substring.
# # Track Maximum: Keep track of the substring with the highest count.

from collections import defaultdict
from typing import Tuple

def most_occurring_substring(s: str) -> Tuple[str, int]:
    if not s:
        return ("", 0)

    substring_count = defaultdict(int)
    max_count = 0
    most_occurring = ""

    n = len(s)
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            substring_count[substring] += 1
            if substring_count[substring] > max_count:
                max_count = substring_count[substring]
                most_occurring = substring

    return (most_occurring, max_count)

# Example usage
s = "banana"
result = most_occurring_substring(s)
print(result)  # Output might be ('a', 3) or ('an', 2) or ('na', 2)
