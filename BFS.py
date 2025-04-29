from collections import deque

def bfs(adj):
    V = len(adj)
    res, visited, q = [], [0]*V, deque()
    visited[0] = 1
    q.append(0)
    while q:
        curr = q.popleft()
        res.append(curr)
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = 1
                q.append(x)
    return res

if __name__ == "__main__":
    n = int(input("Enter number of vertices: "))
    adj = []
    for i in range(n):
        adj.append(list(map(int, input(f"Enter neighbors of vertex {i} (space-separated): ").split())))
    for i in bfs(adj):
        print(i, end=" ")
