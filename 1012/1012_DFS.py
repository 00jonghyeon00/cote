import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x, grid, visited, M, N):
    stack = [(y, x)]
    visited[y][x] = True
    while stack:
        y, x = stack.pop()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < M:
                if grid[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = True
                    stack.append((ny,nx))

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    grid = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        grid[y][x] = 1
    
    cnt = 0

    for y in range(N):
        for x in range(M):
            if grid[y][x] == 1 and not visited[y][x]:
                cnt +=1
                dfs(y, x, grid, visited, M, N)
    
    print(cnt)