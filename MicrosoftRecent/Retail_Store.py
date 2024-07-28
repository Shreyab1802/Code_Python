# A retail store chain wants to expan into new neighbourhood.
# To make the number of clients as larget as possible, the new branch should be at a
# distance of no more than K from all the houses in the neighborhood. A is the matrix of size N * M.
# it represents the neighbourhood as a rectrangular grid,
# in which each cell is an integer 0(an empty plot) and 1(a house) the distance between two
# cells is calculated as the min number of a cell borders that one has to cross to move
# from the source cell to target cell. it doesnt matter whether the cells on the way are empty or
# occupied but it doesnt allow for moving through corners.
# A store an b built on an empty plot. How many suitable locations are there ? Eg: given K= 2
# and matrix A=[[0,0,0,0][0,0,1,0][1,0,0,1]] houses are located in the cells
# with coordinates (2,3)(3,1) and (3,4) we can build a new store on two empty plots that are close
# enough to all the houses the first possible empty plot is located at(3,2) the distance to
# first house at(2,3) is 2. The distance to second house at(3,1) is 1 and third house at(3,4)
# distance is 2. The second possible empty plot is located at (3,3). The distance to the first,
# second and third hoursed are 1,2,1 given the positive integer K and matrix A of size N*M
# return the number of empty plots close enough to all the houses Eg: K=2 A=[[0,0,0,0][0,0,1,0][1,0,0,1]]
# function should return 2

def solution(K, A):
    def manhattan_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    N = len(A)
    M = len(A[0])
    houses = []

    # Identify all house coordinates
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                houses.append((i, j))

    suitable_locations = 0

    # Check all empty plots
    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                all_within_k = True
                for hx, hy in houses:
                    if manhattan_distance(i, j, hx, hy) > K:
                        all_within_k = False
                        break
                if all_within_k:
                    suitable_locations += 1

    return suitable_locations


# Example usage
K = 2
A = [
    [0, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1]
]
print(solution(K, A))  # Output: 2
