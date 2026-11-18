wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
n = 9

from collections import deque

def solution(wires, n):
    # 인접리스트 
    graph = [[] for _ in range(n+1)]
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)

    # bfs
    def bfs(start):
        visited = [False] * (n+1)
        que = deque([start])
        visited[start] = True
        count  = 1

        while que:
            node = que.popleft()
            for next_node in graph[node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    que.append(next_node)
                    count += 1
        return count

    answer = float('inf')

    for a,b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        count = bfs(a)

        diff = abs(count - (n-count))
        answer = min(answer, diff)

        graph[a].append(b)
        graph[b].append(a)

    return answer

print(solution(wires, n))