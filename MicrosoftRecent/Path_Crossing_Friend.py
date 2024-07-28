# https://leetcode.com/discuss/interview-question/5456465/Microsoft-OA


######################
# You want to visit your friend, who lives abroad. It is time to plan the whole journey, both there and back. The trip will be long, so you would like to make it interesting. You do not want to revisit the same places or go along the same paths twice. Also, you do not have much time, so you do not want to head back from any point.
# You will represent your planned path by a string containing four letters: 'N' for north, 'S' for south, 'E for east and W' for west. For example, a path going north, east, east, north, west, south would be notated as "NEENWS".
# You have already made a plan of the outward part of your journey. How will you plan the shortest path back home, fulfilling the criteria described above?
# Write a function:
# class Solution & public String solution(String forth): ›
# that, given a string forth of length N, which denotes the path leading to your friend, returns one of the shortest possible paths back home and fulfils the above conditions. You can assume that you are heading north at both the beginning and the end of the first part of your journey (the first and the last element in forth are equal to 'N'). Moreover, forth does not contain any occurrence of the letter 'S.
# Examples:
# 1. Given forth = 'NEENWN", your function may return "WWSSSE*. It may also return "WSWSSE".
#
# 2. Given forth = 'NWNENWNEN", your function may return "ESSSSSW.
# 几
# 3. Given forth = 'NENENWWWWN*, your function may return "WSSSSEEE.
#
# Write an efficient algorithm for the following assumptions:
# • N is an integer within the range 2.100,000);
# • string forth consists only of the following characters: "N, E and/or W:
# • forth[e] = forth[N-1] = 'N;
# • route designated by forth never goes along the same path

# class Solution:
#     def solution(self, forth):
#         # Initialize the return path string
#         back = []
#
#         # Iterate over the reversed `forth` string and swap directions
#         for direction in reversed(forth):
#             if direction == 'N':
#                 back.append('S')  # North becomes South
#             elif direction == 'S':
#                 back.append('N')  # South becomes North
#             elif direction == 'E':
#                 back.append('W')  # East becomes West
#             elif direction == 'W':
#                 back.append('E')  # West becomes East
#
#         # Join the list to form the final string
#         return ''.join(back)
#
#
# # Example usage:
# solution_instance = Solution()
# forth = "NEENWN"
# print(solution_instance.solution(forth))  # Expected Output: "WWSSSE" or "WSWSSE"
#
# forth = "NWNENWNEN"
# print(solution_instance.solution(forth))  # Expected Output: "ESSSSSW"
#
# forth = "NENENWWWWN"
# print(solution_instance.solution(forth))  # Expected Output: "WSSSSEEE"

##### Solution 2 ##########


