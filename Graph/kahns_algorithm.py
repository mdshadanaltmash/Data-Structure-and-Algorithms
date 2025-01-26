from collections import deque
def topo_sort(adj_list, n):
    in_deg_arr = [0] * n

    for i in range(n):
        for edge in adj_list[i]:
            in_deg_arr[edge] += 1
    queue = deque()
    for v, deg in enumerate(in_deg_arr):
        if deg == 0:
            queue.append(v)
    
    results = []
    while queue:
        curr = queue.popleft()
        results.append(curr)
        for node in adj_list[curr]:
            in_deg_arr[node] -= 1
            if in_deg_arr[node] == 0:
                queue.append(node)
    
    for res in results:
        print(res, end="--->")
    print()


if __name__ == '__main__':
    n = 6  # Number of nodes

    # Edges
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]

    adj_list = [[] for _ in range(n)]
    for edge in edges:
        adj_list[edge[0]].append(edge[1])

    topo_sort(adj_list, n)

