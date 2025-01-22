from collections import deque

def bfs(adj_list, par, dist, S):
    print(f"Finding BFS from source {S}")
    
    q = deque()
    q.append(S)
    dist[S] = 0
    level = 0

    while q:
        node = q.popleft()
        for neighbour in adj_list[node]:
            if dist[neighbour] == float('inf'):
                par[neighbour] = node
                dist[neighbour] = dist[node] + 1
                q.append(neighbour)

def print_shortest_path(adj_list, S, D, V):
    par = [-1] * V
    dist = [float("inf")] * V

    bfs(adj_list, par, dist, S)

    if dist[D] == float('inf'):
        print(f'Destination {D} cannot be reached from source {S}')

    path = []
    curr_node = D
    path.append(curr_node)
    while par[curr_node] != -1:
        parent = par[curr_node]
        path.append(parent)
        curr_node = parent
    
    for i in range(len(path)-1, -1, -1):
        print(path[i], end="-->")



if __name__ == "__main__":
    # no. of vertices
    V = 8
    # Source and Destination vertex
    S, D = 2, 6
    # Edge list
    edges = [
        [0, 1], [1, 2], [0, 3], [3, 4],
        [4, 7], [3, 7], [6, 7], [4, 5],
        [4, 6], [5, 6]
    ]
    adj_list = [[] for _ in range(V)]

    for edge in edges:
        adj_list[edge[0]].append(edge[1])
        adj_list[edge[1]].append(edge[0])
    
    print_shortest_path(adj_list, S, D, V)