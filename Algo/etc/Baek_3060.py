# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#
#     before = list(map(int, sys.stdin.readline().split()))
#     day = 1
#     next = before.copy()
#
#     while sum(next) <= n:
#         day += 1
#
#         for i in range(len(before)):
#             next[i] = before[i] + before[i - 1] + before[(i + 1) % len(before)]
#
#     print(day)

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    before = list(map(int, sys.stdin.readline().split()))
    day = 1
    total = sum(before)

    while total <= n:
        day += 1
        total *= 4

    print(day)