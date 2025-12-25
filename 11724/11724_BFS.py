from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        q = deque([i])
        visited[i] = True
        while q:
            a = q.popleft()
            for j in graph[a]:
                if not visited[j]:
                    visited[j] = True
                    q.append(j)
print(cnt)