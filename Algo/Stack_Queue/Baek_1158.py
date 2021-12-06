#11866과 동일한 문제
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

#시간 복잡도가 더 적은 풀이 방법(수학 풀이)
# import sys
#
# n, k = map(int, sys.stdin.readline().split())
#
# number = [i+1 for i in range(n)]
# result = []
# now = 0
# while number:
#     now = (now + k-1)%(len(number))
#     result.append(number.pop(now))
# print('<' + ', '.join(map(str, result)) + '>')

#queue를 이용해서 풀면 자연스럽게 느려진다.
# from collections import deque
#
# import sys
# input = sys.stdin.readline
#
# n, k = map(int, input().split())
# q = deque(range(1, n+1))
#
# print('<',end='')
# while len(q) > 1:
#     for _ in range(k-1):
#         tmp_data = q.popleft()
#         q.append(tmp_data)
#     print(q.popleft(), end=', ')
# print(q.popleft(), end='>')