people1 = [70, 50, 80, 50]
limit1 = 100

people2 = [70, 80, 50]
limit2 = 100


def solution(people, limit):
    people.sort() # 50 50 70 80
    left = 0
    right = len(people) - 1
    answer = 0

    while left <= right: # 0 3 -> 
        if left < right and people[left] + people[right] <= limit:
            left += 1
        right -= 1
        answer += 1
    return answer 
        

print(solution(people1, limit1))
print(solution(people2, limit2))