# import sys
# import bisect
#
# n = int(sys.stdin.readline())
# nums = []
#
# for _ in range(n):
#     nums.append(int(sys.stdin.readline()))
#
# nums.sort()
#
# s = []
#
# for i in range(n):
#     for j in range(i, n):
#         s.append(nums[i] + nums[j])
#
# s.sort()
# res = 0
# check = False
#
# for k in range(n - 1, -1, -1):
#     for x in range(n):
#         target = nums[k] - nums[x]
#
#         ## 시간 초과
#         if target in s:
#             res = nums[k]
#             check = True
#             break
#
#     if check:
#         break
#
# print(res)

import sys
import bisect

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()

s = []

for i in range(n):
    for j in range(i, n):
        s.append(nums[i] + nums[j])

s.sort()
res = 0
check = False

for k in range(n - 1, -1, -1):
    for x in range(n):
        target = nums[k] - nums[x]

        idx = bisect.bisect_left(s, target)
        if idx < len(s) and s[idx] == target:
            res = nums[k]
            check = True

    if check:
        break

print(res)