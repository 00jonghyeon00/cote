import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dist = [[0]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x):
    q = deque([(y, x)])
    visited[y][x] = True
    dist[y][x] = 1
    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if grid[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))

bfs(0, 0)
print(dist[N-1][M-1])


            

