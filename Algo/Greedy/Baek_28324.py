import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.reverse()
res = []
now = 0

if n > 1:
    for i in range(len(nums) - 1):
        if now >= nums[i]:
            now = nums[i]
        else:
            now += 1

        res.append(now)

    if res[-1] < nums[-1]:
        res.append(res[-1] + 1)
    else:
        res.append(nums[-1])
else:
    res.append(1)

print(sum(res))

# 다른 사람 풀이
# import sys
#
# n = int(input())
# v = list(map(int, input().split()))
#
# a = 0
# ans = 0
#
# for i in v[::-1]:
#
#     if a < i:
#         a += 1
#     else:
#         a = i
#
#     ans += a
#
# print(ans)