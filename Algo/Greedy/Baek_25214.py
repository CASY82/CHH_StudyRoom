import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

low_val = nums[0]
best = 0
res = []
res.append(best)

for num in nums[1:]:
    if num - low_val > best:
        best = num - low_val
    if num < low_val:
        low_val = num
    res.append(best)

print(*res)