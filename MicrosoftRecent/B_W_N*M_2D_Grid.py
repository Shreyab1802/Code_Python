# You are presented with a two-dimensional grid of size N * M (N rows and M columns). Each cell in the grid is either black ("8") or white ("w"). A row or column is considered symmetric if it reads the same forwards as it does backward. For example, a row "BWwBWB" is symmetric whereas "wBws" isn't. The same symmetry criterion applies to columns. In one move, you can change the color in a single cell to the opposite. Your task is to determine the minimum number of moves required to make every row and column in the grid symmetric.
# Write a function:
# def solution (grid)
# that, given an array grid consisting of N strings, all of length M (each string is a single row of the grid), returns the minimum number of moves required to make all rows and columns symmetric.
# Examples:
# 1. Given grid = ["ввимв", "www", "swww"], the function should return 3. In the beginning, the grid appears as follows:
# Task 1
# 2
# 3
# Examples:
# 1. Given grid = ["awws", "wwwew", "Bwwww"], the function should return 3. In the beginning, the
# grid appears as follows:
# In 3 moves, we can change it to look like this:
# Task 1
# 2. Given grid = ["вив" the second example:
# "WBB'
# WEw"], the function should return 4.

import math
def minOperationToSymmetric(grid):
    n = len(grid)
    m = len(grid[0])
    totalCost = 0

    for ii in range(math.ceil(n / 2)):
        for jj in range(math.ceil(m / 2)):
            numBlack = 0
            numWhite = 0
            iis = [ii]
            jjs = [jj]
            if ii != n - 1 - ii: iis += [n - 1 - ii]
            if jj != m - 1 - jj: jjs += [m - 1 - jj]

            for i2 in iis:
                for j2 in jjs:
                    if grid[i2][j2] == 'B':
                        numBlack += 1
                    else:
                        numWhite += 1
            totalCost += min(numBlack, numWhite)
    return totalCost


vs = [
    ["BBWWB",
     "WWWBW",
     "BWWWW"],
    ["BWB",
     "WBB",
     "WBW"],
    ["BBBB",
     "WWWW",
     "BBWB",
     "WWWW"]
]

answer = [3, 4, 7]

for ii in range(len(vs)):
    alg = minOperationToSymmetric(vs[ii])
    ans = answer[ii]
    print(alg, ans)


