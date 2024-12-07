import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
res = 0

for i in range(1, n - 1):
    res = max(res, (min(nums[i - 1], nums[i + 1]) + nums[i]))

print(max(res, nums[0], nums[-1]))

# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# a = list(map(int, input().split()))
# ans = max(a)
#
# for i in range(1, n - 1):
#     if min((a[i - 1], a[i + 1])) > 0:
#         ans = max((ans, a[i] + min((a[i - 1], a[i + 1]))))
# print(ans)

# import sys
# input = sys.stdin.readline
#
# n = int(input())
# lst = list(map(int, input().split()))
# mx = 0
# for i in range(1, n-1):
#     sm = 0
#     if lst[i-1] > lst[i+1]:
#         sm += lst[i] + lst[i+1]
#     else:
#         sm += lst[i] + lst[i-1]
#     if sm > mx:
#         mx = sm
# print(max(mx, lst[0], lst[-1]))