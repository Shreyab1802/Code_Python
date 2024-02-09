def count_repeated_chars(s):
    count = 0
    for i in range(len(s) - 1):
        if s[i].islower() and s[i+1].isupper():
            count += 1
    return count

# Example usage:
input_str = 'xyzxyzwXYZWBC'
result = count_repeated_chars(input_str)
print("Number of repeated characters in the pattern lowercase followed by uppercase:", result)