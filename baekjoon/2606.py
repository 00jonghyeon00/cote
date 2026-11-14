import sys
from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS
for i in range(1, N+1):
    graph[i].sort()

# DFS 재귀
dfs_order = []
visited = [False] * (N+1)

def dfs(start):
    visited[start] = True
    dfs_order.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(dfs_order)
print(len(dfs_order)-1)

# DFS stack
dfs_order = []
visited = [False] * (N+1)

# BFS
bfs_order = []
visited = [False] * (N+1)

def bfs(start):
    q = deque([start])
    visited[start] = True
    count = 0

    while q:
        v = q.popleft()
        bfs_order.append(v)
        for i in graph[v]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1
    return count

print(bfs(1))
print(bfs_order)


