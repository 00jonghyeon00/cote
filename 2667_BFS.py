import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

sizes = []

for x in range(N):
    for y in range(N):
        if grid[x][y] == 1 and not visited[x][y]:
            q = deque( [ (x,y) ] )
            visited[x][y] = True
            cnt = 0

            while q:
                cx, cy = q.popleft()
                cnt += 1
                for i in range(4):
                    nx = cx + dx[i]
                    ny = cy + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if grid[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
            sizes.append(cnt)

sizes.sort()
print(len(sizes))
for k in sizes:
    print(k)