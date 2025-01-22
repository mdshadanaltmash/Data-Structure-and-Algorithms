"""
Link to question: https://www.geeksforgeeks.org/find-the-level-of-given-node-in-an-undirected-graph/

Given an undirected graph with V vertices and E edges and a node X, The task is to find the level of node X in the undirected graph. If X does not exist in the graph then return -1.

Note: Traverse the graph starting from vertex 0.

Examples:


Input: V = 5, Edges = {{0, 1}, {0, 2}, {1, 3}, {2, 4}}, X = 3
Output: 2
Explanation: Starting from vertex 0, at level 0 we have node 0, at level 1 we have nodes 1 and 2 and at level 2 we have nodes 3 and 4. So the answer is 2

nput: V = 5, Edges = {{0, 1}, {0, 2}, {1, 3}, {2, 4}}, X = 5
Output: -1
Explanation: Vertex 5 is not present in the given graph so answer is -1

"""

from collections import deque
def find_level(V, edges, x):
    max_vertex = 0
    for vertex in edges:
        max_vertex = max(max_vertex, vertex[0], vertex[1])
    
    adj_list = [[] for _ in range(max_vertex+1)]
    for i in range(len(edges)):
        adj_list[edges[i][0]].append(edges[i][1])
        adj_list[edges[i][1]].append(edges[i][0])
    
    if x>max_vertex or len(adj_list)==0:
        return -1

    visited = [False]*(max_vertex+1)
    q = deque()
    q.append(0)
    level = 0

    # while q:
    #     curr = q.popleft()
    #     if curr == x:
    #         return level
    #     level+=1
    #     for node in adj_list[curr]:
    #         if node == x:
    #             return level
    #         if not visited[node]:
    #             visited[node]=True
    #             q.append(node)
    # return -1
    while(len(q)>0):
        sz=len(q)
        while(sz>0):
            currentNode=q[0]
            q.popleft()
            if(currentNode==X):
                return level
            for it in adj_list[currentNode]:
                if not visited[it]:
                    q.append(it)
                    visited[it]=1
            sz=sz-1
        level=level+1
    return -1



V=5
edges=[[0,1],[0,2],[1,3],[2,4],[3,5],[5,6]]
X=6
 
#Function call
level=find_level(V,edges,X)
print(level)