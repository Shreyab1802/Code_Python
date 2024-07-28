# A map of a village is split into a rectangular grid with N rows (numbered from 0 to N-1) and M columns (numbered from 0 to
# M-1). Establish at most two rice cultivation areas in the village, using only cells dedicated to this purpose.
# The map is described by an array of strings: the C-th character of the R-th string can be either'., meaning that the square of land in the R-th row and C-th column is a place where rice cultivation can be established, or '# if it is an agricultural building.
# The shape of the cultivation areas should be a narrow rectangle (vertical with one cell width or horizontal with one cell height).
# The areas cannot share cells, but can share a side.
# What is the maximum number of cells that can be used for cultivation by choosing at most two areas?
# Write a function:
# class Solution { public int solution(String[] A); ›
# that, given an array of strings A, returns an integer: the maximum number of cells that can be used for cultivation by choosing at most two areas.
# Examples:
# 1. Given A = [".##..",'.#.#.,"
# ".....*, *##. #*], the function should return 7. An example placement of cultivation areas is shown
# in the diagram below.
# 2. Given A = [*#.#*
# *,*#.#*], the function should return 4.
# 3. Given A = ["###..'
# ・・・・・
# *, "###.#*], the function should return 7.
# Write an efficient algorithm for the following assumptions:
# • N is an integer within the range [1..500];
# • all strings in A are of the same length M within the range [1..500];
# • all strings in A consist only of the characters*.' and/or '#.



class Solution:
    def solution(self, A):
        N = len(A)
        M = len(A[0])

        max_area = 0
        all_areas = []

        # Find all vertical rectangles
        for c in range(M):
            start = None
            for r in range(N):
                if A[r][c] == '.':
                    if start is None:
                        start = r
                else:
                    if start is not None:
                        all_areas.append((start, c, r - 1, c))
                        start = None
            if start is not None:
                all_areas.append((start, c, N - 1, c))

        # Find all horizontal rectangles
        for r in range(N):
            start = None
            for c in range(M):
                if A[r][c] == '.':
                    if start is None:
                        start = c
                else:
                    if start is not None:
                        all_areas.append((r, start, r, c - 1))
                        start = None
            if start is not None:
                all_areas.append((r, start, r, M - 1))

        # Calculate sizes of all areas
        def area_size(r1, c1, r2, c2):
            return (r2 - r1 + 1) * (c2 - c1 + 1)

        all_areas = [(r1, c1, r2, c2, area_size(r1, c1, r2, c2)) for (r1, c1, r2, c2) in all_areas]
        all_areas.sort(key=lambda x: -x[4])  # Sort areas by size in descending order

        # Find the two largest non-overlapping areas
        def is_non_overlapping(a, b):
            ar1, ac1, ar2, ac2, _ = a
            br1, bc1, br2, bc2, _ = b
            return ar2 < br1 or ar1 > br2 or ac2 < bc1 or ac1 > bc2

        for i in range(len(all_areas)):
            max_area = max(max_area, all_areas[i][4])
            for j in range(i + 1, len(all_areas)):
                if is_non_overlapping(all_areas[i], all_areas[j]):
                    max_area = max(max_area, all_areas[i][4] + all_areas[j][4])
                    break

        return max_area


# Test cases
solution_instance = Solution()
print(solution_instance.solution([".##..", ".#.#.", ".....", "##.#."]))  # Output: 7
print(solution_instance.solution(["#.#.", "#.#."]))  # Output: 4
print(solution_instance.solution(["###..", ".....", "###.#"]))  # Output: 7
