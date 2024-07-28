# you are given a string s and a two-dimensional array of characters of size NxN named grid.
# Each field in the grid is either empty (denoted by a dot ".") or contains an uppercase English lettwer.
# Each particular letter may appear at most twice in the grid.
# your task is to reconstruct string s by visiting fields of the grid.
# You start thr reconstruction with an empty string. you can choose the field in which you want to start.
# in one move you can change the current field to an adjacent one (up, down, left, right)
# if you visit a field containing a letter, you may append this letter to thhe end of the reconstructed
# string. Appending a letter is not counted as a move. Each field can be visited and each letter can be
# used multiple times during the reconstruction process. what is the minimum moves needed to reconstruct string S
#
# ('ABCA', ['.A.C', '.B..', '....', '...A']) return 6
# ('XZZY', ['.Z.', 'XBB', '..A']) return -1


from collections import deque, defaultdict


class Solution:
    def min_moves_to_reconstruct_string(self, s, grid):
        n = len(grid)

        # Function to get all positions of a character in the grid
        def get_positions(char):
            positions = []
            for i in range(n):
                for j in range(len(grid[i])):
                    if grid[i][j] == char:
                        positions.append((i, j))
            return positions

        # Function to perform BFS to find shortest path between two positions in the grid
        def bfs(start, target):
            queue = deque([start])
            visited = set()
            visited.add(start)
            moves = 0

            while queue:
                for _ in range(len(queue)):
                    x, y = queue.popleft()
                    if (x, y) == target:
                        return moves
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                            visited.add((nx, ny))
                            queue.append((nx, ny))
                moves += 1
            return float('inf')

        # Get all positions of the characters in the string s
        char_positions = defaultdict(list)
        for char in s:
            positions = get_positions(char)
            if not positions:
                return -1
            char_positions[char].extend(positions)

        # Initialize variables to store the minimum moves
        total_moves = 0
        current_positions = get_positions(s[0])

        for i in range(1, len(s)):
            next_positions = char_positions[s[i]]
            min_moves = float('inf')
            for start in current_positions:
                for target in next_positions:
                    min_moves = min(min_moves, bfs(start, target))
            if min_moves == float('inf'):
                return -1
            total_moves += min_moves
            current_positions = next_positions

        return total_moves


# Example usage
sol = Solution()
print(sol.min_moves_to_reconstruct_string('ABCA', ['.A.C', '.B..', '....', '...A']))  # Output: 6
print(sol.min_moves_to_reconstruct_string('XZZY', ['.Z.', 'XBB', '..A']))  # Output: -1
