players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

def solution(players, callings):
    선수이름과순서 = {}
    for idx,i in enumerate(players):
        선수이름과순서[i] = idx

    for 호명 in callings:
        현재순서 = 선수이름과순서[호명]  
        앞선수 = players[현재순서 - 1] 
        선수이름과순서[호명] = 현재순서 - 1
        선수이름과순서[앞선수] = 현재순서
        players[현재순서-1] = 호명
        players[현재순서] = 앞선수
    return players
       
print(solution(players, callings))