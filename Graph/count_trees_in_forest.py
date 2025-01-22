"""
Given n nodes of a forest (collection of trees), find the number of trees in the forest.

Examples : 

Input :  edges[] = {0, 1}, {0, 2}, {3, 4}
Output : 2
Explanation : There are 2 trees
                   0       3
                  / \       \
                 1   2       4
"""

def dfs(graph, visited, src):
    visited[src] = True
    for i in graph[src]:
        if not visited[i]:
            dfs(graph, visited, i)

def countTrees(graph):
    res = 0
    visited = [False] * len(graph)
    for i in range(len(graph)):
        if visited[i] == False:
            res+=1
            dfs(graph, visited, i)
    return res


def addEdge(graph, src, dest):
    graph[src].append(dest)
    graph[dest].append(src)

if __name__ == '__main__':
 
    V = 8
    adj = [[] for i in range(V)] 
    addEdge(adj, 0, 1) 
    addEdge(adj, 0, 2) 
    addEdge(adj, 3, 4) 
    addEdge(adj, 5, 6) 
    addEdge(adj, 5, 7) 
    print(f"Total Forest is {countTrees(adj)}")