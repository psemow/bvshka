def bfs_shortest_path(adj, start, target):
    dist = [-1]*len(adj)
    dist[start] = 0
    q = deque([start])
    while q:
        u = q.popleft()
        if u == target: return dist[u]
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return -1

def all_pairs_bfs(adj):
    n = len(adj)
    dist_matrix = [[-1]*n for _ in range(n)]
    for s in range(n):
        dist = [-1]*n
        dist[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        dist_matrix[s] = dist
    return dist_matrix
