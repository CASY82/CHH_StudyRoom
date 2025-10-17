# import sys
#
# n, k = map(int, sys.stdin.readline().split())
#
# safe = []
# broken = []
#
# for _ in range(n):
#     height, status = sys.stdin.readline().strip().split()
#
#     height = int(height)
#
#     if status == "SAFE":
#         safe.append(height)
#     elif status == "BROKEN":
#         broken.append(height)
#
# res_low = k
# res_high = 1
#
# if len(broken) == 0:
#     res_high = max(safe)
#     res_low = max(safe) + 1
# elif len(safe) == 0:
#     res_low = min(broken)
#     res_high = min(broken) - 1
# else:
#     res_low = max(safe) + 1
#     res_high = min(broken) - 1
#
# print(res_low, res_high)

import sys

n, k = map(int, sys.stdin.readline().split())

safe_floors = [1]
broken_floors = [k]

for _ in range(n):
    height, status = sys.stdin.readline().strip().split()
    height = int(height)

    if status == "SAFE":
        safe_floors.append(height)
    elif status == "BROKEN":
        broken_floors.append(height)

max_confirmed_safe = max(safe_floors)
min_confirmed_broken = min(broken_floors)

res_low_ans = max_confirmed_safe + 1
res_high_ans = min_confirmed_broken - 1

print(res_low_ans, res_high_ans)