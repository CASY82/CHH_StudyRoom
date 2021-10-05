from collections import deque

n = int(input())
result = []
dq = deque()
dq.extend([i for i in range(1, n+1)])

while len(dq) >= 2:
    result.append(dq.popleft())
    dq.append(dq.popleft())

result.append(dq[0])

for i in result:
    print(i, end=' ')