import sys

input = sys.stdin.readline

N = int(input().strip())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True
    cnt = 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                cnt += dfs(nx, ny)
    return cnt

sizes = []

for x in range(N):
    for y in range(N):
        if grid[x][y] == 1 and not visited[x][y]:
            sizes.append(dfs(x, y))

sizes.sort()
print(len(sizes))
print("\n".join(map(str, sizes)))