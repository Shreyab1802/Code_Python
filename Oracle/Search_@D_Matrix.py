class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        r = len(matrix)
        c = len(matrix[0])

        left = 0
        right = r * c - 1

        while left <= right:
            mid_index = (left + right) // 2

            mid_element = matrix[mid_index // c][mid_index % c]

            if target == mid_element:
                return True
            elif target < mid_element:
                right = mid_index - 1

            else:
                left = mid_index + 1

        return False
