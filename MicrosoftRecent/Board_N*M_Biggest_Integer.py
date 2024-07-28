# https://leetcode.com/discuss/interview-question/5079053/Microsoft-Codilti-Test

# You are given a board of N rows and M columns. Each field of the board contains a single digit (0−9).
#
# You want to find a path consisting of four neighboring fields. Two fields are neighboring if
# they share a common side. Also, the fields in your path should be distinct (you can't visit the same field twice).
#
# The four digits of your path, in the order in which you visit them, create an integer.
# What is the biggest integer that you can achieve in this way?
#
# Write a function
#
# class Solution { public int solution(int[][] Board); }
#
# that, given the board represented as a matrix of integers consisting of N rows and M columns,
# returns the biggest integer that you can achieve when concatenating the values in a path of length four.
#
# Examples:
#
# Given the following board (N=3, M=5):
# the function should return 9121. You can choose either
# of the following paths (the first field is denoted by red):

class Solution:
    def __init__(self):
        self.ans = 0
        self.board = []
        self.m = 0
        self.n = 0
        self.len = 4
        self.maxPos = [0] * self.len
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def biggest(self, b):
        self.ans = 0
        self.board = b
        self.m = len(self.board)
        self.n = len(self.board[0])
        self.len = 4
        self.maxPos = [0] * self.len

        for r in range(self.m):
            for c in range(self.n):
                self.dfs(r, c, 0, 0)

        return self.ans

    def dfs(self, r, c, pos, cur):
        if r < 0 or r >= self.m or c < 0 or c >= self.n or self.board[r][c] == -1:
            return

        cur = cur * 10 + self.board[r][c]
        if self.maxPos[pos] > cur:
            return

        self.maxPos[pos] = cur
        if pos == self.len - 1:
            if cur > self.ans:
                self.ans = cur
            return

        temp = self.board[r][c]
        self.board[r][c] = -1
        for dir in self.dirs:
            newR = dir[0] + r
            newC = dir[1] + c
            self.dfs(newR, newC, pos + 1, cur)
        self.board[r][c] = temp


# Example usage:
sol = Solution()
board = [
    [9, 2, 3, 1, 1],
    [6, 8, 1, 0, 2],
    [5, 4, 7, 6, 5]
]
print(sol.biggest(board))  # Expected Output: 9121

