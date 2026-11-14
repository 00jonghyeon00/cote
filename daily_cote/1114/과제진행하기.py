plans = [
    ["science", "12:40", "50"],
    ["music", "12:20", "40"],
    ["history", "14:00", "30"],
    ["computer", "12:30", "100"]
]

def solution(plans):
    def 시작시간변환(과제시작시간):
        a,b = 과제시작시간.split(":")
        a = int(a)
        b = int(b)
        return a*60 + b
    
    a = []
    
    for i in plans:
        과목 = i[0]
        시작시간 = i[1]
        필요시간 = int(i[2])
        시작시간 = 시작시간변환(시작시간)
        a.append([과목, 시작시간, 필요시간])
    
    b = sorted(a, key=lambda x : x[1])
    
    result = []
    stack = []

    for i in range(len(b) - 1):
        name, start, playtime = b[i]
        next_start = b[i+1][1]
        남은시간 = next_start - start

        if playtime > 남은시간:
            stack.append([name, playtime - 남은시간])
        else:
            result.append(name)
            남은시간 -= playtime
            while 남은시간 > 0 and stack:
                if stack[-1][1] <= 남은시간:
                    name, time = stack.pop()
                    result.append(name)
                    남은시간 -= time
                else:
                    stack[-1][1] -= 남은시간
                    남은시간 = 0
    result.append(b[-1][0])

    while stack:
        과목, 시간 = stack.pop()
        result.append(과목)
    return result
    
print(solution(plans))        


a = [1,2,3,4]
print(a.pop(), a)