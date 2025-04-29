import heapq

def prim(n, edges):
    graph = [[] for _ in range(n)]
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))

    visited = [0] * n
    heap = [(0, 0)]
    total = 0

    while heap:
        w, u = heapq.heappop(heap)
        if visited[u]: continue
        visited[u] = 1
        total += w
        for nw, v in graph[u]:
            if not visited[v]:
                heapq.heappush(heap, (nw, v))
    return total

n, m = map(int, input("Enter n m: ").split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print("Prim:", prim(n, edges))
