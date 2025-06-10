import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
now = nums[0]
res = [now]

for i in range(1, n):
    if now < nums[i]:
        res.append(nums[i])
        now = nums[i]

print(len(res))
print(*res)