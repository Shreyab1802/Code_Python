# Question : https://leetcode.com/discuss/interview-question/4884549/Microsoft-OA

class Solution:
    def solution(self, R):
        N = len(R)
        M = len(R[0])
        total_cells = N * M  # Total number of cells in the grid
        visited = set()  # Set to store visited cells
        count = 0

        # Define directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        x, y = 0, 0  # Initial position
        dir = 0  # Initial direction: rightwards

        while len(visited) < total_cells:
            # Move until obstacle or boundary is encountered
            while 0 <= x < N and 0 <= y < M and R[x][y] != 'X':
                if (x, y) not in visited:
                    visited.add((x, y))
                    count += 1
                x += directions[dir][0]
                y += directions[dir][1]

            # Move back to the last valid position
            x -= directions[dir][0]
            y -= directions[dir][1]

            # Change direction (clockwise)
            dir = (dir + 1) % 4

            # Move forward in the new direction
            x += directions[dir][0]
            y += directions[dir][1]

            # If the robot revisits the starting position facing rightwards, break the loop
            if (x, y) == (0, 0) and dir == 0:
                break

        return count


# Example usage:
solution = Solution()
R = ["...X..", "....XX", "....."]
print(solution.solution(R))  # Output: 6





