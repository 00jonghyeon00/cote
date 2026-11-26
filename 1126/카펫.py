def solution(brown, yellow):
    total = brown + yellow
    # 가로 x, 세로 y
    # x * y = total
    # x-2 * y-2 = yellow
    # x >= y
    # total // y = 0
    answer = []

    for y in range(3, total):
        if total % y == 0:
            x = total // y
            if x >= y and (x-2) * (y-2) == yellow:
                answer.append(x)
                answer.append(y)

    return answer

brown2 = 8
yellow2 = 1

print(solution(brown2, yellow2))