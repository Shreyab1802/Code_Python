def most_repeated_substring(s: str, k: int) -> str:
    if k > len(s) or k <= 0:
        return ""

    substring_count = {}
    max_count = 0
    most_repeated = ""

    # Initial substring and count
    current_substring = s[:k]
    substring_count[current_substring] = 1

    for i in range(1, len(s) - k + 1):
        # Slide the window by removing the first character and adding the next character
        current_substring = current_substring[1:] + s[i + k - 1]

        if current_substring in substring_count:
            substring_count[current_substring] += 1
        else:
            substring_count[current_substring] = 1

        # Update the most repeated substring if necessary
        if substring_count[current_substring] > max_count:
            max_count = substring_count[current_substring]
            most_repeated = current_substring

    return most_repeated


# Example usage
s = "ababcbabc"
k = 2
print(most_repeated_substring(s, k))  # Output: "ab"