# from collections import deque
#
#
# class Solution:
#     def __init__(self):
#         # Define the movements for each direction
#         self.map = {'N': (-1, 0), 'W': (0, -1), 'E': (0, 1), 'S': (1, 0)}
#         # Define the reverse movements for returning
#         self.reverse_map = {'N': 'S', 'W': 'E', 'E': 'W', 'S': 'N'}
#         # Placeholder for the visited grid
#         self.vis = None
#
#     def solution(self, forth):
#         n = len(forth)
#         # Initialize the visited grid
#         self.vis = [[0] * (2 * n + 1) for _ in range(2 * n + 1)]
#         start = [n, n]  # Start at the center of the grid
#         # Populate the grid with the path taken to the destination
#         destination = self.populate_graph(forth, start)
#         # Find the shortest path back to the start
#         return self.find_shortest_path(start, destination)
#
#     def populate_graph(self, s, curr):
#         r, c = curr
#         self.vis[r][c] = 1  # Mark the start as visited
#         for l in s:
#             next_move = self.map[l]
#             r += next_move[0]
#             c += next_move[1]
#             self.vis[r][c] = 1  # Mark the path as visited
#         #print(f"Grid after populate_graph: {self.vis}")  # Debug statement
#         return [r, c]
#
#     def find_shortest_path(self, start, destination):
#         q = deque()
#         q.append((destination, ""))
#         vis_local = [[0] * len(self.vis[0]) for _ in range(len(self.vis))]
#         vis_local[destination[0]][destination[1]] = 1
#
#         while q:
#             pos, path = q.popleft()
#             if pos[0] == start[0] and pos[1] == start[1]:
#                 #print(f"Path found: {path}")  # Debug statement
#                 return path  # Return the first found shortest path
#             r, c = pos
#
#             for key, move in self.reverse_map.items():
#                 d = self.map[move]
#                 new_r, new_c = r + d[0], c + d[1]
#                 if 0 <= new_r < len(self.vis) and 0 <= new_c < len(self.vis[0]) and self.vis[new_r][new_c] == 1 and \
#                         vis_local[new_r][new_c] == 0:
#                     q.append(([new_r, new_c], path + key))
#                     vis_local[new_r][new_c] = 1
#                     #print(f"Queue state: {q}")  # Debug statement
#         return ""
#
#
# # Example usage
# solution_instance = Solution()
#
# # Test cases
# forth1 = "NEENWN"
# output1 = solution_instance.solution(forth1)  # Expected Output: "WWSSSE" or "WSWSSE"
# print(f"Output for {forth1}: {output1}")
#
# forth2 = "NWNENWNEN"
# output2 = solution_instance.solution(forth2)  # Expected Output: "ESSSSSW"
# print(f"Output for {forth2}: {output2}")
#
# forth3 = "NENENWWWWN"
# output3 = solution_instance.solution(forth3)  # Expected Output: "WSSSSEEE"
# print(f"Output for {forth3}: {output3}")


#### solution 3


from collections import deque

class Solution:
    def min(self, a, b):
        return a if a < b else b

    def max(self, a, b):
        return a if a > b else b

    def solution(self, s: str) -> str:
        w = 0
        e = 0
        n = 0

        for char in s:
            if char == 'N':
                n += 1
            if char == 'W':
                w += 1
            if char == 'E':
                e += 1

        left = -1 - 2 * w
        right = 1 + 2 * e
        up = n + 1

        r = up
        c = right - left

        sx = n
        sy = -left

        vis = [[False for _ in range(c)] for _ in range(r)]

        vis[sx][sy] = True
        ex = sx
        ey = sy

        for char in s:
            if char == 'N':
                sx -= 1
            if char == 'W':
                sy -= 1
            if char == 'E':
                sy += 1
            vis[sx][sy] = True

        q = deque()
        q.append((sx, sy))
        parent = {(sx, sy): (-1, -1)}

        while q:
            x, y = q.popleft()

            directions = [(1, 0), (0, -1), (0, 1)]

            for dx, dy in directions:
                x1 = x + dx
                y1 = y + dy

                if 0 <= x1 < r and 0 <= y1 < c:
                    if not vis[x1][y1]:
                        parent[(x1, y1)] = (x, y)
                        vis[x1][y1] = True
                        q.append((x1, y1))
                    elif x1 == ex and y1 == ey:
                        res = ""
                        px, py = x, y

                        while px != -1 or py != -1:
                            dx = px - x1
                            dy = py - y1

                            if dx == -1:
                                res += 'S'
                            else:
                                if dy == 1:
                                    res += 'W'
                                else:
                                    res += 'E'

                            x1, y1 = px, py
                            px, py = parent[(x1, y1)]

                        return res[::-1]

# Example usage:
solution_instance = Solution()

forth = "NEENWN"
print(solution_instance.solution(forth))  # Expected Output: "WWSSSE" or "WSWSSE"

forth = "NWNENWNEN"
print(solution_instance.solution(forth))  # Expected Output: "ESSSSSW"

forth = "NENENWWWWN"
print(solution_instance.solution(forth))  # Expected Output: "WSSSSEEE"




