import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 1
start = nums[0]
res = 1

for i in range(1, n):
    if start > nums[i]:
        cnt = 1
    else:
        cnt += 1

    start = nums[i]
    res = max(res, cnt)

print(res)