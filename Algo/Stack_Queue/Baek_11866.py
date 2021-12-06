from collections import deque
import sys
n, k = map(int, sys.stdin.readline().split())
que = deque([(i+1) for i in range(n)])
result = []

while True:
    if not que:
        break

    tmp = k

    for i in range(1, k):
        que.append(que.popleft())

    result.append(que.popleft())


print("<", end='')
for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], end='', sep='')
    else:
        print(result[i], ", ", end='', sep='')
print(">")
