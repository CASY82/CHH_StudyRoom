import sys
from collections import deque

n = int(sys.stdin.readline())
want_pizza = list(map(int, sys.stdin.readline().split()))

time = 0
result = []
que = deque()

for i in range(len(want_pizza)):
    que.append((want_pizza[i], i))

while que:
    now, num = que.popleft()

    time += 1
    now -= 1

    if now == 0:
        result.append((time, num))
        continue

    que.append((now, num))

result.sort(key=lambda x:x[1])

for i in range(len(result)):
    print(result[i][0], end=' ')

# 다른 사람 풀이
# n = int(input())
# pizza = list(map(int, input().split()))
#
# cnt, P = 0, sum(pizza)
# order = [0] * n
#
# while (cnt < P):
#     for i in range(n):  # n조각 순서대로 돌면서
#         if pizza[i] == 0:  # 남은 조각이 없으면 pass
#             continue
#         pizza[i] -= 1
#         cnt += 1
#         if pizza[i] == 0:  # 마지막 조각일때 order에 저장
#             order[i] = cnt
#
# print(' '.join(map(str, order)))