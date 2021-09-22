#시간 초과...
# n, k = map(int, input().split())
# count = 0
# bottle = []
#
# for i in range(n):
#     bottle.append(1)
#
# while True:
#     if k == len(bottle):
#         break
#
#     if len(bottle) >= 2:
#         if bottle[len(bottle) - 1] == bottle[len(bottle) - 2]:
#             bottle[len(bottle) - 1] <<= 1
#             bottle.sort(reverse=True)
#             bottle.pop()
#         else:
#             count += 1
#             bottle.append(1)
#     else:
#         count += 1
#         bottle.append(1)
#
# print(count)
# 다른사람 풀이 참고

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = 0
while bin(N).count('1') > K:
    plus = 2 ** (bin(N)[::-1].index('1'))
    answer += plus
    N += plus
print(answer)