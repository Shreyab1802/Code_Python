# Python program to check if it is possible to reach
# (a, b) from (x, y).
# Returns GCD of i and j
def gcd(i, j):
    if (i == j):
        return i

    if (i > j):
        return gcd(i - j, j)
    return gcd(i, j - i)


# Returns true if it is possible to go to (a, b)
# from (x, y)
def ispossible(x, y, a, b):
    # Find absolute values of all as sign doesn't
    # matter.
    x, y, a, b = abs(x), abs(y), abs(a), abs(b)

    # If gcd is equal then it is possible to reach.
    # Else not possible.
    return (gcd(x, y) == gcd(a, b))