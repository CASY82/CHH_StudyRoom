import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

nums.sort(reverse=True)
minus = 0

for i in range(1, k):
    minus += i

print(sum(nums[:k]) - minus)