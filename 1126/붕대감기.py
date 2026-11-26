def solution(bandage, health, attacks):
    answer = 0

    t = bandage[0] # 기술시전시간
    x = bandage[1] # 초당 체력 회복량
    y = bandage[2] # 연속 시전 성공시 추가 회복량

    시간 = attacks[-1][0]
    연속성공시간 = 0
    현재체력 = health

    공격받은시간 = {}

    for i in attacks:
        공격받은시간[i[0]] = i[1]

    for 시간 in range(1, 시간+1):

        if 시간 in 공격받은시간:
            # 연속성공시간  = 0
            연속성공시간 = 0
            현재체력 -= 공격받은시간[시간]
            if 현재체력 <= 0:
                return -1

        else:
            # 연속성공시간 + 1
            연속성공시간 += 1
            
            if 현재체력 < health:
                현재체력 += x
                if 현재체력 >= health:
                    현재체력 = health

                if 연속성공시간 == y:
                    현재체력 += y
                    if 현재체력 >= health:
                        현재체력 = health
    return 현재체력

print(solution(
    [5, 1, 5],
    30,
    [[2, 10], [9, 15], [10, 5], [11, 5]]
))

print(solution(
    [3, 2, 7],
    20,
    [[1, 15], [5, 16], [8, 6]]
))

print(solution(
    [4, 2, 7],
    20,
    [[1, 15], [5, 16], [8, 6]]
))

print(solution(
    [1, 1, 1],
    5,
    [[1, 2], [3, 2]]
))