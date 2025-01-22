from collections import deque
from GraphList import add_edge, print_graph


def bfs(graph, source, visited=None):
    print()
    print(f"BFS starting from {source}: ")
    q = deque()
    if not visited:
        visited = [False] * len(graph) # marking all node(len of graph) unvisited initially
    visited[source] = True
    q.append(source)

    while q:
        curr = q.popleft()
        print(curr, end="-->")
        for node in graph[curr]:
            if not visited[node]:
                visited[node] = True
                q.append(node)

def bfs_disconnected(graph):
    visited = [False] * len(graph) # marking all node(len of graph) unvisited initially
    
    for i in range(len(graph)):
        if not visited[i]:
            bfs(graph, i, visited)




if __name__ == '__main__':
    vertices = 6
    graph = [[] for _ in range(vertices)]

    add_edge(graph, 0, 1)
    add_edge(graph, 0, 2)
    add_edge(graph, 1, 3)
    add_edge(graph, 1, 4)
    add_edge(graph, 2, 4)
    add_edge(graph, 5, 5)

    print_graph(graph)
    bfs(graph, 0)
    bfs_disconnected(graph)

    """
    0<-->1<-->3,4
    0<-->2<-->4
    5
    """
