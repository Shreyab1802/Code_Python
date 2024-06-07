class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if n == 1:
            return 1

        components = 0
        visited = set()

        graph = {node: [] for node in range(n)}

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        def dfs(node):
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    dfs(neighbour)

        for node in graph:
            if node in visited:
                continue
            else:
                visited.add(node)
                components += 1
                dfs(node)

        return components


