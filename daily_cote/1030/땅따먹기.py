land = [
    [1, 2, 3, 5],
    [5, 6, 7, 8],
    [4, 3, 2, 1]
]

# N행 4열
# land[?][0~3]
# 연속된 두 행에서 같은 열 선택 x

def solution(land):
    n = len(land)
    m = len(land[0])
    dp = [[0]*m for _ in range(n)]
    return dp
print(solution(land))