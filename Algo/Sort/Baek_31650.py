# import sys
#
# n, q = map(int, sys.stdin.readline().split())
# c = list(map(int, sys.stdin.readline().split()))
# t = list(map(int, sys.stdin.readline().split()))
#
# d = []
#
# for i in range(n):
#     d.append(c[i] - t[i])
#
# d.sort()
#
# for _ in range(q):
#     v, s = map(int, sys.stdin.readline().split())
#     tmp = 0
#
#     for j in range(n):
#         if s < d[j]:
#             tmp += 1
#
#     if tmp >= v:
#         print("YES")
#     else:
#         print("NO")

import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())
c = list(map(int, input().split()))
t = list(map(int, input().split()))

d = [ci - ti for ci, ti in zip(c, t)]
d.sort()

for _ in range(Q):
    V, S = map(int, input().split())

    cnt = N - bisect.bisect_right(d, S)
    print("YES" if cnt >= V else "NO")