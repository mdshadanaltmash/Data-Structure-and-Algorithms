from collections import deque
from GraphList import add_edge, print_graph


def dfs_rec(graph, visited, source):
    visited[source] = True
    print(source, end="-->")

    for i in graph[source]:
        if not visited[i]:
            dfs_rec(graph, visited, i)

def dfs(graph, source):
    visited = [False] * len(graph)
    dfs_rec(graph, visited, source)



if __name__ == "__main__":
    V = 5

    # Create an adjacency list for the graph
    adj = [[] for _ in range(V)]

    # Define the edges of the graph
    edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

    # Populate the adjacency list with edges
    for e in edges:
        add_edge(adj, e[0], e[1])

    source = 1
    print("DFS from source:", source)
    dfs(adj, source)