# import sys
#
# n, x = map(int, sys.stdin.readline().split())
# maginot_weight = list(map(int, sys.stdin.readline().split()))
# add_weight = list(map(int, sys.stdin.readline().split()))
#
# now = 0
# cnt = 0
#
# for i in range(n):
#     check_weight = now + add_weight[i]
#     if check_weight - x >= maginot_weight[i]:
#         while check_weight - x >= maginot_weight[i]:
#             now = check_weight - x
#             check_weight = now
#             cnt += 1
#     else:
#         now += add_weight[i]
#
# if cnt > 0:
#     print(cnt)
# else:
#     print(-1)

import sys

n, x = map(int, sys.stdin.readline().split())
maginot_weight = list(map(int, sys.stdin.readline().split()))
add_weight = list(map(int, sys.stdin.readline().split()))

s = 0
ans = 10 ** 30

for i in range(n):
    s += add_weight[i]
    if s < maginot_weight[i]:
        print(-1)
        sys.exit(0)

print((s - maginot_weight[-1]) // x)
