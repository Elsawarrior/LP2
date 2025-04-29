import heapq

def astar(start, goal, graph, h):
    q = [(h[start], 0, start)]
    visited = set()
    while q:
        f, g, u = heapq.heappop(q)
        if u == goal:
            return g
        if u in visited: continue
        visited.add(u)
        for v, w in graph[u]:
            if v not in visited:
                heapq.heappush(q, (g + w + h[v], g + w, v))
    return -1

n, m = map(int, input("Enter n m: ").split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))  # remove this line for directed graph

h = list(map(int, input("Enter heuristic h[]: ").split()))
s, g = map(int, input("Start Goal: ").split())
print("A* Cost:", astar(s, g, graph, h))
