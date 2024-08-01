from typing import List, Tuple
from collections import defaultdict

def most_repeated_substring(s: str, k: int) -> Tuple[str, int]:
    if k > len(s) or k == 0:
        return ("", 0)

    substring_count = defaultdict(int)
    max_count = 0
    most_repeated = ""

    for i in range(len(s) - k + 1):
        substring = s[i:i + k]
        substring_count[substring] += 1
        if substring_count[substring] > max_count:
            max_count = substring_count[substring]
            most_repeated = substring

    return (most_repeated, max_count)

# Example usage
s = "bananawwwwww"
k = 3
result = most_repeated_substring(s, k)
print(result)  # Output might be ('ana', 2)
