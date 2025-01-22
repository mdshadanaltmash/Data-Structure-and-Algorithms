def topological_dfs(adj_list, stack, visited, src):
    visited[src] = True
    for i in adj_list[src]:
        if not visited[i]:
            topological_dfs(adj_list, stack, visited, i)
    stack.append(src)

def topological_sort(adj_list, v):
    stack = []
    visited = [False] * v

    for i in range(v):
        if not visited[i]:
            topological_dfs(adj_list, stack, visited, i)
    
    while stack:
        print(stack.pop(), end="--->")

if __name__ == '__main__':
    v = 4
    adj_list = [[] for _ in range(v)]
    edges = [[0, 1], [1, 2], [3, 1], [3, 2]]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])
    
    topological_sort(adj_list, v)