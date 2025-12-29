import sys

input = sys.stdin.readline

N = int(input())
grid = [list(map(str, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

region = 0
region_2 = 0

def dfs(y, x, mode):
    stack = [(y,x)]
    start = grid[y][x]
    visited[y][x] = True

    if mode == "1":
        while stack:
            y, x = stack.pop()
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < N and 0 <= nx < N:
                    if grid[ny][nx] == start and not visited[ny][nx]:
                        visited[ny][nx] = True
                        stack.append((ny,nx))
    else:
        while stack:
            y, x = stack.pop()
            for k in range(4):
                ny = y + dy[k]
                nx = x + dx[k]
                if 0 <= ny < N and 0 <= nx < N:
                    if not visited[ny][nx]:
                        if start == "B":
                            if grid[ny][nx] == "B":
                                visited[ny][nx] = True
                                stack.append((ny, nx))
                        else:
                            if grid[ny][nx] in ('R', 'G'):
                                visited[ny][nx] = True
                                stack.append((ny, nx))

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs(y, x, "1")
            region += 1

visited = [[False]*N for _ in range(N)]

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            dfs(y, x, "2")
            region_2 += 1

print(region, region_2)