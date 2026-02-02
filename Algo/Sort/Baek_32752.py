# 수열이에요?
import sys

n, l, r = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

start = nums[:l - 1]
tmp = nums[l - 1:r]
end = nums[r:]

tmp.sort()
array = start + tmp + end

res = 1

for i in range(1, n):
    if array[i - 1] > array[i]:
       res = 0
       break

print(res)