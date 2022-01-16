import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    dq = deque()

    for i,v in enumerate(priority):
        dq.append([i,v])

    priority.sort(reverse=True)
    i = 0
    #우선순위대로 popleft
    while dq:
        if priority[i] == dq[0][1]:
            result = dq.popleft()
            i += 1

            if result[0] == m:
                break
        else:
            dq.append(dq.popleft())

    print(i)