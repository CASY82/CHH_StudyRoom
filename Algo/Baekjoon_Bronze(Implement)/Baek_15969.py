import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

print(max(nums) - min(nums))