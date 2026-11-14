import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N+1)

# # dfs recursive

# def dfs(v):
#     visited[v] = True
#     for j in graph[v]:
#         if not visited[j]:
#             dfs(j)
# cnt = 0
# for i in range(1, N+1):
#     if not visited[i]:
#         cnt += 1
#         dfs(i)

# print(cnt)

# dfs stack
cnt = 0

for i in range(1, N+1):
    if visited[i]:
        continue
    cnt += 1
    stack = [i]
    visited[i] = True
    while stack:
        v = stack.pop()
        for j in graph[v]:
            if not visited[j]:
                visited[j] = True
                stack.append(j)
print(cnt)