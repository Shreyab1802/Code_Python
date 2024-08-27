def match_with_dot(s1, s2):
    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] != '.' and s1[i] != s2[i]:
            return False

    return True


def match_with_digit(s1, s2):
    i, j = 0, 0

    while i < len(s1) and j < len(s2):
        if s1[i].isdigit():
            n = int(s1[i])  # Convert the digit to an integer
            i += 1
            j += n  # Skip `n` characters in s2
        elif s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            return False

    # Both strings should be fully traversed for a successful match
    return i == len(s1) and j == len(s2)

print(match_with_dot("r.kt", "rokt"))  # True
print(match_with_dot("r.k", "rokt"))   # False

print(match_with_digit("i12","international"))
