class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        adjList = defaultdict(list) # node of neighbor and distance

        for src, dst, dist in roads:
            adjList[src].append((dst, dist))
            adjList[dst].append((src, dist))

        def dfs(i):
            if i in visited:
                return
            visited.add(i)

            nonlocal res

            for nei, dst in adjList[i]:
                res = min(res, dst)
                dfs(nei)


        res = float("inf")
        visited = set()
        dfs(1) #can start from any node

        return res