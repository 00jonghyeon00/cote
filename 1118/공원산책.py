def solution(park, routes):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n = len(park)
    m = len(park[0])

    direction = {"N":0, "E":1, "S":2, "W":3}

    # s찾기
    for i in range(n):
        for j in range(m):
            if park[i][j] == "S":
                x, y = i, j

    for route in routes:
        방향, 거리 = route.split()
        거리 = int(거리)

        k = direction[방향]

        tx, ty = x, y
        가능 = True

        for _ in range(거리):
            tx += dx[k]
            ty += dy[k]

            if not (0<=tx<n and 0<=ty<m):
                가능 = False
                break

            if park[tx][ty] == "X":
                가능 = False
                break
        if 가능:
            x, y = tx, ty
            
    return [x, y]


park1 = ["SOO", "OOO", "OOO"]
routes1 = ["E 2", "S 2", "W 1"]

park2 = ["SOO", "OXX", "OOO"]
routes2 = ["E 2", "S 2", "W 1"]

park3 = ["OSO", "OOO", "OXO", "OOO"]
routes3 = ["E 2", "S 3", "W 1"]

print(solution(park1, routes1))  # [2, 1]
print(solution(park2, routes2))  # [0, 1]
print(solution(park3, routes3))  # [0, 0]