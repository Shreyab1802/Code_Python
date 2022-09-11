import collections

graph = { 'A' :['B', 'c' ,'d'] , 'B' : ['c'],'c' :['d'],'d':[]}

visited_nodes = set()

def bfs(graph, root):
    visited_nodes = set()
    queue = collections.deque([root])

    while queue:
        vertex = queue.popleft()
        visited_nodes.add(vertex)
        for i in graph[vertex]:
            if i not in visited_nodes:
                queue.append(i)
    print(visited_nodes)

bfs(graph,'A')