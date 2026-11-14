maps1 = [
    "SOOOL",
    "XXXXO",
    "OOOOO",
    "OXXXX",
    "OOOOE"
]

maps2 = [
    "LOOXS",
    "OOOOX",
    "OOOOO",
    "OOOOO",
    "EOOOO"
]

from collections import deque

# BFS 2회 풀이
def solution_1(maps):
    n = len(maps)
    m = len(maps[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for x in range(n):
        for y in range(m):
            if maps[x][y] == "S":
                S = (x, y)
            elif maps[x][y] == "L":
                L = (x, y)
            elif maps[x][y] == "E":
                E = (x, y)

    def bfs(start, end):
        distance = [[-1] * m for _ in range(n)]
        que = deque([start])
        distance[start[0]][start[1]] = 0

        while que:
            x, y = que.popleft()
            if (x, y) == end:
                return distance[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<n and 0<=ny<m:
                    if maps[nx][ny] != "X" and distance[nx][ny] == -1:
                        distance[nx][ny] = distance[x][y] + 1
                        que.append((nx, ny))
        return -1
    
    a = bfs(S, L)
    if a == -1:
        return -1
    b = bfs(L, E)
    if b == -1:
        return -1
    return a + b

print(solution_1(maps1))

# 상태 + bfs 1회