matrix = [[1, 2, 3, 4, 6],
           [5, 3, 8, 1, 2],
           [4, 6, 7, 5, 5],
           [2, 4, 8, 9, 4]]

rows = len(matrix)
cols = len(matrix[0])
def sum_submatrix(matrix, r,c,br,bc):
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if i in range(r,br+1) and j in range(c, bc+1):
                sum += matrix[i][j]


    return sum


print(sum_submatrix(matrix, 0,2,2,2))