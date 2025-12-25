import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input().strip())

for tc in range(T):
    M, N, K = map(int, input().split())

    grid = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1

    worms = 0

    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1 and not visited[y][x]:
                worms += 1
                q = deque([(y, x)])
                visited[y][x] = True

                while q:
                    cy, cx = q.popleft()
                    for i in range(4):
                        ny = cy + dy[i]
                        nx = cx + dx[i]
                        if 0 <= ny < N and 0 <= nx < M:
                            if grid[ny][nx] == 1 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                q.append((ny, nx))

    print(worms)