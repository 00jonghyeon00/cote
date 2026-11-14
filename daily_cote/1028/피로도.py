k = 80
dungeons = [
    [80, 20],
    [50, 40],
    [30, 10]
]

from itertools import permutations

def solution(k, dungeons):
    answer = 0
    던전순서 = []
    던전순서갯수 = len(dungeons)

    for i in permutations(range(던전순서갯수)):
        던전순서.append(i)

    for i in 던전순서: #(0 2 1)
        현재피로도 = k
        탐험횟수 = 0
        for j in i: # 0 2 1 
            최소필요피로도, 소모피로도 = dungeons[j]
            if 현재피로도 >= 최소필요피로도:
                현재피로도 -= 소모피로도
                탐험횟수 += 1
            else:
                break
        answer = max(answer, 탐험횟수)

    return answer        
        
print(solution(k, dungeons))