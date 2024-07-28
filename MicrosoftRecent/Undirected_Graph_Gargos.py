# u r given an undirected graph consisting of N vertices, numbered from 1 to
# N and M edges. The graog us described by two arrays, A and B both of length M.
# A pair (A[K],B[K]) for k from 0 to M-1. describes edge between vertex A[K] and bertex B[k] ur task is to
# check whether the given graph contains a path from vertex 1 to vertex N going through all the vertices one by one
# in increasin order of their numbers. All connections on the path should be direct. example
# Given N =4, A=[1,2,4,4,3] and B=[2,3,1,3,1] t he function should return true. there is a path 1-2-3-4 using the
# edges (1,2)(2,3)and (4,3)


class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __eq__(self, other):
        return (self.v1 == other.v1 and self.v2 == other.v2)

    def __hash__(self):
        return hash((self.v1, self.v2))

def solution(edges, N):
    cur_vertex = 1
    while cur_vertex < N:
        if Edge(cur_vertex, cur_vertex + 1) not in edges:
            break
        cur_vertex += 1
    return cur_vertex == N

# Example usage
edges = {Edge(1, 2), Edge(2, 3), Edge(3, 4)}
N = 4
print(solution(edges, N))  # Output: True

edges = {Edge(1, 2), Edge(2, 3)}
N = 4
print(solution(edges, N))  # Output: False
