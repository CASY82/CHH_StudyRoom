import sys
import heapq

n, m, k = map(int, sys.stdin.readline().split())
work = []
heapq.heapify(work)
satisfied = 0
res = 0
res_list = []

for _ in range(n):
    heapq.heappush(work, -int(sys.stdin.readline()))

while True:
    if not work:
        break

    now = -heapq.heappop(work)
    satisfied = (satisfied // 2) + now
    res_list.append(satisfied)

    now -= m
    if now > k:
        heapq.heappush(work, -now)

    res += 1

print(res)
for i in res_list:
    print(i)

# 다른 사람 풀이
# import sys
# import heapq
# input = sys.stdin.readline
#
# n, m, k = map(int, input().split())
# h = []
#
# for i in range(n):
#     x = int(input())
#     heapq.heappush(h, -x)
#
# y = 0
# res = []
#
# while True:
#     p = -heapq.heappop(h)
#
#     if p <= k:
#         break
#
#     x = y // 2 + p
#     res.append(x)
#     p -= m
#     heapq.heappush(h, -p)
#     y = x
#
# print(len(res))
# print(*res, sep = '\n')