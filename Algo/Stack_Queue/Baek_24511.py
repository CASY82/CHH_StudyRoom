import sys
from collections import deque

n = int(sys.stdin.readline())

# queuestack = [deque() for _ in range(n)]
queuestack = deque()

# 큐/스택 확인
check = list(map(int, sys.stdin.readline().split()))
# origin_data
first_data = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
# new set
new_data = list(map(int, sys.stdin.readline().split()))

res = []

# for i, dq in enumerate(queuestack):
#     if check[i] == 1:
#         continue
#     dq.append(first_data[i])

for i in range(n):
    if check[i] == 1:
        continue
    queuestack.append(first_data[i])

# length = len(queuestack)

for data in range(m):
    tmp = new_data[data]
    queuestack.appendleft(tmp)
    tmp = queuestack.pop()

    res.append(tmp)

print(*res)