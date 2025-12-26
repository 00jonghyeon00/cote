import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()

    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1:
                q.append((y,x))

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if grid[ny][nx] == 0:
                    grid[ny][nx] = grid[y][x] + 1
                    q.append((ny,nx))
    
bfs()

ans = 0
for i in grid:
    if 0 in i:
        print(-1)
        break
    ans = max(ans, max(i))
else:
    print(ans-1)