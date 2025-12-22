import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

visited = [False]*(N+1)
dfs_order = []
stack = [V]

while stack:
    v = stack.pop()
    if visited[v]:
        continue
    visited[v] = True
    dfs_order.append(v)
    for i in reversed(graph[v]):
        if not visited[i]:
            stack.append(i)

visited = [False]*(N+1)
bfs_order = []
q = deque([V])
visited[V] = True

while q:
    v = q.popleft()
    bfs_order.append(v)
    for i in graph[v]:
        if not visited[i]:
            visited[i] = True
            q.append(i)

print(*dfs_order)
print(*bfs_order)

# DFS 재귀
# dfs_order = []
# visited = [False]*(N+1)
# def dfs(v):
#     visited[v] = True
#     dfs_order.append(v)
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)
# dfs(V)
# print(*dfs_order)
