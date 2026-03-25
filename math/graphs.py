from collections import deque

def read_adj_matrix(filename):
    with open(filename) as f:
        return [list(map(int, line.strip().split(','))) for line in f]

def matrix_to_adj(matrix):
    n = len(matrix)
    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                adj[i].append(j)
    return adj

def connected_components(adj):
    n = len(adj)
    visited = [False]*n
    comps = []
    for v in range(n):
        if not visited[v]:
            comp = []
            stack = [v]
            visited[v] = True
            while stack:
                u = stack.pop()
                comp.append(u)
                for w in adj[u]:
                    if not visited[w]:
                        visited[w] = True
                        stack.append(w)
            comps.append(comp)
    return comps

def vertex_max_degree(adj):
    degs = [len(adj[i]) for i in range(len(adj))]
    return degs.index(max(degs)), max(degs)
