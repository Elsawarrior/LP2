def kruskal(n, edges):
    parent = list(range(n))
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    edges.sort(key=lambda x: x[2])
    total = 0

    for u, v, w in edges:
        ru, rv = find(u), find(v)
        if ru != rv:
            parent[ru] = rv
            total += w
    return total

n, m = map(int, input("Enter n m: ").split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
print("Kruskal:", kruskal(n, edges))
