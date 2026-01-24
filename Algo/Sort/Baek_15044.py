# Fase
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort(reverse=True)

last_score = nums[k - 1]
res = k

for i in range(k, n):
    if nums[i] == last_score:
        k += 1
    else:
        break

print(k)