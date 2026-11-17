wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]
n = 7

# 1-3
# 2-3
# 
def solution(wires, n):
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    return graph

print(solution(wires, n))