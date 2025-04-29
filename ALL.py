#PRIMS
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


#KRUSKALS
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


#CHATBOT
print("Hello, I m your chatbot assistant!")
print("Welcome to Library!")
print("Type 'help' to see options and 'exit' to leave ")

books = {
    "maths": "available",
    "science" : "out of stock",
    "english" : "available"
}
while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Thank you!")
        break
    elif user_input == "help":
        print("Chatbot: I can help you with:\n")
        print("1. Store timings. \n")
        print("2. Book Availability.\n")
        print("3. Payment methods\n")
        print("Enter exit to leave chatbot\n")

    elif user_input == 'time':
        print("We are available from 9 am to 9 pm from Monday to Saturday\n Thank you!!")

    elif user_input == 'book':
        print(books)

    elif user_input == "payment":
        print("We accept cash, card and upi.\n Thank you!")

    else:
        print("Incorrect input!")

#A* ALGORITHM
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


#DFS
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


#BFS
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


#NQUEEN

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(board, col, n):
    if col >= n:
        print_board(board)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = "Q"
            res = solve_n_queens(board, col + 1, n) or res
            board[i][col] = "."  # Backtrack

    return res

def n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    if not solve_n_queens(board, 0, n):
        print("No solution exists")

# Example usage:
n = 4
n_queens(n)

