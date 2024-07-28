from typing import List
import collections

def getFood(self, grid: List[List[str]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    queue = collections.deque()
    visited = set()

    # Identify the starting location
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "*":
                queue.append((i, j, 0))  # 3rd parameter is the steps taken
                visited.add((i, j))
                break
        else:
            continue
        break

    # Define directions for movement
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

    while queue:
        curr_row, curr_col, steps = queue.popleft()

        if grid[curr_row][curr_col] == "#":
            return steps

        for row_inc, col_inc in directions:
            new_row = curr_row + row_inc
            new_col = curr_col + col_inc

            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != "X":
                if (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))

    return -1
