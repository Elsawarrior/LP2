def dfs(adj, v, res, s=0):
    v[s] = 1
    res.append(s)
    for i in range(len(adj)):
        if adj[s][i] and not v[i]:
            dfs(adj, v, res, i)

n, m = map(int, input("Enter number of vertices and edges: ").split())
adj = [[0]*n for _ in range(n)]

print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = adj[v][u] = 1

res = []
dfs(adj, [0]*n, res)
print("DFS traversal:", *res)
