from collections import deque
x = 3
y = 4
q = deque([ (x, y)])
print(q)
a,b = q.popleft()
print(a,b)