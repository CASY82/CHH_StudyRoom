# Q-인덱스
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort(reverse=True)
res = 0
cnt_check = True

for i in range(1, n + 1):
    for check in range(i):
        if nums[check] < i:
            cnt_check = False

    if cnt_check:
        res += 1

print(res)