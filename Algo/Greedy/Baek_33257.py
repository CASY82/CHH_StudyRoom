import sys

n, e = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort()
res = 1

for i in range(n - 1):
    if nums[i + 1] - nums[i] < e:
        continue
    else:
        res += 1

print(res)

# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
# def solution():
#     n, e = map(int, input().split())
#     d = sorted(list(map(int, input().split())))
#     count = 1
#     for i in range(1, n):
#         if d[i] - d[i - 1] >= e:
#             count += 1
#     print(count)
# solution()