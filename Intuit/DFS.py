graph = { 'A' :['B', 'c' ,'d'] , 'B' : ['c'],'c' :['d'],'d':[]}

visited_nodes = set()

def dfs(graph, visited_nodes, root):
    if root not in visited_nodes:
        visited_nodes.add(root)
        print(visited_nodes)
        for neighbour in graph[root]:
            dfs(graph,visited_nodes,neighbour)
    print(visited_nodes)

dfs(graph,visited_nodes,'A')
