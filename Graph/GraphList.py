# Create a graph by using adjacency list


def add_edge(graph, source, destination, directed=False):
    graph[source].append(destination)
    if not directed:
        graph[destination].append(source)
    
def print_graph(graph):
    v = len(graph)
    for i in range(v):
        print(f"{i}: ", end=" ")
        for j in range(len(graph[i])):
            print(graph[i][j], end=", ")
        print()

if __name__ == '__main__':
    vertices = 5
    graph = [[] for _ in range(vertices)]

    add_edge(graph, 0, 1)
    add_edge(graph, 0, 2)
    add_edge(graph, 1, 3)
    add_edge(graph, 1, 4)
    add_edge(graph, 2, 4)

    print_graph(graph)
