import sys
from collections import deque




input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
visited = [[False]*N for _ in range(M)]

    
    

# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# def bfs(y, x):
#     if grid[y][x] == 1:
#         q = deque([(y,x)])
#         visited[y][x] = True
#         while q:
#             y, x = q.popleft()
#             for k in range(4):
#                 ny = y + dy[k]
#                 nx = x + dx[k]
#                 if 0 <= ny < N and 0 <= nx < M:
#                     if grid[ny][nx] == 1 and not visited[ny][nx]:
#                         visited[ny][nx] = True
