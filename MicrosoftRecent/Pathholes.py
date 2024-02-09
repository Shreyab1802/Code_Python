def solve(n, s, b):
    consecutivePotholesCount = []
    curr = 0
    for i in s:
        if i == 'x':
            curr += 1
        else:
            if curr > 0:
                consecutivePotholesCount.append(curr)
            curr = 0
    if curr > 0:
        consecutivePotholesCount.append(curr)

    consecutivePotholesCount.sort(reverse=True)
    ans = 0
    for i in consecutivePotholesCount:
        if i + 1 <= b:
            ans += i
            b -= (i + 1)
        else:
            ans += max(0, b - 1)
            break
    return ans

print(solve(17, "...xxx..x....xxx.", 7)) # ans = 5
print(solve(7, "..xxxxx", 4))  # ans  = 3
print(solve(11, "x.x.xxx...x", 14)) # ans = 6
print(solve(2, "..", 5)) # ans = 0